create model `result`
options ( model_type='LINEAR_REG' ) as
select
  sum(mt.n_alt_alleles) as n_plof,
  mt.phenotype as label
from mt
left join interval_table
on interval_table.left_endpoint >= mt.locus
and mt.locus <= interval_table.right_endpoint
where mt.predicted_lof
group by interval_table.left_endpoint,
         interval_table.right_endpoint

select *
from ml.advanced_weights(
  model `result`, struct(false as standardize))
