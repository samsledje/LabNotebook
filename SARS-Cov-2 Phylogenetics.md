# SARS-Cov-2 Phylogenetics

[Dropbox](https://www.dropbox.com/sh/pffc8guf9uvb4ox/AACiWBY9YgaFyRTbOgUXGdkLa?dl=0)

### Software

[TreeTime](https://github.com/neherlab/treetime)

[iTOL](https://itol.embl.de/upload.cgi)

### Literature

[[Reading List#Species Tree Estimation]]

[[Fast and accurate branch lengths estimation for phylogenomic trees]]

[A new coronavirus associated with human respiratory disease in China - Wu](s41586-020-2008-3)

[[The proximal origin of SARS-CoV-2 - Andersen]]

[SARS-CoV-2 Human PPI](2020.03.22.002386v1.full)

[[Evolutionary origins of the SARS-CoV-2 sarbecovirus lineage responsible for the COVID-19 pandemic]]

[[Evolutionary Insights into the Ecology of Coronaviruses]]

### Kellis Resources

[[SARS-CoV-2 PhyloCSF - Google Docs]]

### TODO

[[Research Tasks]]

- Sliding window construct alignments with muscle / MAFFT
    - Window size, jump
    - Slide windows 1000, jump 500bp
    - Along entire sequence or just in areas of interest
    - Include MERS in alignment
- Construct phylogenies
    - Whole genome phylogeny
    - RAxML with fast bootstrapping
    - raxmlHPC -m GTRGAMMA -s <codonalignment> -n <outputfile> -p 1
    - Settle on list of species
        - New random bat genomes, pangolin, civet cats, outgroup
        - 100 best bat hits, choose some number randomly with low e-value to capture diversity of bat covid genomes
- Root phylogenies
    - Outgroup - SARS / KY352407
    - MAD rooting
    - RAxML midpoint rooting
- Error Correction
    - TreeFix-DTL
    - TreeSolve
- TreeTime rescaling and rate estimation
    - Re-estimate branch lengths with RAxML
    - TreeTime units are years - what are rates??
    - Supposed recombination breakpoints
    - Entire genome alignment
- DTL reconciliation with
    - Neighboring trees
    - Genome tree
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

### Misc Notes

- Potential recombination breakpoints
    - ~ 12k nucleotides
    - 13 522, 23 686
    - ~11 000 - ~13 000

[[Natural Selection Analysis   COVID-19 analysis on usegalaxy.]]