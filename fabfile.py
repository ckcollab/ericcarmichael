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
    print "Checking URLs"
    bad_urls = scan_directory_for_bad_urls(DEPLOY_PATH)

    if not bad_urls:
        print "URL's are looking good"
    else:
        for url in bad_urls:
            print "Broken link found in file %s on line %s linking to %s" % (url[1], url[2], url[0])

    return bad_urls


def deploy():
    clean()
    local("make html")

    bad_urls = check_urls()

    if not bad_urls:
        local("git push")
        local("git push heroku master")
