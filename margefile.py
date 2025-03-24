import pandas as pd
data = pd.read_csv('/home/ayush-kurmi/Desktop/python/numpy/customers-10000.csv')
dict_dta = {}
for index , row in data.iterrows():
    # print(index,row)
    name = row['First Name']
    filename = f"{name}.csv"
    if name in dict_dta:
        
        dict_dta[name].append(row.to_dict())
    else:
        
        dict_dta[name] = [row.to_dict()]
        
        

print(dict_dta)