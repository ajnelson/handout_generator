# Handout generator

This script package generates a PDF with slightly varying numbers, given a roster.

The roster format is a tab-separated values ("TSV") file.  The first field is the student's name, which can be a full name including whitespace.  The second field onward are the values to substitute in a templated Latex file.

The Latex template file (e.g. `template.tex.in` in this directory) should be normal Latex, except every value to be substituted should be the string `%VALUEn%` (e.g. `%VALUE0%`, `%VALUE1%`).  A temporary `.tex` file will be generated, and a PDF will be generated from that `.tex` file.


## License

[BSD 2-clause](https://opensource.org/licenses/BSD-2-Clause).


## Setup

Expected environment:  macOS or Linux, Python (either version 2 or 3) installed, and command-line Latex available.  It may work in Windows, but has not been tested.

`make` is only necessary if you want to run the demo below.


## Usage

Example call:

    python populate_from_tsv.py template.tex.in students.tsv

To see everything in action, you can run `make`.  You may need to supply a path to a Python executable, e.g. `make PYTHON=/opt/local/bin/python3.5`.  Either Python 2 or 3 should work.

If you'd like to run things with debugging enabled, add `DEBUG_FLAG=--debug` to your `make` call.
