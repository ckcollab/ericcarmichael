Title: Writing my first python package
Date: 2014-4-14 13:00
Tags: python, existence, pypi, pelican, fabric
Category: python


I've been looking make a little python package to launch on [pypi](https://pypi.python.org/) for quite some time. Just
recently with [Pelican](http://getpelican.com) I am having about 50 urges per second to make little tools that make the
experience a little smoother.


## The problem

One of the things that keeps irking me while writing posts was constantly having to double check that I put in the
correct value for each link in markdown

    :::text
    So there I was, at [Some Restaurant I can't Remember]() downtown and I totally saw Becky macking on Jonathon!

Right as I am getting into the juicy gossip I normally would blog about, now I have worries:

1. I will forget to fix that link
2. I will think about "did I fix that link?" even if I already did
3. I. will. forget. to. fix. that. LINK!
4. Years later I will wake up in a cold sweat wondering, "Did I fix that link?"


## The attempted solution

My first idea was to make some kind of hook in the Pelican system that re-wrote `[text](url)` links where the `url` was
empty with the first google search result of the `text` description.

That idea sucks for so many reasons:

* It could completely destroy posts
* It modifies the repository
* Did I fix that link?


## The real solution: [Existence](https://github.com/ckcollab/existence)

After playing around with a few different ideas I finally thought: screw this. I was thinking too hard, all of the
solutions were too convoluted. When I stepped away from the computer and thought for a while I realized
the problem I was *really* trying to fix: broken links!

After some searching I didn't find a nice simple python module that ran through static html files, tried links, and spit
out which ones were bad.


## Writing the module

I want this to run quickly or I'll never use it, so my plan is to use `requests` asychronously after scanning all of the
files for broken links. However, after trying my damndest I couldn't get `grequests` to work right... I was having weird
errors in the background I couldn't debug easily.

Then I saw [this](http://stackoverflow.com/a/14369828/2197389) nice little example, here's my version:

    :::python
    def async_check_url(url, file_name, line_number):
        try:
            urllib2.urlopen(url)
        except urllib2.URLError:
            BROKEN_URLS.append((url, file_name, line_number))


    def check_urls(urls):
        '''
        expected format of urls is list of tuples (url, file name, source line) i.e. ("google.com", "index.html", 32)
        '''
        threads = list()

        for u in urls:
            t = Thread(target=async_check_url, args=(u[0], u[1], u[2]))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()






## Getting it on pypi

### 1. sign up on pypi.com

### 2. create `.pypirc` in home directory with login info

    :::text
    [distutils]
    index-servers = pypi

    [pypi]
    username:ckcollab
    password:hunter2

### 3. fill out setup.py

    :::python
    import os
    from setuptools import setup


    try:
        with open('README.md') as readme:
            long_description = readme.read()
    except IOError, ImportError:
        long_description = ''

    setup(
        install_requires = [
            "lxml>=3.3.4",
            "cssselect>=0.9.1"
        ],
        name="existence",
        py_modules=["existence"],
        version="0.0.8",
        author="Eric Carmichael",
        author_email="eric@ckcollab.com",
        description="Checks static .html files for bad links",
        long_description=long_description,
        license="MIT",
        keywords="link checker",
        url="https://github.com/ckcollab/existence",
        classifiers=[
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )



### 4. submit

    :::text
    > python setup.py register
    > python setup.py sdist upload



## Plugging it into [fabric](http://www.fabfile.org/)

    :::python
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






Now I just run

    > fab deploy

and I will never ever, ever have to worry about broken links in my blog! Thanks [existence](https://github.com/ckcollab/existence)!
