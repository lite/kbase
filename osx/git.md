GIT Guide
====

[Pro Git](http://progit.org/)
[gitready](http://gitready.com/)
[Git](http://ihower.tw/blog/archives/2591)

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
  
optional parameter
----

    git status -s
    git add -i
