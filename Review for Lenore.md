    [Bioinformatics](https://mc.manuscriptcentral.com/bioinformatics) 
[[PAX2GRAPHML_Applications_Note.pdf]]

## Installation

 - Difficulty running notebook/building container -- would be better to have a `pip` or `conda` install, with requirements of Python3 and graph-tool (Java for sub-modules)
 - Should edit jupyter launch code with `-e PASSWORD=password`, because it is required to get into the jupyter lab -- or else make it clear somewhere that the password is "password"
 - Don't have access to data even with notebook
     - THIS IS IMPORTANT -- on an AFS filesystem, chmod won't do it -- should include directions to copy data into the container using `docker cp`
 - pax2graphml/run.sh should specify `fjrmore/pax2graphml`
 - building from src/install.sh crashes python silently
- pax2graphmlenv does not work at all -- can't build locally or run because does not exist on DockerHub

### Notebooks
- In notebook 1 (and subsequent) -- `rootPath`  in [2] should point to `/home/user/data` if data folder is copied in
- In notebook 2.2 -- Was not packaged with `annot/annot_node_index.csv` and `annot/annot_edge_index.csv` files which seem to be required

### Software Notes
- Maybe a verbose option for a few functions that don't return anything would be good - i.e. pax_import.join_annotation, graph_explore.save_graphml -- some sort of confirmation that something has happened -- similar to the "response" messaage given in [2] of notebook 4