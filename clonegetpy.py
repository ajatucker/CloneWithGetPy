import pandas as pd
from git import Repo
import os
#This is the repo that will contain all of our cloned repos
clonegetpy = Repo('D:/CloneWithGetPy')
clone_repo_path = 'D:/CloneWithGetPy/ClonedRepos/'

#The file path is hard coded, but it could be done dynamically by using os
dataframe = pd.read_csv('D:/CloneWithGetPy/ML-PythonProjects-WithTravisCI.csv')
reponame = dataframe['RepoName']
repoURL = dataframe['GitHubURL']

export = dataframe.values.T[0].tolist()
for cell in range(len(export)): #add in len(export) when ready to pull all
    #need to investigate these repos in the following 4 cells
    #2 don't exist, 1 has a too long of a file path, and the last one had issues while cloning
    if cell == 190 or cell == 210 or cell == 391 or cell == 417:
        print("Repository", reponame[cell], "has a long file path or doesn't exist.")
        continue
    print("Row: ", cell) #displayed this to make sure all rows were read properly
    print("Cloning Repository name:", reponame[cell])
    print( "Cloning Repository URL:", repoURL[cell])
    file_path = os.path.join(clone_repo_path, reponame[cell])
    is_created = os.path.isdir(file_path)
    if(is_created):
        print("Already cloned", reponame[cell])
    else:
        cloned_repo = Repo.clone_from(repoURL[cell], file_path)
        print("Done cloning", reponame[cell], "repository.")
print("Cloned all repositories.")