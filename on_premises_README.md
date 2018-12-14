---
layout: page
title: Installation
sidebar_link: true
id: on_premises_readme
toc: true
---

Copyright © tagtog Sp. z o.o.

# tagtog installation using Docker

The tagtog system runs as a mixture of **Docker** containers. This **works on Linux, macOS, and Windows**.


# HOWTO

## Requirements

Your system must have installed:

1. [Docker](https://www.docker.com)
  * The recommended version is >= 18.03
  * To ensure that your docker installation works correctly and that you have the necessary rights to install and run docker images, run: `docker info`. Please ensure that you don't get an error like _permission denied_, and rather as expected see the details of your docker installation.

2. [Docker Compose](https://docs.docker.com/compose/)
  * The recommended version is >= 1.18

3. **IMPORTANT**. The running docker host must have the `vm.max_map_count` setting variable to be at least greater than _262144_. You can check the value by running: `sysctl vm.max_map_count`. If it is too low, **set the value by running**: `sudo sysctl -q -w vm.max_map_count=262144`.

4. [Bash Shell](https://www.gnu.org/software/bash/)
  * Installed in practically all systems by default.
  * Clarification: any other Unix shell should work too, including for Windows the Unix-like environment Cygwin. However, only the Bash shell is officially supported.

5. [cURL](https://en.wikipedia.org/wiki/CURL)
  * Installed in practically all systems by default


### Machine Requirements

Your server (e.g. private one, or on AWS, Azure, or Linode) should meet the following minimum requirements:

* **8 GB RAM**
* **50 GB of disk space**


## First-time Install

* You will receive a single-line script. This script contains all the information regarding your one-server-only **license**.
* Execute the script in some folder where you will run from now on all tagtog-related commands.
* A helper bash script is installed in this folder. This script assumes an UNIX environment and was tested only on **Linux and macOS**. It should work on Windows with Cygwin too. The script is not mandatory to run tagtog, but it is highly recommended.


## Run

* Choose one full-path folder/volume where all your tagtog data will be stored. For description purposes, let's call this folder `$TAGTOG_HOME` (you can indeed assign it to a global variable, such as: `export TAGTOG_HOME="$PWD/tagtog_home"`). **Important**: always write this as a full path (that is, not as a relative path such ~/tagtog or ./tagtog, but rather `/my/volume/tagtog`).

* Run the application:

```shell
./tagtog_on_premises restart latest $TAGTOG_HOME

# See more options in the tagtog_on_premises script
```

* Point your browser now to: `https://<tagtog_running_ip>:<tagtog_https_port>`.


### HTTPS & SSL

tagtog runs on _https_ only and redirects all http requests to https. We recommend setting your http and https ports to the defaults 80 and 443 but you are free to choose other ones. See the `tagtog_on_premises` script.

By default, tagtog uses a SSL self-signed certificate. To use your own SSL certificate, place the following 2 files in the folder `${TAGTOG_HOME}/ssl`:

* `tagtog_PRIVATE_KEY.key` (you can use a symlink)
* `tagtog_SSL_CERTIFICATE.pem` (you can use a symlink)


### How and where the data is stored

All tagtog data is stored in the folder: `${TAGTOG_HOME}/persistent_data/`. We recommend that you have periodic backups to avoid data losses. There are other folders in `$TAGTOG_HOME`, which nature, however, is temporary; you can nonetheless back up that too.

### Proxy

The application supports http proxies and automatically recognizes your host variables `$http_proxy` and `$https_proxy` (either written in both all lower or all upper case).




## Update

You can manually check for [new tagtog updates on this link](http://docs.tagtog.net/updates.html). Then:

```shell
./tagtog_on_premises update
./tagtog_on_premises restart latest $TAGTOG_HOME
```


## Troubleshooting

Upon a problem, try one of the following solutions first.

If your issue or question is not resolved yet, shoot us directly an email: [support@tagtog.net](mailto:support@tagtog.net). We are also happy to open a slack chat team with you for faster communication.

Please provide detailed information of the problem and **send us always the container logs**: `docker logs tagtog_webapp_1` && `docker logs tagtog_taskmanager_1`.



### Issues with document uploading, or with the docker container `tagtog_taskmanager_1`:

Try:

1. Removing all queued documents for parsing: `rm "$TAGTOG_HOME/tmp/to_process/*"`
2. Restarting the application: `./tagtog_on_premises restart latest $TAGTOG_HOME`


### Issues in an update

Try:


```shell
echo "0" > LATEST_VERSION
./tagtog_on_premises update
./tagtog_on_premises restart latest $TAGTOG_HOME
```


### Wrong entity offsets on the display

On a few rare cases, the entity offsets from the underlying data model (ann.json) may not match those of the interface. This visually results in some seemingly-broken entities. You might try to fix these errors running the following script:

```shell
# PLEASE, BACKUP YOUR DATA FIRST
./tagtog_on_premises fix_documents latest $TAGTOG_HOME
```


### Lack of writing file access

On some rare cases, the docker containers cannot hold writing access to the `$TAGTOG_HOME` folder and file hierarchy.

In this case, figure out why that could be the case. Anything related to your user not having enough rights?

Otherwise, a quick solution is:

1. Grant all permissions to everybody: `chmod 777 -r $TAGTOG_HOME`
2. Restart the application: `./tagtog_on_premises restart ...`



### tagtog docker images not found, on a new server installation

Chances are that you must re-do a first-time installation on your new server/instance, like this:

```shell
./tagtog_on_premises first_installation LICENSE_NAME LICENSE_KEY
```

Do the above if you encounter something like this:

```
Creating network "tagtog_default" with the default driver
Pulling cache (redis:4.0-alpine)...
4.0-alpine: Pulling from library/redis
4fe2ade4980c: Already exists
fb758dc2e038: Pull complete
989f7b0c858b: Pull complete
d5318f13abaa: Pull complete
3521559474dd: Pull complete
add04b113886: Pull complete
Pulling db (tagtog_db:3.2018-W21.0)...
ERROR: The image for the service you're trying to recreate has been removed. If you continue, volume data could be lost. Consider backing up your data before continuing.

Continue with the new image? [yN]y
Pulling db (tagtog_db:3.2018-W21.0)...
ERROR: pull access denied for tagtog_db, repository does not exist or may require 'docker login'
.............................One process could not be started. Check the logs of 'tagtog_jobmanager_1'
```
