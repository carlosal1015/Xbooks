FROM gitpod/workspace-full:latest
USER root
RUN apt-get update && apt-get install -y
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh 
RUN bash Anaconda3-5.0.1-Linux-x86_64.sh -b -p ~/anaconda 
RUN echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc 
RUN conda update conda
RUN apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
USER root
