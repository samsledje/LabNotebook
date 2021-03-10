## [[Research Tasks#Biological Case Study for RECOMB Cell Systems | Tasks]]

## References
[Compendium of 4,941 rumen metagenome-assembled genomes for rumen microbiome biology and enzyme discovery](https://www.nature.com/articles/s41587-019-0202-3)

## Objectives:
- Less well-studied species from a network perspective
    - [[PPI in Malaria]]
    - [sheep](https://pubmed.ncbi.nlm.nih.gov/24904168/)
    - [songbirds](https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC4359888&blobtype=pdf) suggested by Lenore
- Something where we can focused on _pathways_ and _modules_ rather than individual interactions
- Focus on _binding interactions_ not _regulatory interactions_
- Rohit To Do: Look up cow rumen on google scholar, curate a list of 15-20 genes involved in cow digestion, run PPI on whole genome w/ rumen genes, tie back to [sheep rumen](https://pubmed.ncbi.nlm.nih.gov/24904168/)

## Cow rna-seq:   
- [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE160028](https://www.google.com/url?q=https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc%3DGSE160028&sa=D&source=hangouts&ust=1613149873656000&usg=AFQjCNFn7JUDnC1E0feM8CJvXYDlkNfEGw)  \*new nanopore reads ~100 samples  
- [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99210](https://www.google.com/url?q=https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc%3DGSE99210&sa=D&source=hangouts&ust=1613149873656000&usg=AFQjCNF4lubyE2CYKwgCOickCp3njiD8bg)  \*early embryo-- not ideal  
- [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE82272](https://www.google.com/url?q=https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc%3DGSE82272&sa=D&source=hangouts&ust=1613149873656000&usg=AFQjCNGh6nwCU21WjfVl0CwYEO6PbKdmSA) \*ruminal epithelium-- great but old  
- [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE136800](https://www.google.com/url?q=https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc%3DGSE136800&sa=D&source=hangouts&ust=1613149873656000&usg=AFQjCNHl3GD-EY_24KESL7I6EuHgks-ZYA) \*also stem cells ?  
- [https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE162952](https://www.google.com/url?q=https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc%3DGSE162952&sa=D&source=hangouts&ust=1613149873656000&usg=AFQjCNEXkabN4OjXckWk6-Cw-BcmYwFW9g)  \*fetal gonads-- not ideal

## Cow Rumen-Specific Proteins
- TCHHL2:
    - ENSBTAP00000066329.1
    - ENSBTAP00000060747.1
- PRD-SPRII:
    - ENSBTAP00000063491.1
    - ENSBTAP00000065881.1
    - ENSBTAP00000070493.1
    - ENSBTAP00000070470.1
    - ENSBTAP00000044090.1
- S100-A12:
    - ENSBTAP00000056088.2
    - ENSBTAP00000034009.2
    - ENSBTAP00000008523.6
    - ENSBTAP00000067294.1
- S100-A2:
    - ENSBTAP00000000589.2


### Predict Interactome
```
dscript predict --pairs cow_candidates_clean_asof_20210222.tsv.0{i} --model ~/Group/www/data/dscript/data/models/human_v1.sav --embeddings ../Bos_taurus.ARS-UCD1.2.pep.clean.h5 --outfile cow_rumen_predictions_asof_20210222.0{i} --device {i}
```

[[Cow Rumen 300k Results]]

### Functional Categories
- Immune Response -- t cell, b cell, antibody, inflammatory response, etc.
- Calcium/Zinc/Magnesium/S100 binding
- Transcription factor binding / RNA polymerase / DNA binding
- [SH2](https://pfam.xfam.org/family/SH2) Domain Binding
- [phosphatidylinositol](https://en.wikipedia.org/wiki/Phosphatidylinositol) binding

### Clusters
- Cluster 532566686263287317
    - ENSBTAP00000056088.2 (rumen, S100-A12)
    - ENSBTAP00000034009.2 (rumen, S100-A12)
    - ENSBTAP00000008523.6 (rumen, S100-A12)
    - ENSBTAP00000067294.1 (rumen, S100-A12)
    - ENSBTAP00000000589.2(rumen, S100-A2)
- Cluster  2136893754839125225
    - ENSBTAP00000066329.1 (rumen, TCHHL2)
    - ENSBTAP00000060747.1 (rumen, TCHHL2)
    - ENSBTAP00000060528.1 which is the center of the complex formed by two TCHHL2 proteins is 125 residues long, and has a 75.5% match to uniprot [A0A075B6I0](https://www.uniprot.org/uniprot/A0A075B6I0) and the human protein IGLV8-61 , one of the proteins part of the light chain of immunoglobulin (i.e. antibodies)
- Cluster 184581346961070354
    - ENSBTAP00000063491.1 (rumen, PRD-SPRII)
    - ENSBTAP00000070493.1 (rumen, PRD-SPRII)
- Cluster 2220037255618645010
    - ENSBTAP00000070470.1 (rumen, PRD-SPRII)
    - Connected through ENSBTAP00000056580.1 - like human [GSX2](https://www.genecards.org/cgi-bin/carddisp.pl?gene=GSX2) - Transcription factor
    - To ENSBTAP00000004986.4 - bovine hepsin [HPN](https://www.uniprot.org/uniprot/A1L5C6)
- Cluster 848614617682430755
    - ENSBTAP00000065881.1 (rumen, PRD-SPRII)
    - Connected through ENSBTAP00000010113.3 - bovine [AGXT2](https://www.uniprot.org/uniprot/Q17QF0)
- ENSBTAP00000044090.1 (rumen, PRD-SPRII) not in any clusters -- ego graph cluster is 601666597559199004
    - brain segmentation, visual perception, locomotory behavior, neuromuscular process
- ENSBTAP00000054517.1 -- bovine [CANX](https://www.uniprot.org/uniprot/A7Z066) connects S100, TCHHL2, and PRD-SPRII clusters

