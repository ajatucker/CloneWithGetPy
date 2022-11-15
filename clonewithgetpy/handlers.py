import pandas as pd
import git
from git import Repo
import os
import csv
from csv import writer
from unidiff import PatchSet
from io import StringIO
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
"""
Trying to investigate if adding some handling would speed up repo cloning and getting commits at all.
Next consideration is to add another thread, so file will be created then the commit info will be gathered.
"""


class IHandler(ABC):
    """
    Interface for file and repo
    """

    @abstractmethod
    def set_next(self, handler: IHandler) -> IHandler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AHandler(IHandler):
    _next_handler: IHandler = None

    def set_next(self, handler: IHandler) -> IHandler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

#clone repo request
class CloningHandler(AHandler):          
    def handle(self, request: Any) -> str:
        if request == "clone":
            return f"Begin Cloning"
        else:
            return super().handle(request)

#commit requests
class CommitHandler(AHandler):          
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class FileHandler(AHandler):
    def handle(self, request: Any) -> str:
        if request == "test":
            return f"test file"
        else:
            return super().handle(request)

#I've encountered a few errors that will likely reoccur, so I'm going to add in an error handler at the minimum
class ErrorHandler(AHandler):
    def handle(self, request: Any) -> str:
        if request == "error":
            return f"print error message"
        else:
            return super().handle(request)

class Repo():          
    file_path = None
    repoName = None
    repoURL = None
    def __init__(self, file):
        table = pd.read_csv('D:/CloneWithGetPy/ML-PythonProjects-WithTravisCI.csv')
        reponame = table['RepoName']
        repoURL = table['GitHubURL']
        #file_path = os.path.join(file, reponame[cell])
    def checkFiles(self, f):
        is_created = os.path.isdir(f)

if __name__ == "__main__":
    file = FileHandler()
    repo = CloningHandler()

    file.set_next(repo)
