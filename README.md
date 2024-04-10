# This assignment was for the Wolt Data Science internship, which was REJECTED with baseless reasoning.

### Reason 1: Pre-processing before doing the train-test split. For example, scaling the whole dataset and only then doing the train-test split.

**Response:** I fail to see any issue of data leakage here, as I have binned the data instead of standardizing it on a scale. The provided data remained within a determined range even for unseen data.

### Reason 2: Not addressing the time series aspects of the data. You cannot conduct a random split for testing and training sets with time series data if the aim is to predict the future.

**Response:** While the data is indeed in a time series format, the reviewer failed to recognize that:
1. The events are random, suggesting there may be no relation between t_1 and t_2.
2. Relevant time information is encoded into features such as hour and weekday, potentially making it safe to perform a random split now.

### Reason 3: Can you achieve similar or comparable performance with linear regression?

**Response:** The reviewer should have consulted the notebook where I evaluated the data using cross-correlation, revealing no indication of linear dependency. This suggests that a non-linear model should be explored instead of dwelling on linear regression.

### Reason 4: Selecting an overly complex model and overfitting.

**Response:** The applied model utilizes a simple 2-layer LSTM to capture non-linearity. I fail to comprehend how this could be perceived as overly complex by the reviewer. Overfitting is already mitigated through:
1. LSTM dropout
2. Cross-validation.

### Reason 5: Conducting light exploratory data analysis and relying solely on the model to interpret the data.

**Response:** The reviewer should revisit the notebook to review the exploration part. If n-fold cross-validation on a fully random split fails to establish trust, then there seems to be no limit to suspicion.

## Comments for the Reviewer:

- Data science should not be treated dogmatically; there are many nuances that the reviewer missed but was quick to dismiss with preconceived, condescending remarks.

---------------------------------------------------------------------------------------------------------------------

# Instructions:

- Navigate to the sandbox and locate the 'dp.ipynb' notebook for further exploration or to reproduce results.

# Requirements:

- Install the necessary requirements outlined in the requirements.txt file located in the root directory.
