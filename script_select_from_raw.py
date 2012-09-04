#!/usr/bin/python
"""
EXAMPLE USE
python $HOME/prune_dependency_matrix_workflow/script_select_from_raw.py fname_rownums=$HOME/gse7307/GSE7307_GPL570.symbol_rownums.gt0.25.pina.txt fname_rawtab=$HOME/gse7307/GSE7307.raw.tab > $HOME/gse7307/GSE7307_GPL570.raw.gt0.25.pina.tab

"""
import sys

FNAME_ROWNUMS = "/Users/z/Dropbox/biostat/study_data/GSE7307/GSE7307_GPL570.symbol_rownums.gt0.25.pina.txt"
FNAME_RAWTAB = "/Users/z/Dropbox/biostat/study_data/GSE7307/GSE7307_GPL570.raw.tab"

def main(fname_rownums=FNAME_ROWNUMS, fname_rawtab=FNAME_RAWTAB):
  rownums = set([int(line.split('\t')[0]) for line in open(fname_rownums) if line.strip()])
  row_ids = [line.split('\t')[1] for line in open(fname_rownums) if line.strip()]

  fp = open(fname_rawtab)
  n_lines = 0
  print fp.next().strip('\n')
  for i, line in enumerate(fp):
    if i in rownums:
      print line.rstrip('\n')
      s = line.split('\t')[0]
      assert row_ids[n_lines] == s, "%s != %s @ %d" % (row_ids[i], s, i)
      n_lines += 1

if __name__ == "__main__":
  main(**dict([s.split('=') for s in sys.argv[1:]]))
    
