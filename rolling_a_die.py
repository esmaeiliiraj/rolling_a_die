# Code is written in Python!

import numpy as np
import scipy
import matplotlib.pyplot as plt

# Tune the sample size to see when the probablility of each event converges to 1/6 = 16.6%
s = np.random.randint(1, high=7, size=1000)

# The first line is written differen just for the sake of showing a different way of writing the program
e = [[i==1 for i in s].count(True),
len(s[s==2]),
len(s[s==3]),
len(s[s==4]),
len(s[s==5]),
len(s[s==6])]

for i in range(6):
    prob = e[i] / len(s) * 100
    print(f'Probability of e{i+1} is {prob:.2f} %')
