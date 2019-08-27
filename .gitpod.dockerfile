FROM gitpod/workspace-full:latest
USER gitpod
RUN cd /tmp && curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh && \
sha256sum Anaconda3-2019.03-Linux-x86_64.sh && \
bash Anaconda3-2019.03-Linux-x86_64.sh -y
ENV PATH=$PATH:$HOME/anaconda3:$HOME/anaconda3/bin
USER root
