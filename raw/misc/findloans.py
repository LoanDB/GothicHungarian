"""cd to folder `misc` and run `findloans.py` from terminal"""

from pathlib import Path

from gensim.models import KeyedVectors

from loanpy.helpers import plug_in_model
from loanpy.loanfinder import Search

def main():
    """Creates loans.csv with potential Gothic loanwords in Hungarian."""

    folder_raw = Path(__file__).parent.parent
    #define 5 input paths
    path2got = folder_raw / "adapt.csv"
    path2hun = folder_raw / "reconstruct.csv"
    path2sc = folder_raw / "sc_H2EAH.txt"  # for likeliestphonmatch
    path2substi = folder_raw / "substi_WOT2EAH.txt"  # for likeliestphonmatch
    path2vectors = folder_raw / "german.model"
    #define output path
    out_path = folder_raw / "loans.csv"

    #create instance of loanpy.loanfinder.Search
    search_obj = Search(
    path2donordf=path2got, path2recipdf=path2hun,
    semsim=0, scdictlist_ad=path2substi, scdictlist_rc=path2sc)

    # plug in German vectors manually, since default is English
    plug_in_model(KeyedVectors.load_word2vec_format(path2vectors, binary=True))

    # search for loans
    search_obj.loans(write_to=out_path)

if __name__ == "__main__":
    main()
