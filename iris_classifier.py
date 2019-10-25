# Max Geiszler
# 5/8/19
# CS3310 HW Assignment 4


import os
import pandas as pd


cwd= os.getcwd()
#Set the current working directory (cwd):
cwd = os.getcwd()
print('The current working directory is', cwd, '\n')


file_to_read ='iris.csv'

print('1) Using pd to read file:', file_to_read, '\n')
df= pd.read_csv(os.path.join(cwd, file_to_read))



def decision(sep_l, sep_w, pet_l, pet_w):
    vir = "virginica"
    ver = "versicolor"
    sel = "setosa"
    sepL_sepW = sep_l+sep_w
    if pet_w < 1.0:
        return sel
    elif pet_w >= 1.8:
        return vir
    elif pet_l > 5.1:
        return vir
    elif pet_w <=1.4:
        return ver
    elif sepL_sepW <8.3:
        return vir
    else:
        return ver 

print("test decision")
success = 0
fail = 0
for i, row in df.iterrows():
    sep_l = row["sepal_length"]
    sep_w = row["sepal_width"]
    pet_l = row["petal_length"]
    pet_w = row["petal_width"]
    cl = row["class"]
    guess = decision(sep_l,sep_w, pet_l, pet_w)
    
    if  guess == cl:
        success +=1
    else:
        fail +=1
        print("thought "+ guess, " was "+ cl+"\n")
        # print("failed on "+ str(i))
        print(row)

print(str(success/150)+ "% accuracy")




