"""
Check git vesion
git --version

For Git installation 1st time set config values

git config --global user.name "Amir Savvy"
git config --global user.email "mianamirlahore@gmail.com"

git config --list


Take help

git help config
git config --help
git add --help


Initialize a repo from existing code

git init

Before 1st commit
git status

To ignore the file create
git .gitignore

Add files
git add test.py
git add -A
git reset test.py
git commit -m "Initial commit"
git log


 Clone the remote repo
 git clone ../remote_repo.git


Check remote branch
git remote -v
git branch -v

Pushing the changes

git diff
git status
git add -A
git commit -m 'message'

Then push
git pull origin master
git push origin master

Common Git work flow of developers

Create new branch
git branch new_login
git checkout new_login

Push changes into branch
git push -u origin branch-name

Check all local and remote branches
git branch -a


Merge a branch
git checkout master
git pull origin master
git branch --merged
git merge branch-name
git push origin master


Deleting a branch

git branch --merged
git branch -d branch-name
git branch -a
git push origin --delete branch-name

# Fixing Common Mistakes and Undoing Bad Commits











































"""