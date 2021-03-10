 [[Kolodny_Protein_Interface_Similarity.pdf]]
 
 Consider surface patches of `n=4,5,6` residues, where a patch has `n` C-alpha atoms
 Consider only pairs of proteins where both interfaces are larger than 15 residues
 
 - 3DID file has all domain/domain interactions
 - Filter 80% sequence identity with CD-HIT, take sequences longer than 50, where both interfaces are larger than 15 residues
 - Convert these domains/interfaces into .inter format for PatchBag
 - GIVEN these domains/interfaces, map back to PDB ID/chain and grab the sequence in those domains
 - Embed using D-SCRIPT

1. Run DSSP on PDB file
2. Residues with >20% accessibility are on the surface
    **NOTE** Divide accessibility by maximum accessibility, we DO NOT know maximum accessibility for [SEC, PYL, UNK](https://www.genome.jp/kegg/catalog/codes1.html)
3. Create interface file with X-CA Y-CA Z-CA, Prop0, Prop1, Residue #, Interface(0/1)
```
ls ~/db/pdb_STRING/ | grep pdb | parallel --eta 'bash extractInterfaceFileFromPDB.sh {.}.pdb ~/db/pdb_STRING/ ~/db/pdb_STRING/interfaces 15'
```

5. Compute patchBag of interface file
    Can launch MATLAB in cmd line only with -nojvm

```
[ PatchBagMatrix ] = createPatchbag(6, 50, '/afs/csail/u/s/samsl/Work/Interface_Prediction/vreven_interfaces/', 1, 3, 0, 'inter', 'R')
```