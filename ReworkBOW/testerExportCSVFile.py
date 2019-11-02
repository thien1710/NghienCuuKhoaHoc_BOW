import csv

mydict = {'key1': 'value_a', 'key2': 'value_b', 'key3': 'value_c'}
import pandas as pd

df=pd.read_csv('./testerExportCSVFile.csv')
df2 = pd.DataFrame.from_dict(data=mydict, orient='index')
print(df)
print(df2)
print('*' * 30)
dfConCat = {}
for d in (df, df2): dfConCat.update(d)
print(dfConCat)
# (pd.DataFrame.from_dict(data=mydict, orient='index').to_csv('testerExportCSVFile.csv', header=False))
# df2.to_csv('testerExportCSVFile.csv', header=False)

# d1={1:2,3:4}
# d2={5:6,7:9}
# d3={10:8,13:22}
# d4 = {}
# for d in (d1, d2, d3): d4.update(d)
# print(d4)
