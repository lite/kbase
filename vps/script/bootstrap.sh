# rvm bootstrap

apt-get -q -y update
apt-get -q -y install build-essential bison openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libmysqlclient-dev libmysqlclient16
apt-get -q -y install git-core curl
apt-get -q -y install clang
apt-get -q -y install ruby1.8-dev rubygems                

bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)
rvm install ree 
rvm use ree --default
rvm gem install chef ohai --source http://gems.opscode.com --source http://gems.rubyforge.org --no-ri --no-rdoc

