# Extracting Dollars from a String
import re

## Data
report = '''
If you invested $1 in the year 1801, you would have $18087791.41 today.
This is a 7.967% return on investment.
But if you invested only $0.25 in 1801, you would end up with $4521947.8525.
'''

## One-Liner
dollars = [x[0] for x in re.findall('(\$[0-9]+(\.[0-9]*)?)', report)]

## Result
print(dollars)

