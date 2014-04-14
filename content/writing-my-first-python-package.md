Title: Writing my first python package
Date: 2014-4-14 13:00
Tags: python, existence, pypi
Category: python
Status: draft

I've been looking make a little python package to launch on [pypi](https://pypi.python.org/) for quite some time. Just
recently with [Pelican]() I am having about 50 urges to make little tools that make the experience much smoother.


## The problem

One of the things that keeps irking me while writing posts was constantly having to double check that I put in the
correct value for each link in markdown

    So there I was, at the [Some Restaurant]() downtown and I totally saw Becky macking on Jonathon!

Right as I am getting into the juicy gossip I normally would blog about, now I have worries:

1. I will forget to fix that link
2. I will think about "did I fix that link?" even if I already did
3. I. will. forget. to. fix. that. LINK!
4. Years later I will wake up in a cold sweat wondering, "Did I fix that link?"


## The solution

My first idea was to make some kind of hook in the Pelican system that re-wrote `[text](url)` links where the `url` was
empty with the first google search result of the `text` description.

That idea sucks for so many reasons:

* It could completely destroy posts
* It modifies the repository
* Did I fix that link?

## Writing my first pypi package

It was easy as

### 1. setup something

### 2. something else

### 3. something omtein
