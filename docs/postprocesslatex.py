"""

#. Replace badges with plain links
#. Replace greek char Delta with correct encoding

"""

ENCODINGS = {
"∆": r"\(\Delta \)"
}

REPLACEBADGES = {  # plain links, no badges

r"\sphinxhref{https://creativecommons.org/licenses/by/4.0/}" +
r"{\sphinxincludegraphics{{/home/viktor/Documents/GitHub/" +
r"gerstnerhungarian/docs/doctrees/images/" +
r"554312bbffabcb804cf4f8c50b1b75a140d3bd2b/by}.svg}}":

r"License: CC BY 4.0\\\\" + "\n",

r"\sphinxhref{https://dl.circleci.com/status-badge/redirect/gh/" +
r"LoanpyDataHub/gerstnerhungarian/tree/main}{\sphinxincludegraphics" +
r"{{/home/viktor/Documents/GitHub/gerstnerhungarian/docs/doctrees/" +
r"images/5221f732c98234d1f31dd595c54f19217d01ec6a/main}.svg}}":

r"Continuous integration: " +
r"https://dl.circleci.com/status-badge/redirect/gh/" +
r"LoanpyDataHub/gerstnerhungarian/tree/main\\\\"  + "\n",

r"\sphinxhref{https://gerstnerhungarian.readthedocs.io/en/latest/" +
r"?badge=latest}{\sphinxincludegraphics{{/home/viktor/Documents/GitHub/" +
r"gerstnerhungarian/docs/doctrees/images/" +
r"941b25609704529107ac2a098aef56238d782e60/" +
r"04afe4fcf94364fa02d681ebc3ad2f4dd1402430}.svg}}":

r"Documentation: https://gerstnerhungarian.readthedocs.io/en/latest/\\\\" +
"\n",

r"\sphinxhref{https://github.com/martino-vic/gerstnerhungarian/" +
r"actions?query=workflow\%3ACLDF-validation}{\sphinxincludegraphics" +
r"{{/home/viktor/Documents/GitHub/gerstnerhungarian/docs/doctrees/" +
r"images/4a378d74fa8541e029a8e727f0722e6159b8f949/badge}.svg}}":

r"CLDF validation: " +
r"https://github.com/martino-vic/gerstnerhungarian/" +
r"actions?query=workflow\%3ACLDF-validation\\\\" +
"\n",

r"\sphinxincludegraphics{{/home/viktor/Documents/GitHub/" +
r"gerstnerhungarian/docs/doctrees/images/" +
r"d44641bc24451db56ba1c2f56d656871246a1945" +
r"/Glottolog-100%25-brightgreen}.svg}":

r"Glottolog: 100\%\\\\" + "\n",

r"\sphinxincludegraphics{{/home/viktor/Documents/GitHub/" +
r"gerstnerhungarian/docs/doctrees/images/" +
r"76c362aa69c478e0e38fe53aa1207f4c4e0247c2/3984c76090ee859c11f6da2984a8848fac1f0c3e.svg}":

r"Concepticon: 100\%\\\\" + "\n",

r"\sphinxincludegraphics{{/home/viktor/Documents/GitHub/" +
r"gerstnerhungarian/docs/doctrees/images/" +
r"8610b4fe2e7a97bed23df74a39cd30feda0b8612/Source-100%25-brightgreen}.svg}":

r"Source: 100\%\\\\",

r"\sphinxincludegraphics{{/home/viktor/Documents/GitHub/" +
r"gerstnerhungarian/docs/doctrees/images/" +
r"54c8ae34ac3ec41286b604aef9bcbad15a74f3de/BIPA-100%25-brightgreen}.svg}":

r"BIPA: 100\%\\\\" + "\n",

r"\sphinxincludegraphics{{/home/viktor/Documents/GitHub/" +
r"gerstnerhungarian/docs/doctrees/images/" +
r"64600fa1cdb6b54d89ce1e5ebac95262ca62a8fc/" +
r"b8fdf0ffe8e33ddbdc635aa3b469289f77c84efb}.svg}":

r"CLTS SoundClass: 100\%\\\\" + "\n",

r"\sphinxincludegraphics{{/home/viktor/Documents/GitHub/gerstnerhungarian/" +
r"docs/doctrees/images/" +
r"76c362aa69c478e0e38fe53aa1207f4c4e0247c2/3984c76090ee859c11f6da2984a8848fac1f0c3e}" +
".svg}":

r"Vector coverage: 88\%\\\\" + "\n",

r" \sphinxincludegraphics{{/home/viktor/Documents/GitHub/gerstnerhungarian/docs/doctrees/images/be037cb372fe82ccb3e3ab6c2ab1eb62ef77e6b0/7690bf4d2ca2c181b71fba959ee8e1f1f318b06e}.svg} \sphinxhref{https://pypi.org/project/spacy/}{\sphinxincludegraphics{{/home/viktor/Documents/GitHub/gerstnerhungarian/docs/doctrees/images/2d081927145272de8a9ed568341618987dcea5d3/SpaCy-v3.5}.1-blue}}":

r"SpaCy: v3.5.1\\\\" + "\n"

}

def process_tex_file(input_filename, output_filename):
    """
    #. Read the file from specified path
    #. Apply changes from dictionaries defined on top
    #. Write file to specified path

    """
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    for dictionary in [ENCODINGS, REPLACEBADGES]:
        for key in dictionary:
            content = content.replace(key, dictionary[key])

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(content)


if __name__ == "__main__":
    process_tex_file(
        'docs/latex/gerstnerhungarian.tex',
        'docs/latex/gerstnerhungarian2.tex'
        )
