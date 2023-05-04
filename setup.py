from setuptools import setup, find_packages

setup(
    name="GothicHungarian",
    version="1.0",
    packages=find_packages(),
    install_requires = ["spacy>=3.5.2", "loanpy==3.0.0"],
    entry_points={
        "console_scripts": [
            "loadinput = gothuncommands.loadinput:main",
            "phonmatch = gothuncommands.phonmatch:main",
            "semmatch = gothuncommands.semmatch:main",
            "loadcols = gothuncommands.loadcols:main"
        ],
    }
)
