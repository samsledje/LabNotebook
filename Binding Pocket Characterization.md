# Find Color Motifs in Interaction Networks

This ties in with [[D-SCRIPT Embedding UMAP]]

## Protein Structure Landscape Research
- [x] [SCOP](http://scop.mrc-lmb.cam.ac.uk/)
- [x] [[Kolodny_Global_View_Of_Protein_Universe.pdf]]
- [x] [[Kolodny_Protein_Interface_Similarity.pdf]]
- [x] [[Edwards_Structural_Bridging_Fold_Space.PDF]]
- [ ] [[Yu_Berger_Entropy_Scaling_Search.pdf]]
- [ ] [[Osadchy_Kolodny_Maps_of_protein_structure.pdf]]

## Rohit Email Ideas
1. A protein’s 3D binding interface is a meaningful, conserved entity: if A and B interact, and you define A’s neighbors based on binding pocket structural similarity (and ditto for B), these neighbors are likely to interact. This is similar to our knn analysis, as Sam was mentioning. 
2. Of the 4 SCOP classes (alpha, beta, alpha/beta, alpha+beta), the alpha/beta class shows the most continuity in structural variation. It is also the class where nearby structures have the greatest risk of being functionally different (function as annotated by GO terms).

For #1 above, I don’t think there’s a binding-pocket classification we can directly use for our method-- we’d need to build it ourselves **(clustering Kolodny embeddings)**. They demonstrated only a proof of concept in the [[Kolodny_Protein_Interface_Similarity.pdf |  2018 Paper]]

Not all of these directly build upon our PPI work, but they do use similar thinking. Below, I sketch out some ideas that might be interesting. I’m not saying we should do these-- they are intended just as a starting point for future discussion.

### PPI prediction
We start from the [[D-SCRIPT]] n-x-100 dimensional embedding and extract from it the subspace that corresponds to a protein’s binding pocket structure. One way to do this will be to train a Siamese network structure: training on the set of PDB structures with known binding interfaces, pass two sequences through identical models (shared parameters) that each reduce the D-SCRIPT n-x-100 embedding to a k-dimensional vector. We then compute the dot-product of these vectors, using that as a measure of similarity between the proteins and supervising the measure with the ground-truth structural similarity of the two binding pockets (calculated by distance between vectors from [[Kolodny_Protein_Interface_Similarity.pdf | PatchBag]]. At the end of training, the k-dimensional embedding will capture the binding pocket characteristics of a protein, **and we can perform clustering on these k-dimensional vectors**; this would be similar to node “color” as we’ve talked about. We’d use this information with a [[D-SCRIPT + Glide | graph theoretic method]] and/or use it to [[D-SCRIPT with Attention | make D-SCRIPT’s model better]]. 

Binding Pocket characterization is useful beyond PPI - classifying cell surface receptors based on binding pocket type

Existing PPI networks - classify all interactions, look for patterns

How do PatchBag distances correlate with random walk distances in the PPI network?

After we _recover_ patch bag clusters, can we _improve_ clusters to be more biologically meaningful -- network coloring

### Link prediction and functional annotation:
#1 above implies that there are a set of protein structures for which the structure->function relationship is less tight than for others. Our pretrained embedding can be used to identify these proteins **(how? where do we get known function?)** (e.g. by supervising against SCOP classes of known PDB structures). Eventually, we’d produce a per-protein score suggesting how tightly linked its structure and function are. **We could then propose and test a hypothesis that regions of the network populated by proteins with low scores respond less well to link or function prediction algorithms.**

#### Remote #homology estimation
As an extension of this idea, we’d propose and test the hypothesis that homology estimation across distant species works poorly for proteins with low scores. 

#### PPI prediction in a new species
We’d use these per-protein scores to establish a confidence estimate for D-SCRIPT predictions on a new species. In low confidence cases, we’d trust graph-theoretic methods more; elsewhere, we’d stick with the D-SCRIPT prediction. 

An interesting extension would be to use the concept of **function**, as encoded in the PPI network, to directly produce this per-protein score. We’d use it to confirm Kolodny et al.’s point #1 above and also explore the score’s use in other contexts. 

# Data
https://www.atom3d.ai/
Vreven Docking Benchmark data set
