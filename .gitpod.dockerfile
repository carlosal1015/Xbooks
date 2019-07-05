FROM gitpod/workspace-full
RUN sudo apt-get remove python -y
RUN sudo apt-get update && sudo apt-get upgrade
RUN sudo apt-get install python3.7
