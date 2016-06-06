#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Alex Nelson"

import os
import logging
import subprocess

_logger = logging.getLogger(os.path.basename(__file__))

import populate

def main():
    with open(args.input_tsv, "r") as in_fh:
        expected_value_count = None
        for (line_no, line) in enumerate(in_fh):
            cleaned_line = line.strip()
            if cleaned_line == "":
                continue

            line_parts = cleaned_line.split("\t")
            #Read name
            student_name = line_parts[0]

            #Read values, skipping blank fields (so two tabs act as one delimiter)
            values_list = [ part for part in line_parts[1:] if not part is None ]
            if expected_value_count is None:
                expected_value_count = len(values_list)
            if len(values_list) != expected_value_count:
                info_tuple = (
                  line_no,
                  student_name,
                  len(values_list),
                  expected_value_count
                )
                raise ValueError("Error in line %d (student %s): Found %d values, expected %d." % info_tuple)

            #Populate from template
            _logger.debug("Generating Latex file for %s." % student_name)
            populate.replace_values(args.input_template_tex_in, student_name + ".tex", student_name, values_list)

            #Generate PDF from tex file
            _logger.debug("Generating PDF for %s." % student_name)
            subprocess.check_call(["pdflatex", student_name])
            subprocess.check_call(["pdflatex", student_name])
            subprocess.check_call(["pdflatex", student_name])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("input_template_tex_in")
    parser.add_argument("input_tsv", help="Tab-separated values file.  First field is student's name, the rest are values to be substituted for %VALUEn%, where n is 0-indexed.")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    main()
