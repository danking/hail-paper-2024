select locus, ref_allele, alt_allele,
       avg(n_alt_alleles) as af
from mt
group by locus, ref_allele, alt_allele
