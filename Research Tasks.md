## [[CNN Protein Contact Prediction | PPI Prediction Methods]]
- [ ] #important 2 page camera ready for RECOMB proceedings #due 22 January
- [ ] #important Update paper for bioRxiv #due 22 January
- [ ] #important Get [[Compare performance with MSA based models | MSA]] contact map prediction running
- [ ] [[Biological Case Study for RECOMB Cell Systems]] #due 1 April
- [ ] Pool data from many species to train model
- [ ] See how quickly PIPR gets better when given additional fly/mouse data to train on - how generalizable are we / how much tuning is needed to perform better
    - train/test split by protein, not by protein pair
- [ ] Can D-SCRIPT embeddings be used for remote #homology detection and #function prediction
- [x] Submit abstract to [CSHL Networks Meeting](https://meetings.cshl.edu/meetings.aspx?meet=NETWORK&year=21)

---
## [[Binding Pocket Characterization]]
- [x] #important Get [[Kolodny_Protein_Interface_Similarity.pdf | PatchBag]] up and running to generate basis vectors for a given protein - [[Running PatchBag]]
- [ ] #important Compare clustering in D-SCRIPT embedding space and PatchBag space -- how similar are they _out of the bag_
- [ ] Recovering Patch Bag Embeddings
    - [x] Generate patch bag embeddings for known PDB proteins
    - [ ] Cluster patch bag embeddings
    - [ ] Train a model from our embeddings and contact maps to recover the clustering
    - [ ] Train a model from our embeddings to recover their embeddings directly
- [ ] How do PatchBag distances correlate with random walk distances in the PPI network?
    - [ ] Compute pairwise patch bag distances
    - [ ] Compute random walk distances
    - [ ] Compute GLIDE distances

---
## [[Coral PPI Prediction]]
- [ ] We need to generate [[Coral experimental candidates]] for experimental validation ASAP
    - [x] Put together [[List of questions about coral experiment types]] 
    - [x] [[Meet with Natasha and Judith 05 Jan 2021]]
    - [x] [[Meeting with Hollie 04 Jan 2021]]
- [Candidate PPIs Google Sheet](https://docs.google.com/spreadsheets/d/1w-fJ8koBLLAzB_tMVrrdSSDLqvzsnsuprbEMwcJ89ZE/edit?usp=sharing)
- [ ] Map [ReefGenomics](http://pdam.reefgenomics.org/) [Pdam](https://www.nature.com/articles/s41598-018-34459-8) IDs to NCBI IDs
- [ ] Enrichment of high/low pH interactions --> Federica Scucchia Haifa

## Network-Sequence Hybrid
- [ ] GLIDE stuff w/ Kapil

---
## [[SARS-Cov-2 Phylogenetics]]
- [x] Read papers in [[Reading List#Species Tree Estimation]] and [[Reading List#Recombination Detection]]
- [x] Identify transfers with >80% bootstrap support and top transfers in clade of interest
- [x] Present tables in tree/figure format for next week
- [x] Schedule a meeting with Sumaira
- [ ] Hammer out detailed methods with Sumaira
- [x] Identify important transfers to present with Sumaira

## General

- [ ] Write [[Master's Thesis#Proposal]]