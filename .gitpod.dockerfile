FROM gitpod/workspace-full:latest
USER gitpod
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
RUN bash Anaconda3-5.0.1-Linux-x86_64.sh -b
RUN rm Anaconda3-5.0.1-Linux-x86_64.sh
ENV PATH=$PATH:$HOME/anaconda3
ENV PATH=$PATH:$HOME/anaconda3/bin
RUN conda update conda
RUN conda update anaconda
RUN conda update --all
RUN mkdir $HOME/notebooks
RUN jupyter notebook --generate-config --allow-root
# RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /home/ubuntu/.jupyter/jupyter_notebook_config.py
# EXPOSE 8888
USER root
# RUN cd /tmp && curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh && \
# sha256sum Anaconda3-2019.03-Linux-x86_64.sh && \
# bash Anaconda3-2019.03-Linux-x86_64.sh -y
# ENV PATH=$PATH:$HOME/anaconda3:$HOME/anaconda3/bin
