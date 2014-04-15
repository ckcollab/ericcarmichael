import os

from existence import get_bad_urls
from fabric.api import *


# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))


def deploy():
    clean()
    local("make html")

    print "Checking URLs"
    bad_urls = get_bad_urls(DEPLOY_PATH)

    if not bad_urls:
        print "URL's are looking good"
        local("git push")
        local("git push heroku master")
    else:
        for url in bad_urls:
            print "Broken link found in file %s on line %s linking to %s" % (url[1], url[2], url[0])
