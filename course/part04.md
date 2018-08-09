# Step 4 - JupyterHub

In the last lesson you learned how to build a docker image that contained all of the software and notebooks needed for the workshop-in-a-workshop. You also learned how to run the container and connect to the workshop.

While this worked, the user experience was not satisfactory. You had to copy and paste an access token, and for this to work, the user has to have docker installed. Ideally, we would like to move this docker container to the cloud. This would enable your learner to simply connect to the cloud-based container from their webbrowser, so will not need docker (or your container image) installed.

The first step to moving to the cloud is we need to prepare the container so that it can be used by multiple learners. To do this, we will use [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/). JupyterHub is a multi-user hub that can spawn, manage and proxy multiple instances of single-user Jupyter notebooks. JupyterHub provides a single server to which learners can connect. When a learner connects, JupyterHub will spin out a new jupyter-notebook kernel, one for each learner, based on the docker container image that you supply.

## Building your JupyterHub image

To get this to work, we need to add JupyterHub to our workshop-in-a-workshop jupyter image. This is a little complex. To make it easier, JupyterHub provides a range of base images. In the `jupyterhub` directory you can find the below Dockerfile;

```
```

Before we build this image, we should clean out all old docker images. This saves space, particularly if you are running this as part of the RSE workshop, for which disk space is very limited. The below command will remove all unused and untagged docker image containers;

```
$ docker system prune -a
```




***

# [Previous](part03.md) [Up](../README.md) [Next](part05.md)

