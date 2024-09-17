import os
import subprocess
from github import Github


def create_local_repo(repo_name):
    os.makedirs(repo_name, exist_ok=True)
    os.chdir(repo_name)
    subprocess.run(["git", "init"])
    print(f"Local repository '{repo_name}' created.")


def add_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", f"Add {filename}"])
    print(f"File '{filename}' added and committed.")


def push_to_github(repo_name, github_token):
    g = Github(github_token)
    user = g.get_user()
    repo = user.create_repo(repo_name)
    remote_url = f"https://{github_token}@github.com/{user.login}/{repo_name}.git"
    subprocess.run(["git", "remote", "add", "origin", remote_url])
    subprocess.run(["git", "push", "-u", "origin", "master"])
    print(f"Repository pushed to GitHub: {repo.html_url}")


def main():
    repo_name = input("Enter the repository name: ")
    filename = input("Enter the filename to add: ")
    content = input("Enter the file content: ")
    github_token = input("Enter your GitHub personal access token: ")

    create_local_repo(repo_name)
    add_file(filename, content)
    push_to_github(repo_name, github_token)


if __name__ == "__main__":
    main()
