"""
Load and transform input data for loanfinder, save to ``raw`` folder.
"""
import argparse
import collections
import csv
import json
import shutil

def main():
    """
    #. Read the filenames with the argparse library
    #. Assign the file contents to variables
    #. Create four dictionaries from them for later use
    #. Create input for `loanpy.loanfinder.phonetic_matches
       <https://loanpy.readthedocs.io/en/latest/documentation.html#loanpy.loanfinder.phonetic_matches>`_.
    #. Write files to ``raw`` folder.
    """
    # read filenames with argparse library
    parser = argparse.ArgumentParser(description='Load Hungarian and Gothic data.')
    parser.add_argument('--hungarian', type=str,
                        default='gerstnerhungarian/loanpy/hun1416unknown,uncertain.tsv',
                        help='Path to the Hungarian TSV file.')
    parser.add_argument('--hun_entries', type=str,
                        default='gerstnerhungarian/cldf/entries.csv',
                        help='Path to Hungarian entries table.')
    parser.add_argument('--hun_senses', type=str,
                        default='gerstnerhungarian/cldf/senses.csv',
                        help='Path to Hungarian senses table.')
    parser.add_argument('--gothic', type=str,
                        default='koeblergothic/cldf/adapt.csv',
                            help='Path to the Gothic csv file.')
    parser.add_argument('--got_forms', type=str,
                        default='koeblergothic/cldf/forms.csv',
                        help='Path to the Gothic forms table.')
    parser.add_argument('--got_senses', type=str,
                        default='koeblergothic/cldf/senses.csv',
                        help='Path to the Gothic senses table.')
    args = parser.parse_args()

    # read Hungarian and Gothic input files, explicit better than implicit
    with open(args.hungarian, "r") as f:
        dfhun = list(csv.reader(f, delimiter="\t"))
    with open(args.hun_entries, "r") as f:
        dfhun_entries = list(csv.reader(f))
    with open(args.hun_senses, "r") as f:
        dfhun_senses = list(csv.reader(f))
    shutil.copy(args.gothic, "GothicHungarian/raw/gothic.csv")
    with open(args.got_forms, "r") as f:
        dfgot_forms = list(csv.reader(f))
    with open(args.got_senses, "r") as f:
        dfgot_senses = list(csv.reader(f))

    # create dict that has entryIDs as keys and reconstr.-regex as vals
    entry_id = [row[0] for row in dfhun_entries]
    rc100 = [row[8] for row in dfhun_entries]
    entryid2rc100 = dict(zip(entry_id, rc100))

    # create dict that converts formID to parameterID
    forms_ID = [row[1] for row in dfgot_forms]
    para_ID = [row[3] for row in dfgot_forms]
    form2paraID = dict(zip(forms_ID, para_ID))

    # create json-dictionary to translate Hungarian IDs to a list of senses
    hunsensedict = collections.defaultdict(list)
    for row in dfhun:
        for srow in dfhun_senses:
            if srow[2] == row[1] and srow[3]:  # IDs match and spacy != ""
                hunsensedict[row[1]].append(srow[3])  # spacy

    # create json-dictionary to translate Gothic IDs to a list of senses
    gotsensedict = collections.defaultdict(list)
    for i, row in enumerate(dfgot_forms[1:]):
        for srow in dfgot_senses[1:]:
            if srow[4] == form2paraID[row[1]] and srow[3]:  # not ""
                gotsensedict[row[1]].append(srow[3])  # spacy

    # Write Gothic and Hungarian senses dictionary to json-file
    with open("GothicHungarian/raw/senses.json", "w+") as f:
        json.dump({"got": gotsensedict, "hun": hunsensedict}, f)

    # add the relevant columns to new df and write rows
    with open("GothicHungarian/raw/hungarian.tsv", "w+") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["ID", "EntryID", "rc100"])
        for row in dfhun[1:]:
            if "not old" not in entryid2rc100[row[1]]:  # skip bad rows
                writer.writerow([f"{row[1]}-1", row[1], entryid2rc100[row[1]]])

if __name__ == "__main__":
    main()
