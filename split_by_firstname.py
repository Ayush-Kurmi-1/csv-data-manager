import pandas as pd
import csv
def randomDataDevideFile( path,based):
    data = pd.read_csv(path)  # read the document
    unique_data = data["First Name"].unique() # unique name nikale
    row_dict = {}  # empty dict create kari
    for index,single_row in data.iterrows():  # for loop lagaya in data per jis se single row nikali  # iterrow means ek ek row nikalna
        name = single_row[based]    # kis base pe data devide kerna hai 

        if name in row_dict :  #  dict me check kerna hai ki bah name hai ki nahi
            row_dict[name].append(single_row.to_dict())  # hai to us row ko us name bale key ki value  me joda 
        else:
            row_dict[name] = [single_row.to_dict()]  #  yadi nahi hai to us name ki ek aur key create kari
    for key in row_dict:  # dict me se ek ek key nikaly
        filename = f"{key}.csv"  # fir usme alag alag key name ki file craete kari
        with open(filename,mode="w" ,newline="") as file :  # us file ko open kiya
            writer = csv.DictWriter(file, fieldnames=row_dict[key][0].keys())  # Define column headers
            writer.writeheader()    # un alag alag file me header likha
            writer.writerows(row_dict[key])  # un sabhi file me row write kari


link = input("Enter the path of document : ")
based = input("Enter the based to devid fale : " )

randomDataDevideFile(link,based)

