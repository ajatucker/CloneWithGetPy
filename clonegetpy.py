import pandas as pd
from git import Repo
import os
#This is the repo that will contain all of our cloned repos
clonegetpy = Repo('D:/CloneWithGetPy')
clone_repo_path = 'D:/CloneWithGetPy/ClonedRepos/'

#The file path is hard coded, but it could be done dynamically by using os or pathlib
dataframe = pd.read_csv('D:/CloneWithGetPy/ML-PythonProjects-WithTravisCI.csv')
reponame = dataframe['RepoName']
repoURL = dataframe['GitHubURL']
#print sheet
export = dataframe.values.T[2].tolist()
for cell in range(len(export)): #add in len(export) when ready to pull all
    if cell == 190 or cell == 210:
        continue
    print("Row: ", cell)
    print("Cloning Repository name:", reponame[cell])
    print( "Cloning Repository URL:", repoURL[cell])
    #file_path = 'D:/CloneWithGetPy/ClonedRepos' + '/' + reponame[cell]
    file_path = os.path.join(clone_repo_path, reponame[cell])
    is_created = os.path.isdir(file_path)
    if(is_created):
        print("Already cloned",reponame[cell])
    else:
    #print(file_path)
        cloned_repo = Repo.clone_from(repoURL[cell], file_path)
        print("Done cloning", reponame[cell], "repository.")
print("Cloned all repositories.")