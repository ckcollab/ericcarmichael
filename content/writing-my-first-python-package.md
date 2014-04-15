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


## The real solution

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
        print "Checking: %s" % url
        response = urllib2.urlopen(url)

        if response.code != 200:
            broken_link_exception(url, file_name, line_number)


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

    readme = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

    setup(
        name="existence",
        py_modules=["existence"],
        version="0.0.1",
        author="Eric Carmichael",
        author_email="eric@ckcollab.com",
        description="Checks static .html files for bad links",
        long_description=readme,
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
    from fabric.api import local, run

    def deploy():
        # run make html
        # run existence
        # if existence has failures stop
        # git push heroku master
        pass





Now I just run

    > fab deploy

and I will never ever, ever have to worry about broken links in my blog! Thanks [existence](https://github.com/ckcollab/existence)!
