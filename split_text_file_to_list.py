from pandas import DataFrame
keys = ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4']
values = [22000,25000,27000,35000]
dic = {'Car': keys}
print(dic)
dic.update({'Price': values})
print(dic)

df = DataFrame(dic, columns= ['Car', 'Price'])

export_csv = df.to_csv ('export_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path

print (df)