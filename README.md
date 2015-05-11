Eric Carmichael's blog
======================

![Picture of Eric Carmichael](content/images/kayak.jpg)

<p align="center"><b>"This is like my tenth time on a kayak, I'm pretty cool"</b> <br> &mdash; Eric Carmichael on Fernan Lake, Idaho</p>

Environment variables
=====================

```
export PELICAN_SITE_URL="http://ericcarmichael.com"
```

Getting started
===============

`pip install -r requirements.txt`

`export PELICAN_SITE_URL="file:///Users/you/your/blog/dir/output"`

Writing articles
================

`make regenerate`

this will write to `output/` whenever you change the articles in `content/`

Fab commands
============

`fab deploy`

cleans output, verifies urls, then if they are valid `git push`, and `git push heroku master`

`fab clean`

removes and recreates a clean `output/` dir

`fab check_urls`

iterates over every `a` tag to verify it has a URL and that URL exists, I wrote this mainly to catch myself
from missing small details, like [forgetting to fill in a `[text](url)` tag](http://www.ericcarmichael.com/writing-my-first-python-package.html)!
