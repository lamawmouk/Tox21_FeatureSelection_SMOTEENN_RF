# Tox21_FeatureSelection_SMOTEENN_RF
This repository contains code accompanying the paper:
Identifying Protein Features and Pathways Responsible for Toxicity using Machine learning, CANDO, and Tox21 datasets: Implications for Predictive Toxicology
DOI:10.1101/2021.12.13.472455

In the  directory there are three folders containing the data curation files, feature generation files, and the model training files.

* In the Tox21_DataPreproccessing folder `Tox21_datacuration.ipynb`: This is used for data curation using the 12 Tox21 assays (labels of activity).
* In the Feautregeneration_using CANDO folder `Feature_generation_trainset.ipynb` and `Feature_generation_testset.ipynb`: These are used for feature generation for train and test datasets using the SMILES from Tox21 data.
* In the ModelTraining folder `Datapreprocessing_modeltraining.ipynb`: This is used to preproccess the features and labels and perfrom model training. The `train_utils.py` and `utilities.py` files are helper functions for model training. 
