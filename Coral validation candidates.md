- [Candidate PPIs Google Sheet](https://docs.google.com/spreadsheets/d/1w-fJ8koBLLAzB_tMVrrdSSDLqvzsnsuprbEMwcJ89ZE/edit?usp=sharing)
- [[List of questions about coral experiment types]] 
- [[Meet with Natasha and Judith 05 Jan 2021]]
- [[Meeting with Hollie 04 Jan 2021]]
- [[Meeting with Debashish and Phil 28 Jan 2021]]

# Experimental Validation High Level
get clusters that are involved with sensory perception in 3 networks, take pairs we predict and validate some
- pull out clusters with lokender's and hannah's proteins
- look at clusters in cytoscape and decide which ones to look at
- homology based --> proteins which look like heat shock proteins in other species
- computational docking screen
    - [InterEvDock2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6030979/)
    - [HDOCK](http://hdock.phys.hust.edu.cn/)
    - [Struct2Net](http://cb.csail.mit.edu/cb/struct2net/webserver/)
    - [HADDOCK](https://wenmr.science.uu.nl/haddock2.4/)
- shortlist of experimental validation candidates
    - yeast two hybrid / co immuno-precipitation

# Candidates

## Sensory Perception Clusters
- 894982169120702597
- 108400644249311062
- 1797582330054254039
- 83190531764443604
- **1869880305084515762**
- **1536542255591810346** (and Ca+ binding)
- 750568462183856468
- 603593032561892165
- 1760879761140871336
- **128415096254841052** (visual perception)
- 1201615696319342022
- 2293950928530227780
- **677832734244605912** (cocaine)
- 500307542323764329
- 343147617515947034
- 403843271590465059
- 259720880979499154

## GPCRs
_Judith K-S, Nathan Brenner_

1. Find [Alpha](https://www.uniprot.org/uniprot/P08539), Beta, [Gamma](https://www.uniprot.org/uniprot/G3V2N0) Homologs
2. Union of all hhblits hits to identify candidates
3. Run all vs. all predictions
4. Find triad of alpha/beta/gamma interaction
5. See where those proteins slot in to larger functional modules

## Toll-Like Receptors
_Lokender Kumar_

TLRs, find interaction partners as homologs with human interactors of TLRs
Stimulate cell with signals and do qPCR
- **pdam_00000737-RA**
    - Ubiquitin protein activity: 1294492063848056811
    - Almost ALL its partners are in clusters enriched for Ubiquitin protein activity
    - Very high probability wtih pdam_00005996-RA --> 1650493990156415144
- pdam_00011599-RA
- **pdam_00011734-RA** 
    - Calcium ion binding: 1992563040795069362
    - In cluster 1306735003166862070 in cross-species network
    - High probaiblity of interaction with:

        |Name|Like|Cluster|
        |---|---|---|
        |pdam_00023012-RA | [ANOS1 Anosmin-1](https://www.uniprot.org/uniprot/P33005)|1981445261579114090|
        |pdam_00019117-RA | [PTPRF Receptor-type tyrosine-protein phosphatase F](https://www.uniprot.org/uniprot/P10586) | 2073267652699415213 |
        |pdam_00012834-RA | [LRRC4 Leucine-rich repeat-containing protein 4](https://www.uniprot.org/uniprot/Q9HBW1) | 1997884882038636813 |
        | pdam_00018978-RA | [TTN Titin](https://www.ncbi.nlm.nih.gov/gene/7273) | 2052514917294681156 | 
        among others

- pdam_00013021-RA
- pdam_00014109-RA
- **pdam_00015877-RA**
    - Doesn't appear in a Pdam cluster, but 94 interaction partners
    - Interaction partners tend to enrich for Calcium ion binding -- same **1997884882038636813** cluster
    - Potentially interesting interaction partners
        - pdam_00006144-RA in **1107002493754196241** -- GTPase activity
        - pdam_00023591-RA in 516559616760565246 -- Heparin Binding
- **pdam_00015883-RA**
    - Calcium ion binding: 259321696093329610
    - High probability of interaction with:
 
        |Name|Like|Cluster|
        |---|---|---|
        | pdam_00021982-RA | [Ptprq Phosphatidylinositol phosphatase PTPRQ](https://pubmed.ncbi.nlm.nih.gov/12837292/#:~:text=Abstract,%2C%20proliferation%2C%20and%20subcellular%20architecture.) | 1132719596777009417 |
        |pdam_00006270-RA | [Rasl11a Ras-like protein family member 11A](https://www.uniprot.org/uniprot/Q6T310) | **1997884882038636813** |
        | pdam_00009914-RA | [prtgb Protogenin B](https://www.uniprot.org/uniprot/F1QXD0) | **1997884882038636813** |
        | pdam_00004446-RA | [SYT10 Synaptotagmin-10](https://www.uniprot.org/uniprot/Q6XYQ8) | **1997884882038636813** |

- pdam_00017966-RA
- pdam_00021819-RA
- **pdam_00022930-RA**
    - Does not appear in a Pdam cluster, but 98 predicted interactions
    - Interaction partners tend to enrich for Calcium ion binding -- same **1997884882038636813** cluster
- **pdam_00022934-RA**
    - Does not appear in a Pdam cluster, but 120 predicted interactions
    - Potentially interesting partner:
        - pdam_00019835-RA in **1107002493754196241** -- GTPase activity
- pdam_00009200-RA

## Heat Shock Proteins
_Hannah Reich, Hollie Putnam_

This list obtained by BLASTing [Q5FB17 - Pdam HSP70](https://www.uniprot.org/uniprot/Q5FB17.fasta) against our Pdam database

1. Extract all heat shock proteins from Pdam FASTA file
2. Extract all clusters with at least one heat shock protein
3. Take union of clusters and form heat shock subgraph
4. [HHBlits](https://hhblits.cs.tufts.edu/) heat shock subgraph proteins against human or mouse
5. Look for RNAseq data correlation and limit to high correlated interactions
6. Proteomics
7. Look at coevolution / evolutionary trace 
8. Docking prediction
    1. Predict structure w/ RaptorX
    2. Dock w/ ClusPro
9. Filter on PIPR predictions?

- pdam_00009088-RA: **1949589803738394157**
- pdam_00014847-RA: **1949589803738394157**
- pdam_00013964-RA: 656688816176176777
- pdam_00018127-RA: 165664055434327126
- pdam_00014605-RA: 165664055434327126
- pdam_00015460-RA: 165664055434327126
- pdam_00002141-RA: **1888259642088437943**
- pdam_00017170-RA: 2294801486550053239

**476510776833627218** - DnaJ cluster

Compare interactions in clade C vs. clade D, clade D has higher heat tolerance

## Metabolism
_Hannah Reich_

- pdam_00005699-RA
- pdam_00020994-RA
    - Cluster: **598905948006133749**
- **pdam_00002527-RA**
    - Cluster: 631179896347094217
- pdam_00011749-RA
    - Cluster: **598905948006133749**
- pdam_00019926-RA
    - Cluster: 424980178978555871
- pdam_00021852-RA
    - Cluster: **598905948006133749**
- pdam_00006965-RA
    - Cluster: 1870598708561555580
- pdam_00017871-RA
    - Cluster: 631179896347094217
- pdam_00014925-RA
    - Cluster: pdam_00014925-RA
- pdam_00015692-RA
- pdam_00014487-RA
    - Cluster: 1922627732759814528
- pdam_00016812-RA
- pdam_00005771-RA
    - Cluster: 763831930704106115