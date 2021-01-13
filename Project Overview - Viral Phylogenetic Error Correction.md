# Project Overview - Viral Phylogenetic Error Correction

## Overall experimental study design:

- Want to simulate networks and trees that are as “real” as possible, with a large number of infections and several sequences sampled from each infection.
- Want to compare trees reconstructed using TreeFix-VP with trees reconstructed using RAxML and BEAST and show that TreeFix-VP trees are more similar to the true trees.

## Current Experimental Observations:

1. TreeFix-VP makes biggest difference when there are lots of transmissions. This is because TreeFix-VP has no way to “improve” the topology of the subtree that evolves inside any single host.
2. TreeFix-VP performs better with more iterations. Default is 1000, but going up to 5000 may give significant improvements.
3. TreeFix-VP should be scalable up to around 300-400 sequences (analysis finishes within few hours or couple of days).
4. Need fairly long sequences for any phylogenetic resolution.

## Simulation challenges and ideas for their resolution:

1. Simulating using a more realistic model such as SEIR.

*Ideas for resolution*: Experiment to find suitable parameters so that transmission network size is within the range we want.

1. Use a more real network, such as a real world network (BarabasiAlbert), instead of a clique.

*Ideas for resolution:* try out different types of networks.

1. Preventing long branches that seperate transmission events.

*Ideas for resolution*: Find suitable parameters for coalescent model. Sample after fixed amount of time from host infection, rather than at the end of simulation. Use birth-death model instead of coalescent model.

1. Finding a good measure to assess the improvement obtained by using TreeFix-VP compared to using RAxML trees and BEAST trees.

*Ideas for resolution*: Can run transmission inference approach such as Hall’s method (Beastlier) or phyloscanner on reconstructed trees and measure accuracy of inferred transmission network. Can also come up with a new and more suitable distance measure to compute distance between true tree and reconstructed trees.How long should sequences be and with what mutation rate?

1. Accounting for the effect of things such as sequence length, tree height (mutation rate), transmission model, number of TreeFix-VP iterations, number of sampled sequences per host, sequencing of hosts after fixed time from infection or all together at the end.

*Ideas for resolution:* Just need more experiments.