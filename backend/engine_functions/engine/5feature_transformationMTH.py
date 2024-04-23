from sklearn.kernel_approximation import Nystroem
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import pandas as pd

def apply_kernel_approximation(X, n_components=10, kernel='rbf', gamma=0.1):
    """
    Apply the Nystroem method for kernel approximation to transform features.
    """
    nystroem = Nystroem(n_components=n_components, kernel=kernel, gamma=gamma)
    nystroem.fit(X)
    X_transformed = nystroem.transform(X)
    return X_transformed

def split_data(X, y, split_index):
    """
    Split data into training and testing sets based on a given index.
    """
    X_train = X[:split_index]
    y_train = y[:split_index]
    X_test = X[split_index:]
    y_test = y[split_index:]
    return X_train, y_train, X_test, y_test

def address_class_imbalance(X_train, y_train, strategy_dict):
    """
    Use SMOTE to address class imbalance in the training data.
    """
    smote = SMOTE(n_jobs=-1, sampling_strategy=strategy_dict)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    return X_train_resampled, y_train_resampled

def preprocess_data(X_fss, y, split_index, strategy_dict):
    """
    Process data by applying feature transformation, splitting data,
    and addressing class imbalance.
    """
    # Apply Nystroem kernel approximation
    X_kpca = apply_kernel_approximation(X_fss)
    
    # Split data into train and test sets
    X_train, y_train, X_test, y_test = split_data(X_kpca, y, split_index)
    
    # Display class distribution before SMOTE
    print("Class distribution before SMOTE:", pd.Series(y_train).value_counts())
    
    # Address class imbalance with SMOTE
    X_train, y_train = address_class_imbalance(X_train, y_train, strategy_dict)
    
    # Display class distribution after SMOTE
    print("Class distribution after SMOTE:", pd.Series(y_train).value_counts())
    print("Test set class distribution:", pd.Series(y_test).value_counts())
    
    return X_train, y_train, X_test, y_test
