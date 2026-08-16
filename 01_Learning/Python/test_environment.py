import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print("=" * 40)
print("AI Learning Environment Test")
print("=" * 40)

print("\nPython:")
print(sys.version)

print("\nPython Path:")
print(sys.executable)

print("\nPackages:")
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Scikit-learn:", sklearn.__version__)

a = np.array([1, 2, 3, 4, 5])

print("\nNumPy Test:")
print("Array:", a)
print("Mean:", a.mean())

print("\nEnvironment test PASS!")
scores = np.array([85, 92, 76, 88, 95])

print("Scores:", scores)
print("Average:", scores.mean())
print("Highest:", scores.max())
print("Lowest:", scores.min())