n_alleles = hl.len(mt.alleles)
mt.annotate_variants(
  af = hl.range(n_alleles).map(
    lambda i: hl.agg.group_by(
      mt.sample_group,
      hl.agg.mean(mt.GT.one_hot_alleles()[i]))))





