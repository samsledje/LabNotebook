- [Candidate PPIs Google Sheet](https://docs.google.com/spreadsheets/d/1w-fJ8koBLLAzB_tMVrrdSSDLqvzsnsuprbEMwcJ89ZE/edit?usp=sharing)
- [[List of questions about coral experiment types]] 
- [[Meeting with Hollie 04 Jan 2021]]
- [[Meet with Natasha and Judith 05 Jan 2021]]
- [[Meeting with Debashish and Phil 28 Jan 2021]]

### Coral Species
_P. damicornis_
_M. capitata_
_P. acuta_
_A. millipora_

# Experimental Validation High Level

1. Extract relevant {function} proteins from Pdam FASTA file
2. Extract all clusters with at least one {function} protein
3. Take union of clusters and form {function} subgraph
4. [HHBlits](https://hhblits.cs.tufts.edu/) {function} subgraph proteins against human or mouse --> find proteins which look like {function} proteins in other species
5. Look for RNAseq data correlation and limit to high correlated interactions
6. Proteomics
7. Look at coevolution / evolutionary trace 
8. Docking prediction
    1. Predict structure w/ RaptorX
    2. Dock w/ ClusPro
    - [InterEvDock2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6030979/)
    - [HDOCK](http://hdock.phys.hust.edu.cn/)
    - [Struct2Net](http://cb.csail.mit.edu/cb/struct2net/webserver/)
    - [HADDOCK](https://wenmr.science.uu.nl/haddock2.4/)
9. Filter on PIPR predictions
10. Experimental Validation
    1. Direct validation -- two hybrid / co immuno-precipitation
    2. Functional validation -- knockout to phenotypic response

# Functional Candidates

[[Sensory Perception Clusters]]

[[G Protein Heterotrimer & GPCR]]

[[Toll-Like Receptors]]

[[Heat Shock Proteins]]

[[Metabolism]]

[[Fluoresence]] 

[[Cross-Species]]