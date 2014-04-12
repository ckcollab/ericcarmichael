Title: Starting a blog with Pelican
Date: 2014-4-12 0:30
Tags: pelican, python, blogging

Deciding what static site generator to use was tricky. The first option was [Jekyll](http://jekyllrb.com/) which is ruby
and I'm looking for something python. Next I looked at [Hyde](https://github.com/lakshmivyas/hyde) but that had the
, in my opinion, extra requirement of [Django](https://www.djangoproject.com/). I feel like all I need something super simple
that has the bare minimum to poop out content from markdown.

Then I finally found [Pelican](https://github.com/getpelican/pelican) and it seems to satisfy all of my needs: python, ultra simple integration with [heroku](http://heroku.com/) via [this buildout](https://github.com/getpelican/heroku-buildpack-pelican)!

##Configuring

awjefawej

##Developing
Developing is a piece of cake with

    :::bash
    > make regenerate

Any time you make a change to a piece of content the site is rebuilt.

##Theming
asdf


##Deploying
Deploying is easy with a simple

    git push heroku master

    
