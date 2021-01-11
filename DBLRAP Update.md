# DBLRAP Update

### TODO:

[[Other threading programs to stand in for DBLRAP]]

1. update **DBLRAP** + regression

    Struct2Net contains the DBLRAP algorithm for predicting protein-protein interaction scores from sequences using structure

    - convert to standalone linux util
    - wrap DBLRAP_BIN

        [[7271479.pdf]]

        RAPTOR manual

    - update logistic regression (DBLRAP scores --> prob. of interaction)
    - train from STRING or gpb list
    - update PDB sequence database for BLAST and dimer
        - Full PDB list for blast
        - Interaction part for dimer intersection - interaction when complexes have contact points < 4.5 angstroms
2. access coral&algae protein sequences from Tufts server
3. 
    Study on the genome of Porites lutea and its primarily Symbiodinaceae, Cladicopium C15

    - Plutea lutea (~28-31k protein sequences)
        - See note on PDF for gene annotation pipeline
    - Cladicopium C15 (~22.5k protein sequences)
        - See note on PDF for gene annotation pipeline

    Study on the genome of Pocillopora damicornis (Pdam)

    - Pdam (~26k protein sequences)
- ML transfer learning of PPI
    - given 2 sequences from unknown organisms --> can we predict interaction without structure?
    - look for homologous sequences using [**PSI-BLAST**](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE=Proteins&PROGRAM=blastp&RUN_PSIBLAST=on) in [**STRING**](https://string-db.org/) which interact
    - construct known network with STRING interactions (experiments/biochemistry, normal/transfer)
    - train some model to give confidence score for PPI based on homologous interactions in STRING
        - Select random subset of data —> see note on Yu 2010
            - Select subset of proteins, then all proteins which interact with them (to maintain degree distribution of subsampled training network)
        - encode proteins using autocovariance (AC) or cojoint triad (CT) method —> see note on Sun 2017
    - find data for protein interactions across species to understand what that distribution looks like
1. ensemble predictions from DBLRAP and (3) to give a predicted interaction score
2. run coral+algae protein sequences from (2) through (3/4) to generate proposed PPI to test experimentally