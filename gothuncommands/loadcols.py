"""
Merge IDs in ``out/semantic_matches.tsv`` with relevant columns for manual
inspection. 
"""
import csv
import json

def main():
    """
    #. Read the semantic matches file
    #. Read the related tables
    #. Stitch the desired columns together
    #. Overwrite the input file

    """
    # read semantic matches, assign to variable
    with open("out/semantic_matches.tsv", "r") as f:
        dfsem = list(csv.reader(f, delimiter="\t"))

    # read related tables and json
    with open("../gerstnerhungarian/cldf/entries.csv", "r") as f:
        dfhun_entries = list(csv.reader(f))
    with open("../koeblergothic/cldf/forms.csv", "r") as f:
        dfgot_forms = list(csv.reader(f))
    with open("raw/senses.json", "r") as f:
        senses = json.load(f)

    # store info from hungarian entries.csv cols Headword, Etymology 2 dicts
    headwords = [row[2] for row in dfhun_entries[1:]]
    hsegments = [row[4] for row in dfhun_entries[1:]]
    etymologies = [row[6] for row in dfhun_entries[1:]]
    entryIDs = [row[0] for row in dfhun_entries[1:]]
    entryid2headword = dict(zip(entryIDs, headwords))
    entryid2etymology = dict(zip(entryIDs, etymologies))
    entryid2segments = dict(zip(entryIDs, hsegments))

    # store gothic info from forms.csv Form, adapts.csv ad100 2 dicts
    f_ids = [row[1] for row in dfgot_forms]
    forms = [row[5] for row in dfgot_forms]
    segments = [row[6] for row in dfgot_forms]
    f_id2form = dict(zip(f_ids, forms))
    f_id2segments = dict(zip(f_ids, segments))

    # add info from dicts to table
    with open("out/semantic_matches.tsv", "w+") as f:
        writer = csv.writer(f, delimiter="\t")
        #write header
        #newcols = ["hun", "got", "Segments", "Etymology", "sense_got", "sense_hun"]
        #writer.writerow(dfsem[0] + newcols)
        writer.writerow([
        "ID", "ID_s", "ID_rc", "ID_ad", "semsim", "Language_ID", "Segments",
        "Form", "Sense", "Etymology"
        ])
        # loop through table
        i = 0
        for row in dfsem[1:]:
            writer.writerow([f"s{i}", row[0], row[1], "", row[3], "Hungarian",
            entryid2segments[row[1]], entryid2headword[row[1]],
            ", ".join(senses["hun"][row[1]]), entryid2etymology[row[1]]
            ])
            i += 1
            writer.writerow([f"s{i}", row[0], "", row[2], row[3], "Gothic",
            f_id2segments[row[2]], f_id2form[row[2]],
            ", ".join(senses["got"][row[2]]), ""
            ])
            i += 1

if __name__ == "__main__":
    main()
