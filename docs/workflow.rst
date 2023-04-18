Step one: Download and install this repository
==============================================

Clone this repository by running

.. code-block:: sh

   git clone https://github.com/LoanpyDataHub/GothicHungarian.git

from your shell. Next, from the same directory, run:

.. code-block:: sh

   pip install -e GothicHungarian

This will install a command-line interface for running the analyses.

Step two: Load the relevant data in the right format
====================================================

From your command-line, simply run

.. code-block:: sh

   loadinput

Here's what happened under the hood:

.. automodule:: gothuncommands.loadinput
   :members:
