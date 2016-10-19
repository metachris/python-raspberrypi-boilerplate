import os
from fabric.api import local, run, env, task
from fabric.context_managers import cd, lcd
from fabric.operations import put, get
from fabric.decorators import parallel
from fabric.contrib.project import upload_project

# Change to fabfile directory, to make relative paths work
DIR_SCRIPT = os.path.dirname(os.path.realpath(__file__))
os.chdir(os.path.join(DIR_SCRIPT))

DIR_REMOTE = "/server/boilerplate"

env.use_ssh_config = True
if not env.hosts:
    # Set default host to something
    env.hosts = ["raspberrypi"]


@task
@parallel
def upload():
    """ Upload sources """

    # Upload source
    put("src/*.py", DIR_REMOTE, mirror_local_mode=True)


@task
@parallel
def uploadx():
    """ Upload a specific file only """
    put("src/main.py", DIR_REMOTE, mirror_local_mode=True)

