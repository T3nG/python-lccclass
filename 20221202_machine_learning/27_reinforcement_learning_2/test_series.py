import numpy as np
import pandas as pd
actions = [0,1,2,3]

s = pd.Series(
    [0] * len(actions),
    index=actions,
    name='(0,0)'
)
print(s)
'''
0    0
1    0
2    0
3    0
Name: (0,0), dtype: int64
'''

print(pd.DataFrame(s))
'''
   (0,0)
0      0
1      0
2      0
3      0
'''

print(pd.DataFrame(s).T)
'''
       0  1  2  3
(0,0)  0  0  0  0
'''

table = pd.DataFrame(columns=actions, dtype=np.float64)
table = pd.concat([table, pd.DataFrame(s).T])
print(table)
'''
         0    1    2    3
(0,0)  0.0  0.0  0.0  0.0
'''