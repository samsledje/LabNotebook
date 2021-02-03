## [[CNN Protein Contact Prediction | PPI Prediction Methods]]
- [ ] #important Get [[Compare performance with MSA based models | MSA]] contact map prediction running
- [ ] [[Biological Case Study for RECOMB Cell Systems]] #due 1 April
- [ ] Pool data from many species to train model
- [ ] See how quickly PIPR gets better when given additional fly/mouse data to train on - how generalizable are we / how much tuning is needed to perform better
    - train/test split by protein, not by protein pair
- [ ] Can D-SCRIPT embeddings be used for remote #homology detection and #function prediction

---
## [[Interface Classification]]
- [ ] Recovering Patch Bag Embeddings
    - [x] Generate patch bag embeddings for known PDB proteins
    - [x] Cluster patch bag embeddings
    - [ ] Train a model from our embeddings and contact maps to recover the clustering
    - [ ] Train a model from our embeddings to recover their embeddings directly
- [ ] How do PatchBag distances correlate with random walk distances in the PPI network?
    - [ ] Compute pairwise patch bag distances
    - [ ] Compute random walk distances
    - [ ] Compute GLIDE distances
- [ ] Check out [CPORT](http://alcazar.science.uu.nl/services/CPORT/) and [SpotOn](https://alcazar.science.uu.nl/cgi/services/SPOTON/spoton/) for interface prediction stuff

---
## [[Coral PPI Prediction]]
- [ ] #important Narrow down heat shock protein list in [[Coral validation candidates#Hannah Heat Shock Proteins]]
- [ ] #important Search for Beta Propeller candidates [[Coral validation candidates#Beta Propellers]]
    - 20-100 candidate interactions 
- [ ] Enrichment of high/low pH interactions --> Federica Scucchia Haifa
- [ ] Predict PPI interactome in [_Montipora capitata_](http://cyanophora.rutgers.edu/montipora/)

## Network-Sequence Hybrid

- [ ] Take only HIGH confidence D-SCRIPT interactions as "starter" network
    - see what interactions GLIDE would predict
    - what is their overlap with OTHER predictions D-SCRIPT makes
    - what functional things can we say about the NEW network that we couldn't about the OLD network
- [ ] GLIDE stuff w/ Kapil

---
## [[SARS-Cov-2 Phylogenetics]]
- [x] Hammer out detailed methods with Sumaira
- [ ] Update leaf names on circular ancestral transfers plot to be more readable
- [x] Check _direction_ of transfers
    - [ ] For transfers with support in either direction, see if they are unidirectional in individual trees (since we created 10 different ones) -- within a tree, support should be directionally consistent
- [ ] And update [Circos plot](http://mkweb.bcgsc.ca/tableviewer/)
- [ ] **Compute statistics on individual transfers and bunched transfers**
- [ ] Standardize name map (and update figures)
- [ ] Search window analysis for conclusions concordant with ancestral transfers
- [x] Re-root trees with MAD rooting (need to re-optimize branch lengths) and re-do transfer analysis
- [x] Read [[Recombination_In_Viruses_Losada.pdf]]
- [x] Read papers in [[Reading List#Species Tree Estimation]] and [[Reading List#Recombination Detection]]
- [x] Identify transfers with >80% bootstrap support and top transfers in clade of interest
- [x] Present tables in tree/figure format for next week
- [x] Schedule a meeting with Sumaira
- [x] Identify important transfers to present with Sumaira

---
## General

- [ ] Check out [pdb-tools](https://github.com/haddocking/pdb-tools)
- [ ] #important Review for Lenore at [Bioinformatics](https://mc.manuscriptcentral.com/bioinformatics)
- [ ] Write [[Master's Thesis#Proposal]]
- [ ] Update Struct2Net Templates / DBLRAP