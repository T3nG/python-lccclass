import numpy as np
import pandas as pd


def c(x):
    return x*x


a = pd.DataFrame([1, 2, 3, 4, 5])

x = a.apply(lambda x:x*x)
y = a.apply(c)


print(x)
print(y)