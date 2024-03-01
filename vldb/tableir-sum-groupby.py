t1.group_by(t1.b) \
  .aggregate(a=hl.agg.sum(t1.a))
