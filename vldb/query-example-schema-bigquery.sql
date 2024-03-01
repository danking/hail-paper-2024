create table mydataset.mt (
  locus: int64,
  ref_allele: string,
  alt_allele: string,
  sample_id: string,
  sample_group: int64,
  n_alt_alleles: int64,
  primary key (locus, ref_allele, alt_allele)
)
cluster by locus, ref_allele, alt_allele
