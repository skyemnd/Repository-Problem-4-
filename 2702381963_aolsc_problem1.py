# -*- coding: utf-8 -*-
"""2702381963_AOLSC_Problem1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cz3DAKS3BcSP7MkPQbLwHDPZuaXewKi2

Problem 1
"""

import pandas as pd

data = pd.read_excel(r"/content/AOLScientificComputing.xlsx")
data.head()

import numpy as np
import matplotlib.pyplot as plt

production_data = data.values.flatten()

months = np.arange(1, len(production_data) + 1)

plt.figure(figsize=(12, 6))
plt.plot(months, production_data, label='Monthly Production', marker='o')
plt.xlabel('Month')
plt.ylabel('Production')
plt.title('Monthly Bag Production (Jan 2018 - Dec 2023)')
plt.legend()
plt.grid(True)
plt.show()

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

months_reshaped = months.reshape(-1, 1)

poly_features = PolynomialFeatures(degree=3)
months_poly = poly_features.fit_transform(months_reshaped)

poly_model = LinearRegression()
poly_model.fit(months_poly, production_data)

production_pred = poly_model.predict(months_poly)

plt.figure(figsize=(12, 6))
plt.plot(months, production_data, label='Monthly Production', marker='o')
plt.plot(months, production_pred, label='Polynomial Trend (Degree 3)', color='red')
plt.xlabel('Month')
plt.ylabel('Production')
plt.title('Monthly Bag Production with Polynomial Trend (Jan 2018 - Dec 2023)')
plt.legend()
plt.grid(True)
plt.show()