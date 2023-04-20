"""
Read the phonetic matches file in folder ``out`` and search for
semantic matches among them. Write results as ``semantic_matches.tsv``
to folder ``out``.
"""
import csv
import json

from loanpy.loanfinder import semantic_matches
import spacy

# install first with $ python -m spacy download de_core_news_lg
nlp = spacy.load('de_core_news_lg')

def semsim(meaning1, meaning2):
    """
    #. Convert each meaning to a Spacy-object
    #. Create cartesian product of both meaning lists with a
       nested for-loop
    #. Return the similarity of the most similar pair
    """
    meaning1 = [nlp(m) for m in meaning1]
    meaning2 = [nlp(m) for m in meaning2]
    bestsim = 0
    for sense1 in meaning1:
        for sense2 in meaning2:
            sim = sense1.similarity(sense2)
            if sim > bestsim:
                bestsim = sim
    return bestsim

def main():
    """
    #. Import loanpy.loanfinder.semantic_matches
       <https://loanpy.readthedocs.io/en/latest/documentation.html#loanpy.loanfinder.semantic_matches>`_
    #. Read phonetic matches file with csv library
    #. Read related tables that contain the meanings
    #. Grab meanings from related tables and create new input table
    #. Input the table to the loanfinder module's semantic_matches function
    #. End the function since loanpy writes the file

    """
    # read phonetic matches table
    with open("GothicHungarian/out/phonetic_matches.tsv", "r") as f:
        df_phonmatch = list(csv.reader(f, delimiter="\t"))

    # read json that contains the meanings
    with open("GothicHungarian/raw/senses.json", "r") as f:
        id2senses = json.load(f)

    # replace ID with list of senses
    df_sem_in = [df_phonmatch[0] + ["Hungarian", "Gothic"]]
    for i, row in enumerate(df_phonmatch[1:]):
        try:
            row += [id2senses["hun"][row[1]], id2senses["got"][row[2]]]
            df_sem_in.append(row)
        except KeyError:
            pass
    # find semantic matches
    semantic_matches(df_sem_in, semsim, "GothicHungarian/out/semantic_matches.tsv", 0)

if __name__ == "__main__":
    main()
