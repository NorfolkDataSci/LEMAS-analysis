"""
    Author: Josiah Baker
    Org: Norfolk Data Science

    Simple script for reading a ASCII.txt file with a STATA .dct file into a CSV
    To use: 
        
        python STAT_file_parse.py <asciifile> <setupfile>
"""

import re
import pandas as pd
from sys import argv

digits = re.compile('\%([0-9]?[0-9])')
col_name = re.compile('"(.*?)"')

def main(txtfile, setupfile):
    try:
        digits = re.compile('\%([0-9]?[0-9])')
        name = re.compile('"(.*?)"')
        with open(setupfile) as data:
            col_width = [int(digits.findall(line)[0]) for line in data.readlines() if digits.findall(line)]
            data.seek(0)
            col_names = [name.findall(line)[0] for line in data.readlines() if digits.findall(line)]
            df = pd.read_fwf(txtfile, widths=col_width, header=None, names=col_names)
            df.to_csv(txtfile.split('.')[0] + '_with_headers.csv', index=False)
    except:
        print "There was a problem parsing " + argv[1] 

if __name__ == "__main__":
    main(argv[1], argv[2])
