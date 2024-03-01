select locus, ref_allele, alt_allele,
       sample_group, avg(n_alt_alleles) as af
from mt
group by locus, ref_allele, alt_allele, sample_group
