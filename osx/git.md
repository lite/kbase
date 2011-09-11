GIT Guide
====

[Pro Git](http://progit.org/)
[Git Tutorial](http://www.vogella.de/articles/Git/article.html)
[Git cheat sheets](http://help.github.com/git-cheat-sheets/)
[Git Reference](http://gitref.org/)
[gitready](http://gitready.com/)
[Git](http://ihower.tw/blog/archives/2591)

install a git server
----

    apt-get install ssh
    sudo apt-get install git-core
    sudo adduser git

    # login to server
    # to test use localhost
    ssh git@IP_ADDRESS_OF_SERVER

    # Create repository
    mkdir example.git
    cd example.git
    git --bare init

revert
----
    
    git clean -n
    git clean -f
    
    echo "stupid change" > test01
    git checkout test01
    git add test01
    # restore the file in the staging index
    git reset HEAD test01
    # get the old version from the staging index
    git checkout test01
    
    #Revert a commit
    git revert commit_name
    
    # change the last commit message via the --amend parameter.
    git commit --amend -m "More changes - now correct"

rebase
----

    # Create a new file
    touch rebase.txt

    # Add it to git
    git add . && git commit -m "rebase.txt added to index"
    # Do some silly changes and commit
    echo "content" >> rebase.txt
    git add . && git commit -m "added content"

    # check the git log message
    git log
    
    git rebase -i HEAD~2


submodule
----

    git submodule add git://github.com/opscode/cookbooks.git cookbooks
    git add .gitmodules cookbooks
    git commit -m "Add submodule into version control";
    git submodule init
    git submodule update

fork
----

    git clone git://github.com/lite/dotfiles.git
    git remote add upstream git://github.com/gmarik/dotfiles
    git fetch upstream
    git merge upstream/master

rollback
----

    git log HEAD~1 -1 
    git revert HEAD~1
    git reset HEAD filename 
    git checkout filename 

svn -- not easy to use
----

    git svn clone http://csshx.googlecode.com/svn/ -s
    git remote add origin git@github.com:lite/csshx.git
    git push -u origin master
    git svn rebase
    git push
  

stash
----

    git stash save "stash for apply"
    git stash apply stash@{0}
    git stash pop
    git stash list
    git stash create
    git stash drop
    
patch
----
    
    git branch mybranch
    git checkout mybranch
    touch test05
    git add .
    git commit -a -m "First commit in the branch"
    # Create a patch --> git format-patch master
    git format-patch origin/master
    # Creates patch 0001-First-commit-in-the-branch.patch
    # Switch to the master
    git checkout master
    # Apply the patch
    git apply 0001-First-commit-in-the-branch.patch
    
blame
----
    
    git blame filename

optional parameter
----

    git status -s
    git add -i
    git log --pretty=oneline --graph
    git merge --squash branch
    git branch -a
