#!/usr/bin/env python

__version__ = "0.1.0"
__author__ = "Alex Nelson"

import os
import logging

_logger = logging.getLogger(os.path.basename(__file__))

def replace_values(template_file_name, output_file_name, student_name, values_list):
    #Prepare argument.
    if student_name is None:
        student_name_str = ""
    else:
        student_name_str = student_name

    with open(output_file_name, "w") as out_fh:
        with open(template_file_name, "r") as in_fh:
            contents = in_fh.read()

            contents = contents.replace("%NAME%", student_name_str)

            for (value_no, value) in enumerate(values_list):
                contents = contents.replace("%%VALUE%d%%" % value_no, str(value))
            out_fh.write(contents)

#The main() method is really for unit-testing.
def main():
    replace_values(args.input_template_tex_in, args.output_tex, None, args.value)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("input_template_tex_in")
    parser.add_argument("output_tex")
    parser.add_argument("value", nargs="+")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    main()
