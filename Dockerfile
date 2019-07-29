FROM continuumio/miniconda:latest
LABEL ProjectName="Xbooks" \
      Author="XinYaanZyoy" \ 
      Organization="Xsoft-technologies" \
      GitHub="xsoft-technologies/Xbooks" \
      website="https://xsoft-technologies.github.io/Xbooks" \
      email="patelparth0937@gmail.com"
WORKDIR /
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN mkdir Xbooks/
WORKDIR /Xbooks/
COPY environment.yml ./
COPY app/. ./
RUN echo "conda activate" >> ~/.bashrc
RUN conda env create -f environment.yml	
ENV PATH /opt/conda/envs/Xbooks_env/bin:$PATH
