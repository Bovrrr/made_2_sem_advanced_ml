import pandas as pd
import numpy as np
from datetime import timedelta, datetime

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import seaborn as sns


# фиксируем рандом сид на всякий случай
random_seed = 50
np.random.seed(random_seed)


def count_var(sample):
    var = sample @ sample.T / (sample.size - 1)
    return var


# Напишу ф-цию для подсчёта апостериорного распределения.
def count_posterior(prior, var, X, Y):
    default_mu, default_sigma = prior
    inv_default_sigma = np.linalg.inv(default_sigma)

    new_sigma = np.linalg.inv(inv_default_sigma + X.T @ X / var)
    new_mu = new_sigma @ (inv_default_sigma @ default_mu + X.T @ Y / var)

    return new_mu, new_sigma


third_march = datetime(2020, 3, 3)


def plot_month_distr(day_num, y_samp):
    plt.figure(figsize=(16, 9))
    plt.hist([y[day_num] for y in y_samp], bins=100)
    plt.grid("black")
    plt.show()
