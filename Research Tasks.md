## [[CNN Protein Contact Prediction | PPI Prediction Methods]]

- [ ] #important Get [[Compare performance with MSA based models | MSA]] contact map prediction running
- [ ] Pool data from many species to train model
- [ ] See how quickly PIPR gets better when given additional fly/mouse data to train on - how generalizable are we / how much tuning is needed to perform better
  - train/test split by protein, not by protein pair
- [ ] Can D-SCRIPT embeddings be used for remote #homology detection and #function prediction
- [ ] One-click pipeline for candidate generation from sequences and GO terms

---

## [[Biological Case Study for RECOMB Cell Systems]]
- [ ] #important [[Biological Case Study for RECOMB Cell Systems]] #due 1 April
- [x] Run cow predictions for Cell Systems
- [ ] Send ENSBTAP proteins to manually include
    - ENSBTAP00000063491
    - ENSBTAP00000065881
    - ENSBTAP00000070493
    - ENSBTAP00000070470
    - ENSBTAP00000044090

- [ ] Do cow functional cluster analysis for Cell Systems
- [ ] Identify interesting functional modules / modules related to rumination
- [ ] Map cow gene expression labels to sequences from Bos Taurus
- [ ] Map Bos Taurus sequences to XP protein interaction labels from Rohit
- [ ] Compare predicted network and gene expression values
- [ ] Predict interactions with specifically ruminant genes from sheep paper
- [ ] Comparitive genomics with sheep ruminant gene network?

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
- [ ] Serious consideration to [[Severrisson_Deciphering_interaction_fingerprints.pdf | MaSIF Interaction Fingerprints]]
- [ ] Check out [CPORT](http://alcazar.science.uu.nl/services/CPORT/) and [SpotOn](https://alcazar.science.uu.nl/cgi/services/SPOTON/spoton/) for interface prediction stuff

---

## [[Coral PPI Prediction]]

- [ ] #important Narrow down heat shock protein list in [[Coral validation candidates#Hannah Heat Shock Proteins]]
- [ ] Predict PPI interactome in [_Montipora capitata_](http://cyanophora.rutgers.edu/montipora/)
- [x] Re-do Montipora co-expression with >30 genes per sample, >5 samples per gene
- [ ] Compute gene expression correlations for Acropora
- [x] #important Search for Beta Propeller candidates [[Coral validation candidates#Beta Propellers]]
  - 20-100 candidate interactions
- [x] Predict PPI interactome in _Acropora millepora_
- [x] GCPR in Montipora
- [x] Add 2 extra best-homologs from Pdam -> Montipora to gene coexpression matrix
- [x] Check for montipora closest blast hit of vitaminB12 protein in pdam
    - 

---

## Network-Sequence Hybrid
- [ ] Send Kapil Fly Experimental Network
- [ ] Predict yeast all vs. all
- [ ] what functional things can we say about the NEW network that we couldn't about the OLD network
- [ ] GLIDE denoising / augmentation
- [ ] De novo gene function and functional similarity prediction at the species level

---

## [[SARS-Cov-2 Phylogenetics]]

- [x] Send out when2meet for future meetings
- [ ] Tidy up methods
- [ ] Write results
- [ ] Write discussion
- [ ] Overlap MAD rooting transfers with DTL rooting transfers -- anything should be supported with >top5% support in BOTH
  - [ ] Update circos plot AND ancestral plot
-  [ ] Search window analysis for conclusions concordant with ancestral transfers
-  [x] 2 more simplots -- rows 27 (split) and 31 (no split)
- [x] Hammer out detailed methods with Sumaira
- [x] Update leaf names on circular ancestral transfers plot to be more readable
- [x] Check _direction_ of transfers
- [x] For transfers with support in either direction, see if they are unidirectional in individual trees (since we created 10 different ones) -- within a tree, support should be directionally consistent
- [x] Update [Circos plot](http://mkweb.bcgsc.ca/tableviewer/) names
- [x] **Compute statistics on individual transfers and bunched transfers**
- [x] Standardize name map
- [x] Re-root trees with MAD rooting (need to re-optimize branch lengths) and re-do transfer analysis
- [x] Read [[Recombination_In_Viruses_Losada.pdf]]
- [x] Read papers in [[Reading List#Species Tree Estimation]] and [[Reading List#Recombination Detection]]
- [x] Identify transfers with >80% bootstrap support and top transfers in clade of interest
- [x] Present tables in tree/figure format for next week
- [x] Schedule a meeting with Sumaira
- [x] Identify important transfers to present with Sumaira

---

# [[Interpretable Deep Embedding Model  | IDEM]]

- [x] Write Lily email with manuscript and my notes/questions
- [ ] Look at code / get cleaned up for running on test data
- [ ] Clean up IDEM manuscript for CS submission
- [ ] Download and clean internal WGS data
- [ ] Run IDEM on WGS data
- [ ] Write IDEM manuscript for journal submission

---

## General

- [ ] Check out [pdb-tools](https://github.com/haddocking/pdb-tools)
- [ ] Write [[Master's Thesis#Proposal]]
- [ ] Update Struct2Net Templates / DBLRAP
