pip install djangorestframework
pip install markdown
pip install django-filter
pip install django-haystack
pip install pyelasticsearch

# Install and start mysql
sudo apt-get install mysql-server
mysqld

# Setup Mysql Database:
CREATE DATABASE dweet;


## Install and start elastic search
wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.4.5/elasticsearch-2.4.5.tar.gz
cd elasticsearch-2.4.5
./bin/elasticsearch

#Configure and start django
# Build Models
./manage.py makemigrations
./manage.py migrate
# Build Full Text Index
./manage.py rebuild_index

#start django
./manage.py runserver



