import numpy as np
from sklearn.model_selection import train_test_split

def minute_error(true_minutes, pred_minutes):
    true_minutes = np.array(true_minutes)
    pred_minutes = np.array(pred_minutes)
    abs_diff = np.abs(true_minutes - pred_minutes)
    return np.mean(abs_diff)

def f1_score(true_minutes, pred_minutes, threshold=2.0):
    """
    Calculate the F1 score between true and predicted minutes.
    
    Parameters:
        true_minutes (array-like): True minutes.
        pred_minutes (array-like): Predicted minutes.
        threshold (float, optional): Threshold for considering a prediction correct or incorrect.
        
    Returns:
        f1 (float): The F1 score between true and predicted minutes.
    """
    true_positive = 0
    false_positive = 0
    false_negative = 0

    for true, pred in zip(true_minutes, pred_minutes):
        if abs(true - pred) <= threshold:
            true_positive += 1
        elif true < pred:
            false_positive += 1
        else:
            false_negative += 1

    precision = true_positive / (true_positive + false_positive + 1e-10)
    recall = true_positive / (true_positive + false_negative + 1e-10)

    f1 = 2 * (precision * recall) / (precision + recall + 1e-10)

    return f1, precision, recall

def percentage_outliers(differences):
    Q1 = np.percentile(differences, 25)
    Q3 = np.percentile(differences, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = differences[(differences < lower_bound) | (differences > upper_bound)]
    outliers_percentage = len(outliers) / len(differences) * 100
    return outliers_percentage

from sklearn.model_selection import train_test_split

def splited_indices(X, y, num_splits=5, test_size=0.2):
    num_samples = len(X)
    assert num_samples == len(y)
    test_samples = int(num_samples * test_size)
    splits_indices = []
    for _ in range(num_splits):
        shuffled_indexes = np.random.permutation(num_samples)
        val_idx = shuffled_indexes[:test_samples]
        train_idx = shuffled_indexes[test_samples:]
        splits_indices.append((train_idx, val_idx))
    return splits_indices

def divisors(number):
    '''
    select timestamp
    '''
    common_divisors = []
    for i in range(1, number + 1):
        if number % i == 0:  
            common_divisors.append(i)
    return common_divisors