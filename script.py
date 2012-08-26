#!/usr/bin/python
"""Filter a matrix by variance percentile, unique gene symbol, and enrichment list inclusion.

EXAMPLE USE:
  export STUDY_DIR=$HOME/Dropbox/biostat/study_data/GSE7307
  python script.py outdir=$HOME/Desktop gpl_brief=$STUDY_DIR/GSE7307_GPL570.gpl_brief.txt gpl_data=$STUDY_DIR/GSE7307_GPL570.probes.tab study_data=$STUDY_DIR/GSE7307_GPL570.normed.masked.pkl varlist_fname=$STUDY_DIR/GSE7307_GPL570.varlist.txt percentile=0.25 pina_zip=Homo_sapiens-20110628.txt.zip
"""
from gene_symbol_row_numbers.script import *
from gene_enrichment import *
from lab_util import masked_npy_to_tab
import cPickle as pickle
import sys, os
import zipfile
from gene_enrichment.pina import *

def main(pina_zip=None, outdir=None, gpl_brief=None, gpl_data=None, study_data=None, varlist_fname=None, percentile=0.25):
  # Load files
  assert outdir and gpl_brief and gpl_data and study_data and pina_zip
  percentile = float(percentile)
  assert percentile >= 0
  if not os.path.exists(outdir):
    print "Creating output directory %s..." % (outdir)
    make_dir(outdir)
  d = run(gpl_brief=gpl_brief, gpl_data=gpl_data, study_data=study_data, varlist_fname=varlist_fname, percentile=percentile)

  # Load enrichment from single-file .zip archive
  print "Loading PINA interaction file from zip archive %s." % (pina_zip)
  zfp = zipfile.ZipFile(pina_zip, "r")
  P = PINAEnriched(zfp.open(zfp.namelist()[0]))
  print "Loaded %d interactions between %d unique genes" % (P.n_pairs, len(P.vars))
  # Filter by symbols in enrichment list
  idxs = []
  for v, i in d['d_symbols'].items():
    if P.is_in(v):
      idxs.append(i)
  idxs.sort()
  print "Selected %d variables in PINA gene list." % len(idxs)

  # Assert that selected rows are all in PINA list and are all unique.
  print "Asserting that all row numbers correspond to unique gene symbols in PINA list."
  sym_set = set()
  for i in idxs:
    s = d['gpl'].get_column(d['varlist'][i], 'GENE_SYMBOL')
    assert P.is_in(s)
    assert s not in sym_set
    sym_set.add(s)

  # Output index results.
  study_id = os.path.basename(gpl_data).partition('.')[0]
  out_idx_fname = os.path.join(outdir, "%s.symbol_rownums.gt%.2f.pina.txt" % (study_id, percentile))
  print "Saving sorted idx list in line format '[row_num]\\t[probe ID]\\t[gene symbol]\\n' to %s" \
      % (out_idx_fname)
  fp = open(out_idx_fname, "w")
  for i in idxs:
    fp.write("%d\t%s\t%s\n" % (i, d['varlist'][i], d['gpl'].get_column(d['varlist'][i], 'GENE_SYMBOL')))
  fp.close()

  # Save data array copy of only selected rows.
  out_M_fname = os.path.join(outdir, "%s.gt%.2f.pina.tab" % (os.path.basename(study_data), percentile))
  print "Saving %d selected rows of data matrix as .tab format as %s" % (len(idxs), out_M_fname)
  masked_npy_to_tab.npy_to_tab( \
    d['M'][idxs, :], open(out_M_fname, 'w'), varlist=[d['varlist'][i] for i in idxs])

  

  
if __name__ == "__main__":
  print sys.argv
  main(**dict([s.split('=') for s in sys.argv[1:]]))
