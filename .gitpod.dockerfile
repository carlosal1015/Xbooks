FROM gitpod/workspace-full:latest
USER root
RUN apt-get update && apt-get install -y 
USER gitpod
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh && \
        bash Anaconda3-5.0.1-Linux-x86_64.sh -b -p ~/anaconda && \
        rm Anaconda3-5.0.1-Linux-x86_64.sh && \
        echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc && \
        conda update conda
USER root
