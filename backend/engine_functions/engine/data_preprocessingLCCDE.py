import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def split_data(dataset, test_size=0.2, random_state=0):
    """
    Splits the data into training and testing sets.

    Parameters:
    - df: pandas.DataFrame, the dataframe to split.
    - target_column: str, the name of the target variable column.
    - train_size: float, the proportion of the dataset to include in the train split.
    - test_size: float, the proportion of the dataset to include in the test split.
    - random_state: int, the seed used by the random number generator.

    Returns:
    - X_train: pandas.DataFrame, the training feature set.
    - X_test: pandas.DataFrame, the testing feature set.
    - y_train: pandas.Series, the training target variable.
    - y_test: pandas.Series, the testing target variable.
    """
    df = pd.read_csv("./engine_functions/engine/data/CICIDS2017_sample_km.csv")
    train_size = 1 - test_size
    X = df.drop(['Label'], axis=1)
    y = df['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def apply_smote(X_train, y_train, sampling_strat2=1000, sampling_strat4=1000):
    """
    Applies SMOTE to the training set to handle class imbalance.

    Parameters:
    - X_train: pandas.DataFrame, the training feature set before SMOTE.
    - y_train: pandas.Series, the training target variable before SMOTE.
    - sampling_strategy: dict, the sampling strategy to use for SMOTE.
    - n_jobs: int, the number of parallel jobs to run for SMOTE.

    Returns:
    - X_train_smote: pandas.DataFrame, the training feature set after SMOTE.
    - y_train_smote: pandas.Series, the training target variable after SMOTE.
    """
    sampling_strategy={2:sampling_strat2, 4:sampling_strat4}
    smote = SMOTE(n_jobs=-1, sampling_strategy=sampling_strategy)
    X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
    return X_train_smote, y_train_smote