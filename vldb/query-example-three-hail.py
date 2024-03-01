mt = mt.filter_rows(mt.predicted_lof)
mt = mt.annotate_rows(
  interval = interval_table.index(
    mt.locus, all_matches=True))
mt = mt.explode_rows(mt.interval)
mt = mt.group_rows_by(
  mt.interval
).aggregate(
  n_plof = hl.agg.sum(mt.GT.n_alt_alleles()))
mt = mt.annotate_rows(
  result=hl.agg.linreg(y=mt.phenotype, x=[1.0, mt.n_plof]))
