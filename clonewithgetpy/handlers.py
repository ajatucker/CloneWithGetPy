from __future__ import annotations
import pandas as pd
import git
from git import Repo
import os
import csv
from csv import writer
from unidiff import PatchSet
from io import StringIO
from abc import ABC, abstractmethod
from typing import Any, Optional
"""
Trying to investigate if adding some handling would speed up repo cloning and getting commits at all.
Next consideration is to add another thread, so file will be created then the commit info will be gathered.
"""


# class IHandler(ABC):
#     """
#     Interface for file and repo
#     """

#     @abstractmethod
#     def set_next(self, handler: IHandler) -> IHandler:
#         pass

#     @abstractmethod
#     def handle(self, request) -> Optional[Repositories]:
#         pass


# class AHandler(IHandler):
#     _next_handler: IHandler = None

#     def set_next(self, handler: IHandler) -> IHandler:
#         self._next_handler = handler
#         # Returning a handler from here will let us link handlers in a
#         # convenient way like this:
#         # monkey.set_next(squirrel).set_next(dog)
#         return handler

#     @abstractmethod
#     def handle(self, request: Any) -> Repositories:
#         if self._next_handler:
#             return self._next_handler.handle(request)

#         return None

# #clone repo request
# class CloningHandler(AHandler):          
#     def handle(self, request: Any) -> Repositories:
#         if request:
#             tempR = request.checkFiles()
#             print("Is created is ",tempR)
#             #cloned_repo = Repo.clone_from()
#             #tempR.checkFiles()
#             print(request)
#             return tempR
#         else:
#             return super().handle(request)

# #commit requests
# class CommitHandler(AHandler):          
#     def handle(self, request: Any) -> Repositories:
#         if request:
#             return f"Monkey: I'll eat the {request}"
#         else:
#             return super().handle(request)


# class ReadFileHandler(AHandler):
#     def handle(self, request: Any) -> Repositories:
#         if request:
#             return f"test file"
#         else:
#             return super().handle(request)

# class WriteFileHandler(AHandler):
#     def handle(self, request: Any) -> Repositories:
#         if request:
#             return f"test file"
#         else:
#             return super().handle(request)

#I've encountered a few errors that will likely reoccur, so I'm going to add in an error handler at the minimum
# class ErrorHandler(AHandler):
#     def handle(self, request: Any) -> Repositories:
#         return request

class Repositories():          
    def __init__(self, file_path, reponame, repoURL):
        self.reponame = reponame
        self.repoURL = repoURL
        file_path = os.path.join(file_path, reponame)
        #file_path = os.path.join(file, reponame[cell])
    def checkFiles(self):
        is_created = os.path.isdir(self.file_path)
        return is_created

def client() -> None:

    table = pd.read_csv('D:/CloneWithGetPy/ML-PythonProjects-WithTravisCI.csv')
    clone_repo_path = 'D:/ClonedRepos/'
    reponameList = table['RepoName']
    repoURLList = table['GitHubURL']
    repos = []
    for cell in range(2):
        try:
            repos.append(Repositories(clone_repo_path, reponameList[cell], repoURLList[cell]))
            #result = handler.handle(repos[cell])
            if repos:
                #print("Cloned Repository name:", result.reponame)
                #print( "Cloned Repository URL:", result.repoURL)
                print("No issues")
            else:
                print("There were issues.")
        except:
            print("There was an error")
        


if __name__ == "__main__":
    #r_file = ReadFileHandler()
    #w_file = WriteFileHandler()
    #repoH = CloningHandler()
    #error = ErrorHandler()

    #r_file.set_next(w_file).set_next(repoH)

    client()
