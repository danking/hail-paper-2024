mt.annotate_variants(
  af = hl.agg.group_by(
    mt.sample_group,
    hl.agg.call_stats(mt.GT, mt.alleles)))
