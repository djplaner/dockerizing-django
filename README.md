## Docker version of OnTask

*Current status:* Basically a non-working skeleton.

This project aims to create a version of [OnTask](https://ontasklearning.org/) (in particular the [python version](https://github.com/abelardopardo/ontask_b) that runs as a Docker container/compose. 

Based on [this repo](https://github.com/realpython/dockerizing-django) that scaffolds the "dockerising" of Django app development.


### OS X Instructions

1. Build images - `docker-compose build`
1. Start services - `docker-compose up -d`
1. ??configure??
> - `docker-compose run web /usr/local/bin/python manage.py migrate`
1. Grab IP - `docker-machine ip dev` - and view in your browser
1. Navigate browser to host 0.0.0.0
1. Use OnTask
1. `docker-compose down`
