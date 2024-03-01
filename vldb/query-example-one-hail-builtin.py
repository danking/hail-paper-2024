mt.annotate_variants(
  af = hl.agg.call_stats(mt.GT, mt.alleles).AF)
