# SARS-Cov-2 Phylogenetics

[Dropbox](https://www.dropbox.com/sh/pffc8guf9uvb4ox/AACiWBY9YgaFyRTbOgUXGdkLa?dl=0)

## Software

[TreeTime](https://github.com/neherlab/treetime)

[iTOL](https://itol.embl.de/upload.cgi)

## Literature

[[Reading List#Species Tree Estimation]]

[[Fast and accurate branch lengths estimation for phylogenomic trees]]

[A new coronavirus associated with human respiratory disease in China - Wu](https://pubmed.ncbi.nlm.nih.gov/32015508/)

[[The proximal origin of SARS-CoV-2 - Andersen]]

[SARS-CoV-2 Human PPI](2020.03.22.002386v1.full)

[[Evolutionary origins of the SARS-CoV-2 sarbecovirus lineage responsible for the COVID-19 pandemic]]

[[Evolutionary Insights into the Ecology of Coronaviruses]]

## Kellis Resources

[[SARS-CoV-2 PhyloCSF - Google Docs]]

## Methods

### Species Tree Reconstruction
- How species were chosen
    - Check Irwin for how he selected the 44
    - Added pangolins for SARS-CoV-2, Added civet for SARS
- BEAST of whole genome, NRR A, NRR B
    - GTR + $\Gamma$
    - Uncorrelated relaxed clock with lognormal distribution, informative rate prior

### Gene Family Recombination
- Genes were either annotated or known annotations were aligned to species with unknown annotations
- Align with Muscle
- RAxML constructs unrooted gene tree (GTR + $\Gamma$, 100 rapid bootstraps)
- Error correct with TreeFix-DTL (10x) (default parameters) -- use NRR B as species tree
- (If doing MAD rooting) -- Optimize branch lengths with RAxML
- Root with OptRoot (default parameters) (or MAD rooting)
- For each TreeFix tree - run Ranger-DTL (100x) (default parameters) -- use NRR B as species tree
- For each gene family, 1000 "bootstrap" reconciliations

### Rates Analysis

## Results


## To Do
[[Research Tasks]]

- TreeTime rescaling and rate estimation
    - Re-estimate branch lengths with RAxML
    - TreeTime units are years - what are rates??
    - Supposed recombination breakpoints
    - Entire genome alignment

## Misc Notes
    
- Look for transfers from Aggregate Ranger

    ```bash
    for i in $(ls data_proc);
    do
    	cat data_proc/$i/sars_rooted/RangerDTL_bootstraps/RangerDTL.$i.sars_rooted.speciesReconciliation.agg | sed -n 's/^.*\(Transfers = [[:digit:]]*\).*mapping --> \(n[[:digit:]]*\), .*recipient --> \(n.*\),.*$/\2 --> \3 [\1]/p';
    done
    ```

- Look for transfers from normal Ranger out file

    ```bash
    for i in $(ls data_proc);
    do
    	cat data_proc/$i/sars_rooted/RangerDTL_bootstraps/RangerDTL.$i.sars_rooted.speciesReconciliation.out.boot* | sed -n 's/^.*\(m49\).*Transfer.*Recipient\( --> .*\).*$/\1 \2/p';
    done
    ```


- Potential recombination breakpoints
    - ~ 12k nucleotides
    - 13 522, 23 686
    - ~11 000 - ~13 000

[[Natural Selection Analysis   COVID-19 analysis on usegalaxy.]]