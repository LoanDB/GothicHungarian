Create results
~~~~~~~~~~~~~~

Step 1: Download and install this repository
==============================================

Create and activate a virtual environment and clone this repository
(11.38 MB) by running

.. code-block:: sh

   python3 -m venv venv && source venv/bin/activate
   git clone https://github.com/LoanpyDataHub/GothicHungarian.git

Next, clone the two repositories containing Hungarian and Gothic
language data (10.65 MB + 8.75 MB):

.. code-block:: sh

   git clone https://github.com/LoanpyDataHub/gerstnerhungarian
   git clone https://github.com/LoanpyDataHub/koeblergothic

Next, from the same directory, run:

.. code-block:: sh

   pip install -e GothicHungarian

This will install a command-line interface for running the analysis.
It will also install two dependencies, namely `loanpy
<https://pypi.org/project/loanpy/>`_ and
`Spacy <https://pypi.org/project/spacy/>`_, for which we need to install
a pretrained German word-vector model. You can find different
models on the `Spacy website <https://spacy.io/models/de/>`_. Currently
this 500 MB model seems to be the most suiting (But make sure to use the same
model as in `gerstnerhungarian
<https://github.com/LoanpyDataHub/gerstnerhungarian>`__
and `koeblergothic <https://github.com/LoanpyDataHub/koeblergothic>`__
because entries in those repositories were filtered out if they were missing
from this particular word-vector model):

.. code-block:: sh

   python3 -m spacy download de_core_news_lg

To deactivate the virtual environment run:

.. code-block:: sh

   deactivate

and to remove it run:

.. code-block:: sh

   rm -r venv

Step 2: Load the relevant data in the right format
====================================================

From your command-line, run

.. code-block:: sh

   loadinput

.. automodule:: gothuncommands.loadinput
   :members:

Step 3: Search for phonetic matches
=======================================

From your command-line, run

.. code-block:: sh

   phonmatch

.. automodule:: gothuncommands.phonmatch
   :members:

Step 4: Search for semantic matches
======================================

From your command-line, run

.. code-block:: sh

   semmatch

.. automodule:: gothuncommands.semmatch
   :members:

Step 5: Load columns for manual inspection
=============================================

From your command-line, run

.. code-block:: sh

   loadcols

.. automodule:: gothuncommands.loadcols
   :members:

Step 6: Manually inspect the results
====================================

Open the file in a spread-sheet software, sort the rows according to
semantic similarity (column ``semsim``) and within that according to
cognate ID (column ``ID_s``). Carefully look at the matches:
Pick candidate loanwords where the phonetic matching and the semantic shift
looks plausible.
