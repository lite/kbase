GIT Guide
====

[gitready](http://gitready.com/)
[Git 版本控制系統 (1)](http://ihower.tw/blog/archives/2591)

submodule
----

<pre>
git submodule add git://github.com/opscode/cookbooks.git cookbooks
git add .gitmodules cookbooks
git commit -m "Add submodule into version control";
git submodule init
git submodule update
</pre>

fork
----

<pre>
git clone git://github.com/lite/dotfiles.git
git remote add upstream git://github.com/gmarik/dotfiles
git fetch upstream
git merge upstream/master
</pre>


rollback
----

<pre>
git log HEAD~1 -1 
git revert HEAD~1
git reset HEAD filename 
git checkout filename 
</pre>

svn -- not easy to use
----

<pre>
git svn clone http://csshx.googlecode.com/svn/ -s
git remote add origin git@github.com:lite/csshx.git
git push -u origin master
git svn rebase
git push
</pre>