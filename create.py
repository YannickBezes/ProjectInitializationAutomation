import sys
import os
from github import Github
from config import *

def create():
    repo_name = str(sys.argv[1])
    os.makedirs(PATH + repo_name)
    user = Github(USERNAME, PASSWORD).get_user()
    repo = user.create_repo(repo_name)
    print("Succesfully created repository {}".format(repo_name))

if __name__ == "__main__":
    create()
