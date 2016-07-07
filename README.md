# kairx-analysis
Integrating Qualtrics and Optimizely data to help provide insight into the various studies underway

![mail](images/logo.png)

## About
The purpose of this repo is to provide initial insights into the data captured as part of the KaiRx studies. **Note: all patient related data in this repository is simulated and does not represent any actual individual.**

## Environment
All work will be conducted using [Jupyter's Data Science Notebook Docker Stack](https://github.com/jupyter/docker-stacks/tree/master/datascience-notebook). Once our repo is cloned and `pwd` is pointed toward this repositories parent directory, the following command can be used to bring up our environment:
>`docker run -d -p 8877:8888 -v $(pwd)/notebooks:/home/jovyan/work jupyter/datascience-notebook`

We will use this environment locally (http://127.0.0.1:8877) for development and will stand up a hosting server for our collaborators to view and interact with the results (http://colab-sbx-97.oit.duke.edu:8877).
