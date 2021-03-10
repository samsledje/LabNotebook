## [[CNN Protein Contact Prediction | PPI Prediction Methods]]

- [x] #important Get [[Compare performance with MSA based models | MSA]] contact map prediction running
- [ ] Pool data from many species to train model
- [ ] See how quickly PIPR gets better when given additional fly/mouse data to train on - how generalizable are we / how much tuning is needed to perform better
  - train/test split by protein, not by protein pair
- [ ] Can D-SCRIPT embeddings be used for remote #homology detection and #function prediction
- [ ] One-click pipeline for candidate generation from sequences and GO terms

---

## [[Cow Rumen PPI Network]]
- [ ] #important Submit D-SCRIPT paper to [[Cell Systems Requirements| Cell Systems]]  #due 1 April
    - [ ] Reduce abstract to 150 words
    - [ ] Pipeline schematic
    - [ ] #important Multiple protein averaging MSA - MAFFT for searching for multiple sequence
    - [ ] #important Send Lenore list of rumen proteins with clusters
- [x] Run cow predictions
- [x] Re-do cow predictions with rumen proteins
- [x] Send ENSBTAP proteins to manually include
- [ ] Do cow functional cluster analysis
- [x] Identify interesting functional modules / modules related to rumination
- [x] Map cow gene expression labels to sequences from Bos Taurus
- [x] Map Bos Taurus sequences to XP protein interaction labels from Rohit
- [ ] Compare predicted network and gene expression values
- [x] Predict interactions with specifically ruminant genes from sheep paper
- [ ] Comparitive genomics with sheep ruminant gene network?

---

## [[Interface Classification]]

- [ ] Recovering [[Running PatchBag | Patch Bag]] Embeddings
  - [x] Generate patch bag embeddings for known PDB proteins
  - [x] Cluster patch bag embeddings
  - [x] Train a model from our embeddings and contact maps to recover the clustering
  - [ ] Train a model from our embeddings to recover their embeddings directly
- [ ] How do PatchBag distances correlate with random walk distances in the PPI network?
  - [ ] Compute pairwise patch bag distances
  - [ ] Compute random walk distances
  - [ ] Compute GLIDE distances
- [ ] Download and run [MaSIF](https://github.com/LPDI-EPFL/masif)
- [ ] #important Send Rohit list of chains and their patchBag clusters to compare to SCOP class
- [x] Serious consideration to [[Gainza_et_al_2020_Deciphering_interaction_fingerprints_from_protein_molecular.pdf  | MaSIF Interaction Fingerprints]]
- [ ] Check out [CPORT](http://alcazar.science.uu.nl/services/CPORT/) and [SpotOn](https://alcazar.science.uu.nl/cgi/services/SPOTON/spoton/) for interface prediction stuff

---

## [[Coral PPI Prediction]]

- [ ] #important Narrow down heat shock protein list in [[Coral validation candidates#Hannah Heat Shock Proteins]]
- [ ] Predict PPI interactome in [_Montipora capitata_](http://cyanophora.rutgers.edu/montipora/)
- [ ] Compute gene expression correlations for Acropora
- [x] Re-do Montipora co-expression with >30 genes per sample, >5 samples per gene
- [x] #important Send [[Fluorescence]] predictions & tables to Liza
- [x] Send Fluroescence predictions & tables for TLR/GFP vs. FULL network
- [x] Predict interactions with Judith GPCR candidates in Pdam
- [x] Find GPCR candidate homologs in Mcap
- [x] Predict interactions with GPCR candidates in Mcap
- [x] #important Search for Beta Propeller candidates [[Coral validation candidates#Beta Propellers]]
  - 20-100 candidate interactions
- [x] Predict PPI interactome in _Acropora millepora_
- [x] G protein predictions in Montipora
- [x] Add 2 extra best-homologs from Pdam -> Montipora to gene coexpression matrix
- [x] Check for montipora closest blast hit of vitaminB12 protein in pdam

---
## [[Phylogenetic Genome Assembly]]


---

## Network-Sequence Hybrid
- [x] Send Kapil Fly Experimental Network
- [ ] Predict yeast all vs. all
- [ ] what functional things can we say about the NEW network that we couldn't about the OLD network
- [ ] GLIDE denoising / augmentation
- [ ] De novo gene function and functional similarity prediction at the species level
- [ ] #important Predict D-SCRIPT scores for BioGrid edges that Kapil doesn't have

---

## [[SARS-Cov-2 Phylogenetics]]


- [ ] Tidy up methods
- [ ] Write results
- [ ] Write discussion
- [ ] Look at semantic similarity of sequences and how it varies along the tree
- [ ]  Which species are different between our analysis and Rambaut
- [ ]  Remove "nX" internal node labels where they aren't important
- [ ]  Delve a little further into "recombination highways"
- [ ] Search window analysis for conclusions concordant with ancestral transfers
    - [ ] n49 - n50 in spike protein with medium support
    - [ ] n46 - n2 in envelope
    - [ ] n47 - n2 in orf1ab instead of n48 - n2
    - [ ] a few windows with n2 - n35 early in orf1ab
    - [ ] n35 - n46 in nucleocapsid
    - [ ] n4 - n2 shows up in windows but only very weakly in our analysis -- and in orf1a (in windows), not orf7b (dtl) -- BUT shows up in MAD rooting
-  [x] 2 more simplots -- rows 27 (split) and 31 (no split)
- [x] Send out when2meet for future meetings
- [x] Overlap MAD rooting transfers with DTL rooting transfers -- anything should be supported with >top5% support in BOTH
  - [x] Update circos plot AND ancestral plot
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
- [x] Look at code / get cleaned up for running on test data
- [ ] Run FSESNN on other two benchmark data sets
- [ ] Create IDEM model fitting to the specifications of the manuscript -- proper attention/identity embedding
- [ ] Clean up IDEM manuscript for CS submission
- [ ] Download and clean internal WGS data
- [ ] Run IDEM on WGS data
- [ ] Write IDEM manuscript for journal submission

---

## General

- [ ] Check out [pdb-tools](https://github.com/haddocking/pdb-tools)
- [ ] Write [[Master's Thesis#Proposal]]
- [ ] Update Struct2Net Templates / DBLRAP
