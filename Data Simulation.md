# Data Simulation

**Network topology:** real world network (BarabasiAlbert), and complete network.

Real network models large outbreak, complete graph models small community outbreak.

**Seed Selection**: Single random seed.

**Seed sequence**: Taken from our real data, or random virus sequence. Length of sequence should be based on our real data.

**Transmission end criteria**: Number of transmissions or end time. If we want to use a more complex model (read - GEMF) for transmission sampling, we have to use end time

**Transmission sampling**: random single infection, random multi infection, and more realistic model such as SIER.

**Node evolution**: Birth death, virus tree simulator (coalescent model)

**Sequence evolution**: Are we doing seq-gen? Is there is a more appropriate model we can use?

Currently using seq-gen with the GTR Gamma model

**Source sample**: random edge of tree

**NumTimeSample**: Sampling just once per host.

**Time sample**: Have been using either end time or uniform/truncated normal distributions for sampling. Truncated Normal seems to give the best results

**NumBranchSample**: Sampling a fixed number - 10 or 5

**TreeUnit**: scale to make branch lengths similar to what is observed on real data - still should be refined

**NodeAvailability**: Perfect (all hosts on tree are available to be sampled)

**Sequencing error**: Doing perfect sequencing now, can introduce errors later.

[FAVITES: simultaneous simulation of transmission networks, phylogenetic trees, and sequences](https://www.biorxiv.org/content/early/2018/04/18/297267)