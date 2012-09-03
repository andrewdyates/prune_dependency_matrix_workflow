#!/usr/bin/python
"""
EXAMPLE USE
python $HOME/prune_dependency_matrix_workflow/script_select_from_raw.py fname_rownums=$HOME/gse7307/GSE7307_GPL570.symbol_rownums.gt0.25.pina.txt fname_rawtab=gse7307/GSE7307_GPL570.raw.tab > GSE7307_GPL570.raw.symbol_rownums.gt0.25.pina.txt

"""
import sys

FNAME_ROWNUMS = "/Users/z/Dropbox/biostat/study_data/GSE7307/GSE7307_GPL570.symbol_rownums.gt0.25.pina.txt"
FNAME_RAWTAB = "/Users/z/Dropbox/biostat/study_data/GSE7307/GSE7307_GPL570.raw.tab"

def main(fname_rownums=FNAME_ROWNUMS, fname_rawtab=FNAME_RAWTAB):
  rownums = set([int(line.split('\t')[0]) for line in open(fname_rownums) if line.strip()])
  for i, line in enumerate(open(fname_rawtab)):
    if i in rownums:
      print line.rstrip('\n')

if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
    
