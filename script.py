import gene_symbol_row_numbers.script

def main():
  # Load files
  d = gene_symbol_row_numbers.script.run(gpl_brief=None, gpl_data=gpl_data, study_data=study_data, varlist_fname=varlist_fname, percentile=percentile)
  idxs, gpl, M, varlist = d['idxs'], d['gpl'], d['M'], d['varlist']
  
