# Methods

Augment embedding with MSA based embedding from [[Evolutionary_Context_Deep_Sequence_Modeling_Peng.pdf | Luo et al]] #proteins #function 

## Generate Single Sequence MSA

Params from ComplexContact:
    - Num Iterations: 8
    - E-value cutoff: 1e-20
    - maxfilt 100000000
    - diff inf -all
    - neffmax 20
    
ComplexContact uses Uniprot20 HMM, Feb 2016
CURRENTLY I can find UniClust30

`hhblits -cpu [num-cpu] -i [input fasta] -d [uniprot db] -oa3m [output MSA] -n 8 -e 1e-20 -maxfilt 100000000 -dif inf -all -neffmax 20`

## Align MSA / Create Paired MSA

- Simpler way to do it: how does EVcomplex pair MSAs

We are largely looking at **eukaryotes**, so we want to do **phylogeny concatenation**

Use [NCBI Taxonomy Database](https://www.ncbi.nlm.nih.gov/taxonomy)

## Create Contact Map using {...}
- [[Complex Contact Xu]]
- [EVcoupling](https://github.com/debbiemarkslab/EVcouplings), [EVcomplex](https://elifesciences.org/articles/03430)
- **[[Gremlin-Complex Baker]]**

## Pool Contact Map with {...}
- 