# Coral Network Clusters & Enrichment

# Network Reconstruction & Enrichment

## Generate Candidate Pairs

```bash
[[]]
```

## Pocillopora damicornis

Symbiont: Symbiodinium goreaui (Clade C, type C1, now Cladocopium goreaui)

## Hydra Vulgaris

[Stem cell differentiation trajectories in Hydra resolved at single-cell resolution](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7104783/)

## Diffusion State Distance (DSD & cDSD)

- cDSD
- Converged
- Cut off at some confidence (we use 0.7)

## Spectral Clustering

[[TeamTuskIndvpaper.pdf]]

- k = 500

## GO Annotation & Enrichment

Interesting proteins to search our clusters for:

[https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0192001](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0192001)

[https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7104783/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7104783/)

## Orthology

- Find hydra ID for different protein names/functions

```bash
awk -F"," '{ print $1","$2}' ~/db/STRING/h.vulgaris/DB_SEQS.csv | grep -i {TERM} | sort | uniq -f 1
```

- Compute IsoRank alignment between STRING human and mouse networks and compute functional coherence score, compare with aligning human and mouse networks generated using our method and compute function coherence score
- Can we augment IsoRank with GO terms (add to bit score similarity, something like that)
    - Network Alignment + Module identification —> use modules to help align networks & alignment to help identify modules
- IsoRank w/ human & pdam, transfer annotations from human to pdam —> gpcr tlr analogs

```bash
~/Applications/isorank/isorank-n-s-v3-64  --K 3 --threadid 4 --thresh 1e-4 --alpha 0.6 --maxveclen 1000000 --o hsapi_hvulg_pdam_cluster_output.txt --prefix /afs/csail/u/s/samsl/Berger/interactionPredictionWithContact/isorank/isorank_human /afs/csail/u/s/samsl/Berger/interactionPredictionWithContact/isorank/Hsapi-Hvulg-Pdam.inp
```