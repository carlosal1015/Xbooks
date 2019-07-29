FROM gitpod/workspace-full:latest
USER gitpod
RUN pyenv uninstall --force 2.7.15 && pyenv uninstall --force 3.7.2 && pyenv install anaconda3-5.3.1 && pyenv global anaconda3-5.3.1
USER root