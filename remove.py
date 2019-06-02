import sys
import os
from github import Github
from config import *

def remove():
    repo_name = str(sys.argv[1])
    # Get user
    repo = Github(USERNAME, PASSWORD).get_user().get_repo(repo_name)
    repo.delete()
    print("Succesfully deleted repository {}".format(repo_name))


if __name__ == "__main__":
    remove()
