import pandas as pd
import git
from git import Repo
import os
import csv
from csv import writer
from unidiff import PatchSet
from io import StringIO

# def get_changed_files(currCommit, prevCommit, repo):
#     print("This is current commit info: ",currCommit) 
#     changed_files = []
#     if(prevCommit == commit):
#         for x in currCommit.diff(prevCommit):
#             if x.a_blob.path not in changed_files:
#                 changed_files.append(x.a_blob.path)
        
#             if x.b_blob is not None and x.b_blob.path not in changed_files:
#                 changed_files.append(x.b_blob.path)
#     else:
#         print("empty")
        
#     print(changed_files)

def get_diff_files(c, prevC):
    diffObj = c.diff(prevC)
    all_files = []
    for diff in diffObj.iter_change_type('A'):
        #print("Added file", str(diff))
        all_files.append(diff)
    for diff in diffObj.iter_change_type('D'):
        #print("Deleted file", str(diff))
        all_files.append(diff)
    for diff in diffObj.iter_change_type('R'):
        #print("Renamed file", str(diff))
        all_files.append(diff)
    for diff in diffObj.iter_change_type('M'):
        #print("Modified file", str(diff))
        all_files.append(diff)
    for diff in diffObj.iter_change_type('T'):
        #print("Changed in type file", str(diff))
        all_files.append(diff)

    lsofFiles = []
    #print("All changed files:")
    for f in all_files:
        a_path = f.a_rawpath.decode('utf-8')
        #b_path = f.a_rawpath.decode('utf-8')
        #print("+",b_path)
        #print("-",a_path)
        lsofFiles.append(a_path)
    print("All changed files: ",lsofFiles)
    return lsofFiles



#need to get path
clone_repo_path = 'D:/ClonedRepos/'
#need to create the datafile we'll update
#table = [{'GitAuthor': 'testname','ProjectName':'notproject', 'CommitID':'00000','CommitMessage':'this is a test message'}]
with open("D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv", "a", newline='', encoding='utf-8') as write_file:
    #create data table
    header = ['GitAuthor','ProjectName', 'CommitID','CommitMessage', 'Lsof ModifiedFiles']
    z = writer(write_file)
    z.writerow(header)
    #z.writerows(table)
    
    readDataframe = pd.read_csv('C:/Users/ogime/Desktop/ML-DevOps-Research/ML-PythonProjects-WithTravisCI-Test.csv')
    reponame = readDataframe['RepoName']
    export = readDataframe.values.T[0].tolist()
    for cell in range(1):
        file_path = os.path.join(clone_repo_path, reponame[cell])
        is_created = os.path.isdir(file_path)
        if(is_created):
            print("Reading from Repository:", reponame[cell])
            local_repo = Repo(file_path)
            commits = list(local_repo.iter_commits('master'))
            #noCommit = commits[-1]
            for commit in commits:
                prevIndex = commits.index(commit)
                if(prevIndex == (len(commits)-1)):
                    prevCommit = commits[prevIndex]
                else:
                    prevCommit = commits[prevIndex+1]
                #get_changed_files(commit, prevCommit, local_repo)
                print("Commit author: ",commit.author) # author name
                print("Repo name: ",reponame[cell])
                print("CommitID: ",commit.hexsha)
                print("Commit Message: ",commit.message) #commit message
                commitFiles = get_diff_files(commit, prevCommit)
                #diff = commit.diff(prevCommit)
                new_row = [commit.author,reponame[cell],commit.hexsha,commit.message, commitFiles]
                #print("Getting updated files: ")
                z.writerow(new_row)
                #prevCommit = commit
           #table.__add__({'GitAuthor': commit.author, 'ProjectName': reponame[cell], 'CommitID': commit.hexsha, 'CommitMessage': commit.message})
        else:
            print("There was an error accessing", reponame[cell], "repository.")

write_file.close()
#writing table to csv
#dataframe = pd.DataFrame.from_dict(table)
#dataframe.to_csv('D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv', mode='a', header=True)
