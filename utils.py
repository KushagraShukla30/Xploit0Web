import os
from git import Repo
import shutil
import uuid

def clone_repo(url):
    repo_id = str(uuid.uuid4())
    path = f"cloned_repo/{repo_id}"
    if os.path.exists(path):
        shutil.rmtree(path)
    Repo.clone_from(url, path)
    return path
