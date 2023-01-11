from __future__ import annotations
import pandas as pd
import git
from git import Repo
import os
import csv
from csv import writer
"""
Considering adding two queues one queue for creating repository then add to another getting all of those commits.
Next consideration is to add another thread, so file will be created then the commit info will be gathered.
"""

class Writer():          
    def __init__(self, ifile, ofile, write_frame):
        self.ifile = ifile
        self.ofile = ofile
        self.write_frame = write_frame
        ofile = open(ofile, "a", newline='', encoding='utf-8')
        header = ['GitAuthor','ProjectName', 'CommitID','CommitMessage', 'Lsof ModifiedFiles']
        write = writer(ofile)
        write.writerow(header)
        #write.close()
    def write_to_file(self, new_row):
        ofile = open(ofile, "a", newline='', encoding='utf-8')
        write = writer(ofile)
        write.writerow(new_row)
        #write.close()

class Sampler():          
    def __init__(self, size, c_list):
        self.size = size
        self.c_list = c_list
    def sample(self, writer):   
        sampled_list = []
        while(len(sampled_list) < self.size):
            row = self.c_list.sample()
            print("Randomly selected row: ",row)
            row_number = row.index.tolist()
            new_row = [self.c_list[row_number[0]][0],self.c_list[row_number[0]][1],self.c_list[row_number[0]][2],self.c_list[row_number[0]][3],self.c_list[row_number[0]][4]]
            if(new_row in sampled_list):
                print("Already in list.")
            else:
                print("Inserting row: ",new_row)
                sampled_list.append(new_row)
                writer.write_to_file(new_row)

class RepoContainer():          
    def __init__(self, file_path, reponame, repoURL):
        self.reponame = reponame
        self.repoURL = repoURL
        self.file_path = os.path.join(file_path, reponame)
    def is_created(self):
        is_created = os.path.isdir(self.file_path)
        return is_created
    def get_commits(self, writer):
        local_repo = Repo(self.file_path)
        branch = local_repo.active_branch
        branch = branch.name
        commits = list(local_repo.iter_commits(branch))

        for commit in commits:
            commitFiles = self.get_file_name(commit.stats.files)
            if('.travis.yml' in commitFiles):
                new_row = [commit.author, self.reponame, commit.hexsha, commit.message, list]
                writer.write_to_file(new_row)
            commitFiles=[]

    def get_file_name(info):
        lsofNames = []
        for n,dict_ in info.items():
            lsofNames.append(n)
        return lsofNames

        


if __name__ == "__main__":
    clone_repo_path = 'D:/ClonedRepos/' #change this file path
    commit_frame = pd.DataFrame()
    sample_frame = pd.DataFrame()
    #The first file paths below are the input files, and the second file paths are the output files
    commit_write = Writer('C:/Users/ogime/Desktop/ML-DevOps-Research/ML-PythonProjects-WithTravisCI-Test.csv', "D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv", commit_frame) #change here
    sample_write = Writer('D:/CloneWithGetPy/ML-CommitsFrom-PythonProjects.csv', "D:/CloneWithGetPy/ML-SampledCommitsFrom-PythonProjects.csv", sample_frame) #change here
    df = pd.read_csv(commit_write.ifile)
    rn = df['RepoName']
    url = df['GitHubURL']
    for cell in df.index: 
        try:
            currRepo = RepoContainer(clone_repo_path, rn[cell], url[cell])
            if(currRepo.is_created):
                print("Already cloned", currRepo.reponame)
            else:
                cloned_repo = Repo.clone_from(currRepo.repoURL, currRepo.file_path)
                print("Done cloning", currRepo.reponame, "repository.")
                print("Getting commits from repository:", currRepo.reponame)
                currRepo.get_commits(commit_write)
        except:
            print("Repository has a long file path or doesn't exist in github.")
            continue
    
    s_df = pd.read_csv(commit_write.ofile)
    sampler = Sampler(379, s_df.values.tolist())

    
