"""
Read the prepared input files in folder ``raw`` and search for phonetic
matches between Gothic and Hungarian. Write result as ``phonetic_matches.tsv``
to folder ``out``.
"""
import csv

from loanpy.loanfinder import phonetic_matches

def main():
    """
    #. Import `loanpy.loanfinder.phonetic_matches
       <https://loanpy.readthedocs.io/en/latest/documentation.html#loanpy.loanfinder.phonetic_matches>`_
    #. Read the input data
    #. Pass it on to loanpy
    #. End the function since loanpy writes the file

    """
    with open("GothicHungarian/raw/hungarian.tsv", "r") as f:
        hun = list(csv.reader(f, delimiter="\t"))
    with open("GothicHungarian/raw/gothic.csv", "r") as f:
        got = list(csv.reader(f))

    phonetic_matches(hun, got, "GothicHungarian/out/phonetic_matches.tsv", 10)

if __name__ == "__main__":
    main()
