[[RECOMB Reviews Raw]]
[[List of updates made for DSCRIPT bioRxiv]]

### Minor Writing
- [x] Justify [multiplication | absolute difference] over concatentation -- cite Bepler&Berger for this -- From Bepler&Berger -> "We choose this featurization because it is symmetric, vij = vji, and has shown widespread utility for pairwise comparison models in NLP [36]"
- [x] Comparison of model complexities - # learnable parameters
    - Majority of weights in projection layer <<6165, rest is very small (200 -> 50, 7*7*50 -> 1)
    - [x] Discussion of how our method guards against overfitting
        - Dropout, simple model, magnitude regularization
- [x] Clarify what the MAG loss is (magnitude of contact map). Explain how regularization leads to a few high probability interactions
- [x] Eq 5 - remove $W_3$, $b_3$ from text, or add them to the equation instead of just "Conv"
- [ ] Eq 7 - Why using pseudocount instead of small epsilon
- [x] Clarify 0 padding used for 2D conv net
- [x] Justification of choosing $\eta$ - leads to very steep sigmoid
- [x] Fig 4 - Clarify impact of embedding dimension on performance - clarify size of random embedding and how it was generated
- [x] Page 3 "to to" -> "to"
- [x] Page 16 - Cite previous work for how we did train/test split
- [x] Clarify what PIPR was trained on? I thought it was pretty obvious that we trained both on human PPIs
- [ ] What does it mean to have a high within-cluster similarity? Why is it preferable?


### Major Writing
- [ ] Add supplement explaining with BCE is not the best evaluation method for these contact maps - we do pooling so lose resolution, goal is not to get exactly right b/c cutoff sensitivity
- [ ]  Why train end to end, instead of pooling layers on top of pre-trained contact map prediction, such as [\[28\]](https://pubmed.ncbi.nlm.nih.gov/29275173/)
    - [ ] Cite ComplexContact / EVcoupling
    - Data is maybe not as available for contact map prediction - have more data for interaction than contacts
    - In distant species, evolutionary approaches are more dificult
        - Detecting co-evolution requires assumptions about phylogeny & alignment, which we avoid being purely sequence based
        - Many methods won't find a good MSA
        - Can do in silico mutational study if it is entirely end-to-end
    - Answers that question "Do they interact, and if so how" rather than "We assume they interact, how"

### Additional Experiments
- [ ] [[Compare performance with MSA based models]], including [[Complex Contact Xu]],  [EVcoupling](https://github.com/debbiemarkslab/EVcouplings), [EVcomplex](https://elifesciences.org/articles/03430), **[[Gremlin-Complex Baker]]**
    - Try for something like E. Coli, S. Cerevisiae
    - What do these methods do for proteins that don't interact? If they still try to make a guess --> you can't do pooling on that
- [ ] "Distribution of GO terms should be studied directly in the embedding space or the inferred PPI networks"
    - Compute distribution as: for every pair of protein compute distance as {distance in network | GLIDE distance | node2vec distance } then see correlation between distance and Jaccard similarity of protein GO sets
- [ ] Evaluate inter-protein contact maps using BCE or other metric

### Optional Experiments
- [ ] Does the performance of an embedding depend on its dimensionality?
- [ ] Eq 6 - Why not estimate value of $\gamma$ for each sample, maybe with a small NN - # of contacts should be decreasing function of contact map size