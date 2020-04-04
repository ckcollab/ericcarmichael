Eric Carmichael's blog
======================

![Picture of Eric Carmichael](content/images/kayak.jpg)

<p style="text-align: center;"><b>"This is like my tenth time on a kayak, I'm pretty cool"</b> <br> &mdash; Eric Carmichael on Fernan Lake, Idaho</p>

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


```bash
make html
```

writes static content to `output/`

```bash
make regenerate
```
this will write to `output/` whenever you change the articles in `content/`

```bash
make clean
```
cleans `output/`

```bash
make publish
```

makes site using production settings. also, iterates over every `a` tag to 
verify it has a URL and that URL exists, I wrote this mainly to catch myself
from missing small details, like 
[forgetting to fill in a `[text](url)` tag](http://www.ericcarmichael.com/writing-my-first-python-package.html)!


# TODO

- [ ] Run polished again? Add instructions here
