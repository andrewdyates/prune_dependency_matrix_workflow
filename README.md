prune_dependency_matrix_workflow
================================
Select all rows in a gene expression matrix that:
  1) have unique gene symbols with the highest mean expression
  2) are in the PINA protein network gene list at http://cbg.garvan.unsw.edu.au/pina/interactome.stat.do

##Example Use##
    export STUDY_DIR=$HOME/Dropbox/biostat/study_data/GSE7307
    python script.py outdir=$HOME/Desktop gpl_brief=$STUDY_DIR/GSE7307_GPL570.gpl_brief.txt gpl_data=$STUDY_DIR/GSE7307_GPL570.probes.tab study_data=$STUDY_DIR/GSE7307_GPL570.normed.masked.pkl varlist_fname=$STUDY_DIR/GSE7307_GPL570.varlist.txt percentile=0.25 pina_zip=Homo_sapiens-20110628.txt.zip

note: keep submodules up to date using
    git submodule update --init --recursive