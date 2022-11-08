import pandas as pd
import git
from git import Repo
import os
import csv
from csv import writer
from unidiff import PatchSet
from io import StringIO

def get_changed_files(currCommit, repo):
    changed_files = []
    commit = repo.commit(currCommit)
    uni_diff_text = repo.git.diff(commit, commit,
                                    ignore_blank_lines=True, 
                                    ignore_space_at_eol=True)

    patch_set = PatchSet(StringIO(uni_diff_text), encoding='utf-8')
    for patched_file in patch_set:
        print('Are we hitting this?')
        file = patched_file.path
        print('filename:',file)
    print(changed_files)



#need to get path
clone_repo_path = 'D:/CloneWithGetPy/ClonedRepos/'
#need to create the datafile we'll update
#table = [{'GitAuthor': 'testname','ProjectName':'notproject', 'CommitID':'00000','CommitMessage':'this is a test message'}]
with open("D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv", "a", encoding='utf-8') as write_file:
    #create data table
    #header = ['GitAuthor','ProjectName', 'CommitID','CommitMessage']
    z = writer(write_file)
    #z.writerow(header)
    #z.writerows(table)
    
    readDataframe = pd.read_csv('C:/Users/ogime/Desktop/ML-DevOps-Research/ML-PythonProjects-WithTravisCI-Test.csv')
    reponame = readDataframe['RepoName']
    export = readDataframe.values.T[0].tolist()
    for cell in range(2):
        file_path = os.path.join(clone_repo_path, reponame[cell])
        is_created = os.path.isdir(file_path)
        if(is_created):
            print("Reading from Repository:", reponame[cell])
            local_repo = Repo(file_path)
            commits = list(local_repo.iter_commits('master'))
            #commits_list = list(local_repo.iter_commits('master'))
            for commit in commits:
                print(commit.author) # author name
                print(reponame[cell])
                print(commit.hexsha)
                print(commit.message) #commit message
                    #diff = commit.diff(prevCommit)
                get_changed_files(commit, local_repo)
                    #print(diff)
                new_row = [commit.author,reponame[cell],commit.hexsha,commit.message]
                z.writerow(new_row)
           #table.__add__({'GitAuthor': commit.author, 'ProjectName': reponame[cell], 'CommitID': commit.hexsha, 'CommitMessage': commit.message})
        else:
            print("There was an error accessing", reponame[cell], "repository.")

write_file.close()
#writing table to csv
#dataframe = pd.DataFrame.from_dict(table)
#dataframe.to_csv('D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv', mode='a', header=True)
