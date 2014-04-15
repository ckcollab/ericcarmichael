import os

from existence import scan_directory_for_bad_urls
from fabric.api import *


# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))


def check_urls():
    with hide('warnings'):
        with settings(warn_only=True):
            result = local("existence {deploy_path}".format(**env))

            return result.return_code != 0


def deploy():
    clean()
    local("make html")

    bad_urls = check_urls()

    if not bad_urls:
        local("git push")
        local("git push heroku master")
