import pandas as pd
a = pd.DataFrame(data=['negative', 'negative', 'negative', 'positive', 'positive'], columns=['target'])
# uniuqe() => np.array, tolist() => pyton list
print(a.target.unique().tolist())
