import pandas as pd
import git
from git import Repo
import os
import csv
from csv import writer
from unidiff import PatchSet
from io import StringIO

def get_file_name(info):
    lsofNames = []
    for n,dict_ in info.items():
        #print("This file name is ",n)
        #print("This file's changes are ",dict_)
        lsofNames.append(n)
    return lsofNames

#need to get path - add in dynamic pathing
clone_repo_path = 'D:/ClonedRepos/'
#need to create the datafile we'll update
with open("D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv", "a", newline='', encoding='utf-8') as write_file:
    #create data table
    header = ['GitAuthor','ProjectName', 'CommitID','CommitMessage', 'Lsof ModifiedFiles']
    z = writer(write_file)
    z.writerow(header)
    
    readDataframe = pd.read_csv('C:/Users/ogime/Desktop/ML-DevOps-Research/ML-PythonProjects-WithTravisCI-Test.csv')
    reponame = readDataframe['RepoName']
    export = readDataframe.values.T[0].tolist()
    for cell in range(len(export)): #len(export)
        if cell == 190 or cell == 210 or cell == 391 or cell == 417:
            print("Repository", reponame[cell], "has a long file path or doesn't exist.")
            continue
        file_path = os.path.join(clone_repo_path, reponame[cell])
        is_created = os.path.isdir(file_path)
        if(is_created):
            print("Reading from Repository:", reponame[cell])
            local_repo = Repo(file_path)
            branch = local_repo.active_branch
            branch = branch.name
            commits = list(local_repo.iter_commits(branch))

            for commit in commits:
                commitFiles = get_file_name(commit.stats.files)
                
                if ('.travis.yml' in commitFiles):
                    print("Commit author: ",commit.author) # author name
                    print("Repo name: ",reponame[cell])
                    print("CommitID: ",commit.hexsha)
                    print("Commit Message: ",commit.message) #commit message
                    print("Files changed: ", commitFiles)
                    new_row = [commit.author,reponame[cell],commit.hexsha,commit.message, commitFiles]
                    z.writerow(new_row)
                commitFiles=[]
        else:
            print("There was an error accessing", reponame[cell], "repository.")

write_file.close()
