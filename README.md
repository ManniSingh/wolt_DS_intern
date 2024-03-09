# REJECTED

### Pre-processing before doing train-test split. For example scaling the whole data set and only then doing the train-test split.

**Response:** I don't see any issue of data leakage here, as I have binned the data instead of standardizing it on a scale. The provided data was within a determined range even for the unseen data.

### Not dealing with the time series aspects of time series. You cannot do a random split to test and train sets with a time series if you intend to predict the future.

**Response:** Yes, the data is in time series. However, the reviewer failed to recognize that:
1. The events are random, so it is likely that there is no relation between t_1 and t_2.
2. The relevant time information is encoded into features such as hour and weekday, making it potentially safe to randomly split now.

### Can you get similar or comparable performance with linear regression?

**Response:** The reviewer should have checked the notebook where I have already evaluated the data on cross-correlation, and there is no indication of linear dependency. This suggests that a non-linear model should be tried instead of beating around the bush.

### Selecting overly complex model and overfitting

**Response:** The applied model uses a simple 2-layer LSTM to capture non-linearity. I have no idea how it is complex to the reviewer. Overfitting is already mitigated with:
1. LSTM dropout
2. cross-validation.

### Doing a light exploratory data analysis and trusting the model to make sense of your data

**Response:** The reviewer should check the notebook again to see the exploration part. If n-fold cross-validation on a fully random split can't establish trust, then there is no limit to suspicion.

## Comments for the reviewer

- Data science is not a religion; you should not have strict slot fillings. There are many nuances that the reviewer missed but was quick to give pre-conceived condescending remarks.

---------------------------------------------------------------------------------------------------------------------

# Instructions

- Go to the sandbox and find the 'dp.ipynb' notebook to explore or reproduce results.

# Requirements

- The requirements that may be installed are in the requirements.txt file in the root.
