SUBMISSION: 32
TITLE: Sequence-based prediction of protein-protein interactions: a structure-aware interpretable deep learning model


----------------------- REVIEW 1 ---------------------
SUBMISSION: 32
TITLE: Sequence-based prediction of protein-protein interactions: a structure-aware interpretable deep learning model
AUTHORS: Samuel Sledzieski, Rohit Singh, Lenore Cowen and Bonnie Berger

----------- Overall evaluation -----------
SCORE: 1 (weak accept)
----- TEXT:
The authors proposed a method, named D-SCRIPT, to predict the interfacial contact map of two query proteins as well as whether they interact physically. D-SCRIPT is a deep learning model, consisting of an LSTM model pre-trained by Bepler and Berger ICLR 2019, a 2D residual convolutional neural network, and two pooling layers. The authors proposed to predict the presence of physical interactions from estimated contact maps, which takes advantage of information from contact maps during training and obviates the need of 3D structures when predicting. The authors found their D-SCRIPT exhibits a smaller cross-species generalization error compared to PIPR (Chen et al. Bioinformatics 2019), at the cost of worse within-species performance. One main concern is that the D-SCRIPT algorithm should be further differentiated with the existing models. The comparisons to other related methods can also be much strengthened, and cross-species results can be better interpreted.

+++ Major comments +++

1. In Eq. 2-4, the authors proposed to use two methods to convert two 1D feature maps into a 2D feature map. However, the authors did not explain the rationale of choosing these two specific functions rather than simply concatenating the two vectors at each position of B as used in citation 28. This should be clearly clarified.

2. The authors used the Earth mover's distance to measure the performance of predicted contact maps. The Earth mover’s distance takes two probability distributions as input, but \hat C is not necessarily a probability distribution. In addition, the Earth mover's distance puts a smaller penalty when the predicted positions of interacting residues are wrong but close, compared to other common metrics. However, the accurate prediction of interacting amino acids is important, so it is necessary to show the performance under other metrics, such as BCE. Moreover, the authors should clarify if this phenomenon results from the use of the MAG loss.

3. The neural network that takes the contact map as input and predicts whether the two proteins interact is composed of two pooling layers and one 'truncation' layer. This neural network actually can be appended to any model that predicts contact maps or even more delicate 2D feature maps. If the prediction of contact maps is not satisfactory, why don't we append the two pooling layers to other pre-trained models, like the one in citation 28? This is not clear and the authors should clarify.

4. The authors claimed D-SCRIPT had a smaller generalization error when trained on human proteins and tested in five other species. However, the generalization is needed because the model fails to incorporate information from other species. It is therefore necessary to compare D-SCRIPT with models that are inherently able to adopt cross-species information, like any MSA-based models, including CCMpred, Complex Contact, and EVcoupling. These models predict contact maps or more features and can be used to substitute for the neural network prior to the last two pooling layers. When predicting, these MSA-based models only require sequences from other species, which are easy to obtain, but do not require any knowledge about their PPIs. This comparison would be fair because MSA-based models do not rely on additional and expensive information. I suggest the authors consider these additional evaluations.

5. The authors showed D-SCRIPT underperforms PIPR in human datasets but outperforms PIPR in other species absent in the training set, and concluded the D-SCRIPT is more generalizable. However, the difference in performance on human data sets is quite substantial. This is one major concern from the evaluation that the authors did not really address. It is necessary to eliminate the possibility that PIPR is overfitted to the training species. Besides, comparison of model complexities, such as the number of learnable parameters, are needed.

6. The authors compared D-SCRIPT, PIPR, and their combination. However, the improvement of the joint model is minor and not significant for most cases. When we use D-SCRIPT and PIPR, we usually know the taxonomy, so why don't we choose which single model to use based on the taxonomy of query proteins? This major concern is not addressed and the authors should clarify.

7. The authors used spectral clustering and DSD metric to detect community, and calculated the within-cluster similarity in terms of GO terms. It needs further clarification on what a larger within-cluster similarity implies and why it is preferable. Besides, the non-overlapping clustering is unnecessary in that the distribution of GO terms should be studied directly in the embedding space or the inferred PPI networks.

+++ Minor comments +++

1. The authors claimed to use the weighted average of BCE loss and MAG loss. However, the definition of the MAG loss is not clear. Additional citations or formulas are necessary. In particular, it needs to be explained why the MAG loss focuses on or leads to a few high probability interactions.

2. In the related work, other methods for predicting inter-protein contact maps need to be mentioned and cited, including Complex Contact, and EVcoupling.

3. It needs further explanation why the denominator in Eq. 7 includes an additional 1 instead of a small number.

4. Need to clarify if zero padding is used in the 2D convolutional neural network

5. W3 and b3 do not appear in Eq. 5. Very confusing.

6. How to choose the value of eta?

7. It seems the gamma in Eq. 6 is a learnable model parameter shared across all samples. Why don’t we estimate its value for each sample separately using an extra small neural network? Roughly, the number of interfacial interactions scales linearly in the lengths of the two proteins, so the fraction of nonzero values in Q is supposed to be a decreasing function of the 2D contact map’s size. If we assume values of P_ij are drawn from an isotropic normal distribution, gamma should be larger for longer proteins in order to keep the number of nonzero elements in Q linear in the sum of protein lengths rather than linear in their product.



----------------------- REVIEW 2 ---------------------
SUBMISSION: 32
TITLE: Sequence-based prediction of protein-protein interactions: a structure-aware interpretable deep learning model
AUTHORS: Samuel Sledzieski, Rohit Singh, Lenore Cowen and Bonnie Berger

----------- Overall evaluation -----------
SCORE: 2 (accept)
----- TEXT:
The authors developed a deep-learning method, D-SCRIPT, to predict a physical interaction between two proteins based on their sequences only. It aims to predict (contact) amino acids involved in the interaction. It starts with pre-trained protein embeddings (based on the group’s earlier model), performs dimension reduction for each protein embedding, computes a representation of interaction for each pair of residues, and then tries to capture local structural information via two filters resulting in the contact prediction matrix and the interaction probability. It does not perform well in a within-species evaluation, even when compared with the naive method. Although, it improves significantly when only infrequent interacting proteins are considered (a harder task). However, the main strength of the methods lies in the cross-species prediction of PPI where it was trained on human data and evaluated in other species for which there is little PPI experimental data. Then, it significantly outperforms other methods.

Overall the manuscript is well written and presents an interesting advancement in PPI prediction. The significance and novelty of the study lie in allowing the transfer of information from human PPI to less-studied species based on protein sequence only (no structural information was used). Moreover, the model is interpretable and allows to extract additional knowledge captured by the model.

Remarks:

1. Page 5, Eq. 5: The W_3 weights and b_3 biases are missing in Eq. 5.

2. Figure 4: Does the performance of each embedding type depend on its dimensionality? D-SCRIPT is a 100-dimensional embedding, AAClass - 7, Vec5 - 5, PIPR - 12 (a combination of AAClass and Vec5). Is Random 50- or 100-dimensional embedding? How was it generated?

3. Table 1: The table suggests that there is only one hybrid method, while the authors used two different hybrid methods: one for human data (PIPR enhanced by D-SCRIPT) and another for other species (D-SCRIPT enhanced by PIPR). It should be clarified and different names/labels should be used. The same applies to Table A.1

4. Figure 2: It might help in following the model if you label the matrices with their names (Z, B, C, etc). It will make it easier to identify the parts of the model.

5. Page 3: “to to” -> “to”

6. Page 16: Please provide a citation for “the precedent of previous work”.



----------------------- REVIEW 3 ---------------------
SUBMISSION: 32
TITLE: Sequence-based prediction of protein-protein interactions: a structure-aware interpretable deep learning model
AUTHORS: Samuel Sledzieski, Rohit Singh, Lenore Cowen and Bonnie Berger

----------- Overall evaluation -----------
SCORE: 2 (accept)
----- TEXT:
In this paper, the authors introduce a deep learning approach to predict protein-protein physical interactions based on protein sequence data.  The approach D-SCRIPT uses a pretrained protein embedding along with intermediate layers that is physically motivated and encapsulates inter-protein contacts. D-SCRIPT is trained on human PPI data and evaluated in cross-validation on human data, as well as on predicted PPIs in 5 other model organisms. The approach compares favorably in predicting PPIs to a previous published approach, PIPR, and it is shown that the large-scale prediction of PPIs in D. melanogaster followed by module detection yields functionally coherent sets.   Additionally D-SCRIPT was tested with respect to how well its residue contact model predicts inter-protein contacts, and applied to predict SARS-CoV-2 interactions with human proteins. 

The authors should clarify what the previous PIPR method was trained on- is it possible the previous PIPR method trains on some of the data that it is tested on here? If so, the relative performance of  the newly described method, D-SCRIPT, over PIPR would actually improve in a more fair testing.    The  performance of D-SCRIPT is fairly consistent across organisms (i.e., comparing cross-validation performance in human vs. other organisms), suggesting that the approach generalizes well, though more information about how sequence similarity between human protein interactions and other organisms was dealt with should also be better explained.

Overall, this is an interesting approach with a physically motivated NN model on an important problem.