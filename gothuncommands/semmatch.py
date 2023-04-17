"""
Read the phonetic matches file and search for semantic matches
between Gothic and Hungarian
"""
import csv
import json

from loanpy.loanfinder import semantic_matches
import spacy

nlp = spacy.load('de_core_news_lg')

def semsim(meaning1, meaning2):
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
    #. Read phonetic matches file with csv library
    #. Read related tables that contain the meanings
    #. Grab meanings from related tables and create new input table
    #. Input the table to the loanfinder module's semantic_matches function
    #. End the function since loanpy writes the file

    """
    # read phonetic matches table
    with open("out/phonetic_matches.tsv", "r") as f:
        df_phm = list(csv.reader(f, delimiter="\t"))

    # read json that contains the meanings
    with open("raw/senses.json", "r") as f:
        d = json.load(f)

    # replace ID with list of senses
    dfin = [[row[0], d["hun"][row[1]], d["got"][row[2]]] for row in df_phm[1:]]
    dfin.insert(0, df_phm[0])
    df_phm[0].append("semsim")
    # find semantic matches
    sem = semantic_matches(dfin, semsim, 0)

    for row, sem in zip(df_phm[1:], sem):
        row.append(sem)

    with open("out/semantic_matches.tsv", "w+") as f:
        writer = csv.writer(f)
        writer.writerows(df_phm)

if __name__ == "__main__":
    main()
