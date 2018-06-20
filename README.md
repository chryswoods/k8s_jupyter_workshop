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

Instructions to install and test all of these are below:

### git

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
   stable"

# sudo apt-get update
# sudo apt-get install docker-ce
```

