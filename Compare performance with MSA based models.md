# Methods

Augment embedding with MSA based embedding from [[Evolutionary_Context_Deep_Sequence_Modeling_Peng.pdf | Luo et al]] #proteins #function 

## Generate Single Sequence MSA
Jackhmmr for MSA searching
![[Jackhmmr directions.png]]

## Align MSA / Create Paired MSA
- Pair MSAs using [EVcomplex](https://github.com/debbiemarkslab/EVcouplings) library ([Documentation](https://evcouplings.readthedocs.io/en/latest/evcouplings.complex.html#module-evcouplings.complex.protocol))

## Create Contact Map
- [EVcoupling](https://evcouplings.readthedocs.io/en/latest/evcouplings.couplings.html)
- [[Gremlin-Complex Baker]]

## Pool Contact Map
- Our end step pooling layers of D-SCRIPT

EVcomplex test link -- https://v1.evcouplings.org/jobs/f1420894618de74e30921601172082dc