# CNN Protein Contact Prediction

[[D-SCRIPT]]

## RECOMB Manuscript
[Overleaf](https://www.overleaf.com/project/5f624a8a068b1a0001c66ccd)

[[RECOMB Reviews Raw]]
[[RECOMB Review To-Do List]]

# Questions
---

# Organization of Experiments

[PPI Results Tracking](https://docs.google.com/spreadsheets/d/1oZqaSOthxN7HwvO4VgRLlrp7ES76MsN5bXb4qCSEfD0)

## Comparison with MSA Methods
[[Compare performance with MSA based models]]

## Comparison with Deep Learning Methods
- DPPI - Xu
    - [Predicting protein-protein interactions through sequence-based deep learning](https://academic.oup.com/bioinformatics/article/34/17/i802/5093239)
- PIPR - Chen
    - [Multifaceted protein-protein interaction prediction based on Siamese residual RCNN](https://academic.oup.com/bioinformatics/article/35/14/i305/5529260)
- Stacked Autoencoder - Sun
    - [Sequence-based prediction of protein protein interaction using a deep-learning algorithm](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-017-1700-2)
- Richoux
    - [Comparing two deep learning sequence-based models for protein-protein interaction prediction](https://arxiv.org/abs/1901.06268)

- Compute Venn Diagram of predictions with other methods

## Verification of Embeddings

[[D-SCRIPT Embedding UMAP]]
- KNN Search with Positive & Random Anchor Pairs
- BLAST Search with Positive & Random Anchor Pairs
- Search with Positive & Random Anchor Pairs where distance is computed by induced distance from mismatch kernel [https://academic.oup.com/bioinformatics/article/20/4/467/192308](https://academic.oup.com/bioinformatics/article/20/4/467/192308)

## Verification of our Model

IMPORTANT CHECKPOINT MODELS

- r11-r8redux
- r21-20-with-10-to-1-ratio
- r24-pool-size-9
- r26-phat-sqrt-pool-3-lambda-0.35
- r31
- r48
- x Fold Cross validation on our STRING data set
- x Fold Cross validation on Human / Yeast from profPPIkernel
- Validation on protein interactions from several different species
- Binding affinities
- Plots of prediction densities for positive and negative pairs

## Prediction in Coral
    
    python csv_predict.py ~/db/Coral/PdamXSymbC1.50.800.candidates.csv ~/db/Coral/PdamXSymbC1.50.800.fasta pretrained_models/r48-0.35inter-0.65magnitude-projection/model_final.sav ~/db/Coral/PdamXSymbC1.50.800.predictions --embedding ~/db/Coral/PdamXSymbC1.50.800.h5 --device 3`

# Model Notes

## Data

[[Predicting protein-protein interactions using high-quality non-interacting pairs]]

Species Numbers:

9606 - human

4932 - yeast

6239 - worm

From STRING database:

psql -Upostgres -d homo_sapiens_network

\copy {CMD} to {FILE} csv header

- To LINK_PATH: (select * from (select * from network.actions where mode='binding') as binding inner join (select * from network.hierarchical_ogs_transfer_reports where species_id = 9606) as species on binding.item_id_a = species.protein_id_a and binding.item_id_b = species.protein_id_b)
- To SEQ_PATH: (select * from (select * from items.proteins_names where species_id = 9606) as names inner join (select * from items.proteins_sequences) as seqs on names.protein_id = seqs.protein_id)
- To SEQ_PATH: (select names.protein_id, names.protein_name, seqs.sequence from (select * from items.proteins_names where species_id = 9606 and source like 'Ensembl_translation') as names inner join items.proteins_sequences as seqs on names.protein_id = seqs.protein_id) to downloads/string_seq_db.csv
- To IDMAP_PATH: (select protein_name, protein_id from items.proteins_names where source like 'Ensembl_translation' and species_id=9606)
- PDB: \copy (select protein_name, protein_id from items.proteins_names where source like '%PDB%' and species_id = 9606) to '/afs/csail/u/s/samsl/db/STRING/homo.sapiens/downloads/PDB_ID_MAPPING.csv' csv header

Dates of protein interactions becoming available:

- CREATE VIEW [species_LINKS_SOURCES] as (select links.item_id_a, links.item_id_b, links.mode, sets.sources from (select * from evidence.actions_sets where mode = 'binding') as sets inner join (select * from (select * from network.actions where mode='binding') as binding inner join (select * from network.hierarchical_ogs_transfer_reports where species_id = [SPECIES ID]) as species on binding.item_id_a = species.protein_id_a and binding.item_id_b = species.protein_id_b) as links on links.item_id_a = sets.item_id_a and links.item_id_b = sets.item_id_b group by links.item_id_a, links.item_id_b, links.mode, sets.sources);
- \copy (select * from (select * from [species]_links_sources) as [species] inner join (select * from node_pair_experimental) as scores on [species] .item_id_a = scores.node_id_a and [species] .item_id_b = scores.node_id_b where sources like '%PMID%') to '/afs/csail/u/s/samsl/db/STRING/pub_dates/[species]_experimental_binding_pmid_sources.csv' csv header
- Run do_clean_sources.sh
- create table yeast_evidence_binding_pmids (id varchar); copy yeast_evidence_binding_pmids(id) from '/afs/csail/u/s/samsl/db/STRING/pub_dates/clean_scere_experimental_binding_pmid_sources.csv' csv header;
- \copy (select publication_id, publication_date from yeast_evidence_binding_pmids as yeast inner join evidence.publications as pubs on [yeast.id](http://yeast.id/) = pubs.publication_id group by publication_id, publication_date) to '/afs/csail/u/s/samsl/db/STRING/pub_dates/scere_experimental_binding_pmid_dates.csv' csv header;
- python do_plot_dates.py scere_experimental_binding_pmid_dates.csv

- select item_id, min(first_date) from (select item_id, publication_id from evidence.items_publications group by item_id, publication_id) as pubid inner join (select publication_id, min(publication_date) as first_date from evidence.publications group by publication_id) as pubdate on pubid.publication_id = pubdate.publication_id group by item_id;
- \copy (select * from (select * from human_links_sources) as human inner join (select * from node_pair_experimental) as scores on human.item_id_a = scores.node_id_a and human.item_id_b = scores.node_id_b where sources like '%PMID%') to '/afs/csail/u/s/samsl/db/STRING/homo.sapiens/experimental_binding_pmid_sources.csv' csv header

In Python:

Drop duplicates from both

Inner merge on protein_id_a then protein_id_b

Drop all columns except protein_id_{a,b} and sequence_{a,b}

- Protein complex contacts from PDB

    [](https://zlab.umassmed.edu/benchmark/)

- Compare prediction accuracy on membrane proteins / soluble proteins

[Download](http://hint.yulab.org/download/)

## Model

![[/Scannable Document on Mar 25, 2020 at 10_51_27.png]]

$$f(i,j,\theta, \lambda) = (1-\theta)(exp(-\lambda[\frac{(i+1) - \frac{(N+1)}{2}}{\frac{N+1}{2}}]) \cdot exp(-\lambda[\frac{(j+1) - \frac{(M+1)}{2}}{\frac{M+1}{2}}])) + \theta$$

$$phat(x_0,x_1) = \frac{\sum q_{ij}}{\sum sign(q_{ij})}$$

- Do we include pooling / dropout / regularization layers?
- Embedding with LM
- Position contact prediction
    - Two residues contact if distance of C_beta atoms is < 8 angstrom
    - Pixel-level labeling
    - Contact supervision

full dataset cross val

```bash
python train_interaction_flex.py --pos-pairs ~/db/STRING/homo.sapiens/cv/0.train.pos --neg-pairs ~/db/STRING/homo.sapiens/cv/0.train.neg --pos-test ~/db/STRING/homo.sapiens/cv/0.test.pos --neg-test ~/db/STRING/homo.sapiens/cv/0.test.neg --use-w --do-pool --pool-width 9 --num-epochs 50 --epoch-scale 5 --pred-skew 0.5 --skew-alpha 0.5 --lambda 0.35--output pretrained_models/fd1-skew-0.5-alpha-0.5-lambda-0.35-pool-9/output0.txt --save-prefix pretrained_models/fd1-skew-0.5-alpha-0.5-lambda-0.35-pool-9/model0 --device 0
```

## Training

- Optimizer —> ADAM
- Interaction loss —> binary cross entropy
- Contact Map Loss - regularization at cmap level - add mean of contact map to the loss
- Lambda
- Weight
- Cross validation
    - Residue contact mask
    - Tristan embeddings vs. learned embeddings vs. non-deep alignment features
        - ProteinNet Rao et al
        - Evolutionary Trace - [http://lichtargelab.org/software/ETserver](http://lichtargelab.org/software/ETserver)