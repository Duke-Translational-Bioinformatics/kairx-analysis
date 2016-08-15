FROM jupyter/datascience-notebook
MAINTAINER Ben Neely <nigelneely@gmail.com>

RUN pip install jupyterlab
RUN jupyter serverextension enable --py jupyterlab

EXPOSE 8888

CMD ["jupyter","lab"]
