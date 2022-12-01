import pandas as pd
import git
from git import Repo
import os
import csv
from csv import writer
from unidiff import PatchSet
from io import StringIO
import random

sample_size = 379
sampled_list = []

with open("D:/CloneWithGetPy/ML-SampledCommitsFrom-PythonProjects.csv", "a", newline='', encoding='utf-8') as write_file:
    readDataframe = pd.read_csv('D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv')
    header = ['GitAuthor','ProjectName', 'CommitID','CommitMessage', 'Lsof ModifiedFiles']
    z = writer(write_file)
    z.writerow(header)
    export = readDataframe.values.tolist()

    while(len(sampled_list) < sample_size):
        
        row = readDataframe.sample()
    
        print("Randomly selected row: ")
        print(row)
        row_number = row.index.tolist()
        new_row = [export[row_number[0]][0],export[row_number[0]][1],export[row_number[0]][2],export[row_number[0]][3],export[row_number[0]][4]]
        if(new_row in sampled_list):
            print("Already in list.")
        else:
            #print("Fixing row number: ",row_number[0]+6)
            print("Inserting row: ",new_row)
            sampled_list.append(new_row)
            z.writerow(new_row)
       # print(len(sampled_list))

write_file.close()