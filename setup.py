from setuptools import setup, find_packages

setup(
    name="GothicHungarian",
    version="1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "loaddata = gothuncommands.loaddata:main",
            "phonmatch = gothuncommands.phonmatch:main",
            "semmatch = gothuncommands.semmatch:main"
        ],
    }
)
