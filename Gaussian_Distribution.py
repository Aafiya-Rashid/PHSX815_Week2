import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(".")
from Random import Random

# function gaussian() defined in Random.py will returns gaussian random numbers distribution
mean = 0
standard_deviation = 2.5

x = Random.gaussian(mean, standard_deviation)
 
plt.hist(x, bins = 100, color = "c", density = True, edgecolor = 'k')
plt.grid(color = 'k', ls = 'dashed', lw = 0.75, alpha = 0.2)
plt.title("Gaussian Distribution")
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.savefig("Gaussian.pdf")
plt.show()
