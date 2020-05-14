# Harvard CS50W Notes

- [Harvard CS50W Notes](#harvard-cs50w-notes)
  - [Git and GitHub](#git-and-github)
    - [What is Git](#what-is-git)
    - [Basic git commands](#basic-git-commands)
      - [git clone](#git-clone)
      - [git add](#git-add)
      - [git commit -m "Message"](#git-commit--m-%22message%22)
      - [git push](#git-push)
    - [Merging conflicts](#merging-conflicts)
    - [Extra commands](#extra-commands)
      - [git log](#git-log)
      - [git reset](#git-reset)
  - [Advanced Git Commands](#advanced-git-commands)
    - [Git Branch](#git-branch)
    - [Git Checkout](#git-checkout)
    - [Git Merge](#git-merge)
    - [Git Pull](#git-pull)
    - [Forks](#forks)
    - [Pull Requests](#pull-requests)

## Git and GitHub

### What is Git

Git is a version control system, designed as a backup system and to host your code.
It can also be used in order to synchronise between different developers, especially on larger projects when there are multiple people working on the same project.

Another feature of git is that it can be used to test multiple features without affecting(or losing) the original code. It is handy for testing features out without making them mainstream.

### Basic git commands

#### git clone

To pull a repo down from GitHub we use the `git clone <git url>`
The git url is the link to the page. This will copy all the files into the directory we're in.

#### git add

It is important to "save" incremental changes using git in order to be able to return to code that works, in case there is a bug or a mistake inside of the code.
To apply these changes there are a number of steps that need to be carried out.
The first one of these is the command `git add <filename>`.
This command adds the filename you have specified inside of the <filename>.
Optional: You can use `git add .` in order to add all the files to "stage" the changes. The "." simply adds all the files

#### git commit -m "Message"

The next command is designed to commit the changes we have made, ready to be uploaded. The "-m" let's GitHub know that you want to add a message, followed by the message. This helps keep track of the changes you have made especially when you have made multiple changes to your code. It also helps when you want to recovery or return your code to a previous version.

#### git push

The `git push` command is the final command in the chain of operation. This is the command that pushes all the files that were added to your GitHub repo and "saves" them there.

### Merging conflicts

There might be times when the version you have on your physical computer might be different to the version that is stored in your repository.
This might happen when another developer has worked on the file and committed changes to the repo whilst you're also looking to upload them.
In that case, your editor will open both versions on your computer and show you the differences. You will then have to select the section that you want to keep and the sections that you want to delete in order to sync the code back up. This is to prevent code from being overwritten within the same branch.
You will see something like:

```git
<<<<<< HEAD
 --- Changes that you have made are listed here ---
======
 --- Here is what is different on the repo ---
>>>>>>
```

You will then have to either delete lines from the repo or delete lines from your "section" in order to be able to upload the data to the internet.

### Extra commands

#### git log

The `git log` command will show you the log of the commits that have been made.

#### git reset

There are two git reset commands:

```git
git reset --hard <commit>
git reset --hard origin/master
```

The first command allows you to go back to a previous version. The commit is the hash file that you will find when you run the `git log` command.
The second command will return your code back to the version when you downloaded it of the GitHub repo website.

## Advanced Git Commands

### Git Branch

`git branch` is a command that's used split off code from the working master code. This is typically done in order to work on a new feature without affecting the master branch of the code. This is helpful in order to avoid bugs in the main code as well as to be able to test new features on a separate website, for example.
Using the command will list all the current branches that are available.

`git branch name` will add a branch. The code will not be visible on GitHub unless you push it!

`HEAD` in git means that it is the current branch that is being worked on. Whatever repository we were to pull down (feature branch or master) would be the head.

### Git Checkout

`git checkout` is the command that is used to switch between branches. Using `git checkout name` will switch to the branch with a specific name. `git checkout master` will switch back to the master branch.
Switching branches will change the file that is being worked on to the most up to date one on the particular branch!

### Git Merge

`git merge` is a command in order to merge a branch to the master. `git merge name` is the full command, where name is the name of the branch you want to merge into the master.

### Git Pull

`git pull` combines both `git fetch` and `git merge origin/master` into one command. It updates the repo on your machine to the the version that's currently stored on GitHub!

### Forks

Forking a project won't affect the original repo on GiHub but it allows you to work on the project yourself. This is commonly used in open source projects.

### Pull Requests

A pull request brings in changes from the your repo into another repo. Pull requests are a great way to get feedback about your code. Remember that a pull request won't automatically merge your code with the project, but it will go into a review stage where the code will be examined by the other developer.
It's a very visual way to see your changes vs the project you have forked.
