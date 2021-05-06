# RemoveRow
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: SHARED (Mothur)
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes a Mothur .shared file and removes a specific row
from the file.

The plugin takes as input a tab-delimited parameter file of keyword-value pairs:
inputfile: Mothur shared file
row: Row number

The plugin will then output the same SHARED file, but with the corresponding row removed.

