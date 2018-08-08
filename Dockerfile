# Start your container from one of the many example 
# containers on DockerHub. In this case, we will start
# with a minimal container that provides a working
# Python 3.6 environment

FROM python:3.6-slim-stretch

# Next, it is good to label your image with the maintainer
# Please feel free to put your own name and contact 
# address below
LABEL maintainer="Christopher Woods <Christopher.Woods@bristol.ac.uk>"

# First we want to install all of the Python dependencies
# We should do this as root
USER root

# We will need git to install the Pymaging dependencies.
# It is good practice to update apt before the install,
# and to then remove any unnecessary files afterwards so
# that you keep your container size small
RUN apt-get update && \
    apt-get install --no-install-recommends -qy git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Now lets run the three pip commands
RUN pip install qrcode[pil]
RUN pip install git+git://github.com/ojii/pymaging.git#egg=pymaging
RUN pip install git+git://github.com/ojii/pymaging-png.git#pymaging-png

# We also need to ensure we install jupyter (it is required to
# run a workshop as a jupyter notebook!)
RUN pip install jupyter

# We don't want to be root when running the container,
# so lets now create a normal user account called "jovyan"
# To do this, first create some environment variables
# for this user
ENV SHELL=/bin/bash \
    NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100

ENV HOME=/home/$NB_USER

# Now add a little script that can properly set the file
# access permissions of directories - put it into /usr/bin
ADD fix-permissions /usr/bin/fix-permissions

# We are now ready to create the user account...
RUN useradd -m -s $SHELL -N -u $NB_UID $NB_USER && \
    fix-permissions $HOME

# Now change into the HOME directory and switch
# into the $NB_USER account. All commands from now
# will execute as the user
WORKDIR $HOME
USER $NB_USER

# Add all of the workshop files to the home directory
ADD example_workshop/lesson*.ipynb $HOME/

# The jupyter notebook will run on port 8888. Make sure that
# this port is exposed by the container
EXPOSE 8888

# Set the entrypoint of the container. This is the command
# that will be run when the container starts.
ENTRYPOINT ["jupyter-notebook", "--ip=0.0.0.0"]

# Always finish a Dockerfile by changing to a normal user.
# This stops you from ever publishing a container that accidentally
# runs as root!
USER $NB_USER
