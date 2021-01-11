# Experiment Design

## Phylogenetic Accuracy:

- RF distance between true tree and RAxML tree
- RF distance between true tree and TreeFix-VP tree
- RF distance between true tree and BEAST tree
    - Only did one but it's actually pretty garbage

## Transmission Network Accuracy

- RAxML tree → Phyloscanner → transmission network
- TreeFix-VP tree → Phyloscanner → transmission network
- BEAST tree → Phyloscanner → transmission network
- BEAST tree (w/ ancestral state reconstruction) → transmission network

    Compare networks by looking at FP, FN, TP edges

In all comparisons, but especially with BEAST, note execution time