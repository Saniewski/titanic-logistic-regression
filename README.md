# Titanic Logistic Regression

A logistic regression model predicting the survival of the Titanic passengers.

Data comes from [Kaggle Titanic Competition Dataset](https://www.kaggle.com/c/titanic/data).

Notebooks feature a comparison of three models trained on differently imputed data (non-imputed, median imputed, and an imputation based on another, correlated feature).

## Description

The project contains the following files and directories:
* `data/` - directory containing data files (raw data and the output of the data processing),
  * `train.csv` - training dataset provided by Kaggle,
  * `test.csv` - testing dataset provided by Kaggle,
  * `train_not_imputed.csv` - processed training dataset with dropped rows containing missing `Age` value,
  * `train_median_imputed.csv` - processed training dataset with median imputation of the missing `Age` values,
  * `train_pclass_imputed.csv` - processed training dataset with missing `Age` values imputed by assigning the mean age of the corresponding socio-economic status,
* `requirements.txt` - file containing required python packages (install with `pip install -r requirements.txt`),
* `eda.ipynb` - exploratory data analysis (contains simple data visualizations),
* `eda_dash.py` - exploratory data analysis in the form of a dashboard,
* `data_preprocessing.ipynb` - turning raw training dataset into a processed dataset with each imputation method,
* `logistic_regression.ipynb` - train-valid split of the processed data, model training, validation, and comparison.
