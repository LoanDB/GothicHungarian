"""cd to folder `misc` and run `python makescH_EAH.py` from terminal"""

from pathlib import Path
from loanpy import loanfinder, helpers
from cldfbench import Dataset as BaseDataset
import gensim

def main():
    """creates soundchanges.txt for horizontal or vertical transfers"""

    in_path1 = Path.cwd().parent / "got.csv"
    in_path2 = Path.cwd().parent / "hun.csv"
    in_path3 = Path.cwd().parent / "soundchanges.txt"
    in_path4 = Path.cwd().parent / "substis.txt"
    in_path5 = Path.cwd().parent / "german.model"

    out_path = Path.cwd().parent / "loans.csv"

    #run qfysc module from loanpy
    Dfgothun = loanfinder.Semantix(in_path2, "rc", in_path1, "ad", distance=0,
                                   soundchanges=in_path3, substis=in_path4)
    helpers.model = gensim.models.KeyedVectors.load_word2vec_format(in_path5, binary=True)
    Dfgothun.findloans(write=True, outputname=out_path, statistics=False, likeliest_phonmatch=False,
                       floor_semsim=0, addinfo=False)

if __name__ == "__main__":
    main()
