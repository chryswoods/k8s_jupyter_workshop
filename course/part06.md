# Step 6 - Creating the kubernetes cluster

In the last lesson you uploaded your custom jupyterhub docker image to your private Azure Container Registry.

The next step is to create your own Kubernetes cluster on the [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-gb/services/kubernetes-service/).

[Kubernetes](https://kubernetes.io/) is an example of a container orchestrator service. It is production quality, widely used and fully open source. Kubernetes works by spinning up and down pods, which are containers running on hardware. [Lots of documentation and tutorials are available here](https://kubernetes.io/docs/tutorials/). I have also written a [nice talk](https://drive.google.com/file/d/1kI7NB7jsIReVm2rznBTOcSMaLCuz7O9Q/view) that shows how Kubernetes and JupyterHub work together (from slide 32 onwards). There is also a nice [quickstart guide to using Kubernetes on Azure via AKS](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough).

We are going to now create a kubernetes cluster called `jupyter` in your `rseworkshop` resource group. For this workshop we will give the cluster just 2 cores on a single A2v2 machine instance. This costs about $0.076 per hour, so is pretty inexpensive ;-). Feel free to use more or larger machine instances for larger workshops. The full list of instances available and prices are [available here](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/).

To create the cluster use the command;

```
$ az aks create --resource-group rseworkshop --name jupyter --node-count 1 --node-vm-size Standard_A2_v2 --generate-ssh-keys

```

This may take a few minutes (I spent ten minutes watching the spinning ascii running logo...). When it finishes, you will hopefully see output similar to the above.

## Connecting to your kubernetes cluster

You connect to your kubernetes cluster using `kubectl`. We have already installed this program for you in this image. If you don't have it installed, then you can install it using the command;

```
$ az aks install-cli
```

The connect to your cluster you need to download its login credentials. You can get the credentials using the command;

```
$ az aks get-credentials --resource-group rseworkshop --name jupyter

```

Hopefully this succeeds and you see output similar to the above.

If it has succeeded, then you can query the nodes in your kubernetes cluster using the command;

```
$ kubectl get nodes

```

If this works, you should see that you have 1 node available. Normally you should have 3 nodes, as this gives resilience. For this workshop, and generally for testing, we use 1 node. It is possible to change the number of nodes dynamically after creating the workshop, so good practice is to create the initial workshop with 1 node, and to then scale up to as many nodes as needed during your workshop. Once the workshop is over you can then scale back down to 1 node.

***

# [Previous](part05.md) [Up](../README.md) [Next](part07.md)

