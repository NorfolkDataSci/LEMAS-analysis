import re
import pandas as pd
        
digits = re.compile('\%([0-9]?[0-9])')
col_name = re.compile('"(.*?)"')

with open('/users/josiah.baker/downloads/ICPSR_03079 3/DS0001/03079-0001-Setup.dct') as data:
    col_width = [int(digits.findall(line)[0]) for line in data.readlines() if digits.findall(line)]
    name = re.compile('"(.*?)"')
    data.seek(0)
    col_names = [name.findall(line)[0] for line in data.readlines() if digits.findall(line)]
    
df = pd.read_fwf('/users/josiah.baker/downloads/ICPSR_03079 3/DS0001/03079-0001-Data.txt', widths=col_width, header=None, names=col_names)

print df.head()