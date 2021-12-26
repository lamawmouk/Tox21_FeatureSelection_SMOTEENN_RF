# Tox21_FeatureSelection_SMOTEENN_RF
This repository contains code accompanying the paper:
Identifying Protein Features and Pathways Responsible for Toxicity using Machine learning, CANDO, and Tox21 datasets: Implications for Predictive Toxicology
DOI:10.1101/2021.12.13.472455

In the  directory there are three folders containing the data curation files, feature generation files, and the model training files.

* In the Tox21_DataPreproccessing `Tox21_datacuration.ipynb`: Data curation script using the 12 Tox21 assays (labels of activity).
* In the Feautregeneration_using CANDO `Feature_generation_trainset.ipynb` and `Feature_generation_testset.ipynb`: Feature generation scripts for train and test datasets using the SMILES from Tox21 data.
* In the ModelTraining `Datapreprocessing_modeltraining.ipynb`: Data wrangling and model training. The `train_utils.py` and 'utilities.py' files are helper functions for model training. 
