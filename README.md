propro
======

docker on project 

In [1]: from projects.models import ProjectEnv,ProjectEnvManager

In [2]: project_env = ProjectEnv.objects.create_project_env("buildubuild_team","buildbuild_project",["python, 2.7.8"])

In [4]: project_env = ProjectEnv.objects.create_project_env("buildubuild_team","buildbuild_project",["python, 2.7.8"])
---------------------------------------------------------------------------
ValidationError                           Traceback (most recent call last)
...
ValidationError: [u'The project name already exists']
...
In [15]: a = ProjectEnv.objects.get_project_env('buildbuildproject')

In [16]: a.docker_text
Out[16]: u'FROM ubuntu:14.04\n\nRUN apt-get update\nRUN apt-get install -y build-essential\nRUN apt-get install -y python-dev python-setuptools\n\nRUN easy_install pip\nRUN apt-get install -y git-core\nRUN apt-get install -y curl\n\n# To compile Python and pyenv utilities\nRUN apt-get install -y make libssl-dev zlib1g-dev libbz2-dev \\\nlibreadline-dev libsqlite3-dev wget llvm\n\n# Python version set\nRUN /bin/mkdir -p /downloads/python_pkgs/ && cd /downloads/python_pkgs/\nRUN /usr/bin/wget -P /downloads/python_pkgs/ https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tgz\nRUN /bin/tar -zxf /downloads/python_pkgs/Python-2.7.8.tgz -C /downloads/python_pkgs/\nRUN cd /downloads/python_pkgs/Python-2.7.8/ && /bin/sh configure\n#RUN /bin/sh /downloads/python_pkgs/Python-2.7.8/configure\nRUN /usr/bin/make -C downloads/python_pkgs/Python-2.7.8/ clean\nRUN /usr/bin/make -C downloads/python_pkgs/Python-2.7.8/\nRUN /usr/bin/make install -C downloads/python_pkgs/Python-2.7.8/\nRUN /bin/rm /usr/local/bin/python\nRUN /bin/ln -s /usr/local/bin/python2.7 /usr/local/bin/python\n'

