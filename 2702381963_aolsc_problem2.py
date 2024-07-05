# -*- coding: utf-8 -*-
"""2702381963_AOLSC_Problem2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15EDn8QwsiIpWwKHg_bLfTbD9NYy4AlHj

Problem 2
"""

import pandas as pd

data = pd.read_excel(r"/content/AOLScientificComputing.xlsx")
data.head()

import numpy as np
import matplotlib.pyplot as plt

production_data = data.values.flatten()

months = np.arange(1, len(production_data) + 1)

coefficients = np.polyfit(months, production_data, 3)

x = np.linspace(1, len(production_data), len(production_data))

taylor = np.polyval(coefficients, months)

plt.figure(figsize=(12, 6))
plt.plot(months, production_data, label='Monthly Production', marker='o')
plt.plot(months, taylor, label='Taylor', color = 'red')
plt.xlabel('Month')
plt.ylabel('Production')
plt.title('Taylor Series (Approximation)')
plt.legend()
plt.grid(True)
plt.show()