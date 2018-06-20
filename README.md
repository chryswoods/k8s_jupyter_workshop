# Building and Deploying Custom JupyterHub Images using Docker and Kubernetes to run Workshops in the Cloud

Jupyter provides an excellent interactive environment for running workshops. While there are many free services that let you explore Jupyter, you will need to run your own JupyterHub server if you want to use a custom image that includes your own software, if you want more cores than are provided by the free service, or you want to run a workshop with large numbers of attendees. Building and deploying your own JupyterHub using Docker, Kubernetes and the Cloud is very easy, and this workshop will show you how. You will build your own Docker image, create your own Cloud Kubernetes cluster, and will then deploy JupyterHub to this cluster using Helm. We will also provide tips and tricks we’ve learned from running Jupyter workshops ourselves. So, in short, this is a workshop in which you will learn how to build and run your own workshop

## Recommended prerequisites
You should be comfortable using the Linux command line, should have a very basic understanding of what Docker (or containers) are, and have some knowledge of what Jupyter is (we will provide background reading on Docker and Jupyter, and will teach you about Kubernetes, JupyterHub, and deploying these to the cloud).

## Installing the material onto the VM

The VM needs to have the following installed:

1. Git (so you can download and update this material)
1. A Python that includes jupyter (we will use anaconda python)
1. Docker, with a running docker service
1. The Microsoft "az" command line interface
1. The "kubectl" interface installed via "az"
1. Helm

Instructions to install and test all of these are below.

### git

Install

```
# sudo apt install git
```

Test

```
# git clone https://github.com/chryswoods/k8s_jupyter_workshop
# cd k8s_jupyter_workshop
# ls
LICENSE   README.md  etc. etc.
```

(this should result in the contents of this GitHub repository being
 downloaded into the local k8s_jupyter_workshop directory)

### Anaconda python

We need a Python that includes Jupyter. The easiest way to do this is to use
anaconda python. Install this using

```
# wget https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh
# chmod a+x Anaconda3-5.2.0-Linux-x86_64.sh
# ./Anaconda3-5.2.0-Linux-x86_64.sh
```

This should unpack the installer and ask you where you want to install
anaconda python. Accept the default installation directory of 
`/home/workshops/anaconda3`. Anaconda will install into this directory.

To test, run

```
# ~/anaconda/bin/jupyter-notebook
```

This should print out a lot to the screen showing that Jupyter is starting, 
and then it will launch a web browser with a Jupyter file dialog.

You can close the web browser and use "CTRL+C" to shut down the 
Jupyter server.

Once anaconda has installed and you are happy, you can delete the installer

```
# rm Anaconda3-5.2.0-Linux-x86_64.sh
```

### Docker

Install `docker-ce` using the instructions [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce)

```
# sudo apt-get update
# sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22

# sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   edge"

# sudo apt-get update
# sudo apt-get install docker-ce
```

(note we had to use the "edge" repository as a "stable" version for docker-ce
does not exist yet for Ubuntu 18.04).

To test, run

```
$ sudo docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
Digest: sha256:f5233545e43561214ca4891fd1157e1c3c563316ed8e237750d59bde73361e77
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

and you should see the output as printed below the command.

## Microsoft "az" command line interface

We will install following the instructions [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest)

```
# AZ_REPO=$(lsb_release -cs)
# echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
# sudo tee /etc/apt/sources.list.d/azure-cli.list
# curl -L https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add 
# sudo apt-get install apt-transport-https
# sudo apt-get update && sudo apt-get install azure-cli
```


