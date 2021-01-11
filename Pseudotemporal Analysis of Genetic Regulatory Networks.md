# Psuedotemporal Analysis of Genetic Regulatory Networks

[Pseudotime GRN Project Outline](https://docs.google.com/document/d/1VMwINQNn5krrXqX4gtP6vw0PTOeKcZ-oXK3FEA6Gut4/edit?usp=drivesdk)

# Data

- TCGA

    [Expression Atlas](https://www.ebi.ac.uk/gxa/experiments/E-MTAB-2770/Results)

- Visualization of Data

    [Network plot from expression data in R using igraph](https://www.biostars.org/p/285296/)

- Single Cell Data

# Methods

## New Ideas

- [https://en.wikipedia.org/wiki/Canonical_correlation](https://en.wikipedia.org/wiki/Canonical_correlation)
- Trajectorama analysis of different data sets from different time points
    - Might be best for Huntington's where we have multiple samples from clearly defined different levels of progression
    - [http://cb.csail.mit.edu/cb/trajectorama/](http://cb.csail.mit.edu/cb/trajectorama/)
    - Compare with ACTIONet - [https://www.biorxiv.org/content/10.1101/746339v2.full.pdf](https://www.biorxiv.org/content/10.1101/746339v2.full.pdf)
- Use co-expression to locate gene modules, and then arrange those along a trajectory
- Take a look at SCENIC - [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5937676/pdf/emss-74166.pdf](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5937676/pdf/emss-74166.pdf)
- Gene filtering by (1) total number of counts (2) number of cells it is expressed in (3) highly variable
- Clustering by TF-IDF - [https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-018-4922-4](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-018-4922-4)
- Discover number of clusters by gap statistic approach

## Select Important genes from full set

[Deep multiomics profiling of brain tumors identifies signaling networks downstream of cancer driver genes](https://www.nature.com/articles/s41467-019-11661-4)

- Biological / empirical selection of genes
- Computational Methods for gene filtering

    [](https://www.sciencedirect.com/science/article/pii/B9780128163566000033)

    [](https://www.sciencedirect.com/science/article/pii/B9780128163566000045)

- Identify important gene sets for cell types, pathways, disease

    [GSEA | MSigDB](http://software.broadinstitute.org/gsea/msigdb/)

    [KEGG PATHWAY Database](https://www.genome.jp/kegg/pathway.html#disease)

## Generate co-expression networks

- Nodes are genes, connected by relatedness / similarity of expression in cells
- Distance metric between genes

    [Using Machine Learning to Measure Relatedness Between Genes: A Multi-Features Model](https://www.nature.com/articles/s41598-019-40780-7)

- Clustering, k*NN
- Many methods for network construction

    [Enhanced construction of gene regulatory networks using hub gene information](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-017-1576-1)

    [GeNeCK: a web server for gene network construction and visualization](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2560-0)

- De-noise network before learning pathways network

    [Network enhancement as a general method to denoise weighted biological networks](https://www.nature.com/articles/s41467-018-05469-x)

    [](https://www.biorxiv.org/content/biorxiv/early/2019/09/26/527606.full.pdf)

## Learn regulatory pathways / direction of edges

- This is the hard part
- How to understand causality / assign direction to edges
- Bayesian framework?

    [](https://homes.cs.washington.edu/~suinlee/genome541/bayesnet-gene-regulation1.pdf)

- Cell state gene sets for parts of the cell cycle could give us some information about time / order of expression

    [Bayesian framework for the inference of gene regulatory networks from time and pseudo-time series data](https://academic.oup.com/bioinformatics/article/34/6/964/4222631)

    [BGRMI: A method for inferring gene regulatory networks from time-course gene expression data and its application in breast cancer research](https://www.nature.com/articles/srep37140)

- Graph Convolution Neural Networks

    [](https://arxiv.org/pdf/1901.00596.pdf)

- Probabilistic Boolean Networks

    [Probabilistic Boolean networks: a rule-based uncertainty model for gene regulatory networks](https://academic.oup.com/bioinformatics/article/18/2/261/225574/)

Networks should be scale free

## Cross Validate Network

[A closer look at cross-validation for assessing the accuracy of gene regulatory networks and models](https://www.nature.com/articles/s41598-018-24937-4)

- Evaluate with GO database

## Compare Networks

- Once pipeline is established, can run on different subsets of the data
- Disease vs. control
- Different cell types
- Different stages in development?
- Functional annotation with GO