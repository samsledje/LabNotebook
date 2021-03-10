## [[Research Tasks#Phylogenetic Genome Assembly | Tasks]]

## Scratch Notes
- Identify essential, conserved genes (say, mitochondrial)
- Use evolutionary information to collapse "bubbles" in the assembly graph

## Base Idea
> I think a pretty compelling problem in genome assembly is solving the assembly problem simultaneously across a set of related genomes. My intuition is that one would start with some sense of the phylogenetic relationships (or evolutionary distances) between the species-- Sam has experience in this-- and then use comparative genomics as an error-correcting guide in solving the assemblies jointly. For example, it'd be odd if you see a genome duplication happen down a branch and then a genome de-duplication again. In that case, it is much more likely that the assembly has been led astray by sequencing errors and that the genome duplication didn't happen. 
> I'm wondering if you're looking for a new problem to work on :) ? I think this would be an important problem as sequencing gets cheaper and we get a lot of non-model organism genomes where the quality of assembly and, especially, the gene calling is sub-par. The variety of sequencing technologies, combined with different assembly pipelines, lead to pretty different results on related genomes (as in my previous email). This is made worse by gene-calling methods that can rely overly on homology to model organisms. Corals, in particular, are evolutionarily distant from model organisms, and it's probably better to also incorporate comparative genomics within corals to inform the gene calling.

## References
- [[@waterhouseEvolutionarySuperscaffoldingChromosome2020]]
- [Mash: fast genome and metagenome distance estimation using MinHash](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0997-x)