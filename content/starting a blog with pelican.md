Title: Starting a blog with Pelican
Date: 2014-4-12 0:30
Tags: pelican, python, blogging

Deciding what static site generator to use was tricky. The first option was [Jekyll](http://jekyllrb.com/) which is ruby
and I'm looking for something python. Next I looked at [Hyde](https://github.com/lakshmivyas/hyde) but that had the
, in my opinion, extra requirement of [Django](https://www.djangoproject.com/). I feel like all I need something super simple
that has the bare minimum to poop out content from markdown.

Then I finally found [Pelican](https://github.com/getpelican/pelican) and it seems to satisfy all of my needs: python, ultra simple integration with [heroku](http://heroku.com/) via [this buildout](https://github.com/getpelican/heroku-buildpack-pelican)!






## Development

### Getting started

    :::bash
    > pelican-quickstart

That will take you through a wizard to create a project structure like:

    yourproject/
    ├── content
    │   └── (pages)
    ├── output
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish

### Testing locally

    :::bash
    > make regenerate

Any time you make a change to a piece of content the site is rebuilt.






## Theming

### Theme folder structure

This is what I ended up with for a rough rough draft, from examples in [pelican-themes](https://github.com/getpelican/pelican-themes)

    mytheme/
    ├── static
    │   └── css
    │   └── fonts
    │   └── images
    ├── templates
    │   └── includes
    │        └── _article.html
    │   └── article.html
    │   └── base.html
    │   └── index.html
    │   └── page.html

### Adding tags

I added this to the bottom of my `_article.html`

    :::django
    {% if article.tags %}
        <div class="tags">
            <i class="fa fa-tags"></i>
            {% for tag in article.tags %}
                <a href="{{ SITEURL }}/{{ tag.url }}">{{ tag }}</a>{% if not loop.last %}, {% endif %}
            {% endfor %}
        </div>
    {% endif %}

### Adding page links

Added this to my menu, the "blog" is just a link back to index, so I added that manually

    :::django
    <div class="menu">
        <ul>
            <li><a href="{{ SITEURL }}/index.html">blog</a></li>
            {% for page in pages %}
                <li><a href="{{ SITEURL }}/{{ page.url }}">{{ page.title|lower }}</a></li>
            {% endfor %}
        </ul>
    </div>








## Deploying

### Easy with buildout

    > git push heroku master

### Compressing CSS/JS

I used the assets plugin from [pelican-plugins](https://github.com/getpelican/pelican-plugins) which requires the [webassets](https://github.com/miracle2k/webassets) python module.

    :::django
    {% assets filters="cssmin", output="css/packed.min.css", "css/bootstrap.min.css", "css/pygment-solarized.css", "css/main.css" %}
        <link rel="stylesheet" href="{{ SITEURL }}/{{ ASSET_URL }}">
    {% endassets %}

### Configuration

I created an environment variable `PELICAN_SITE_URL` for my virtualenv and on heroku, that way I can set it locally and test with `make regenerate` easily.







## Conclusion

Man. What a joy! Everything made sense, except for a couple hiccups with webassets that ended up being my fault, typical!

I'd recommend [Pelican](https://github.com/getpelican/pelican) to anyone looking to start a simple blog, it was a joy to work with thanks to all of the hard work
that went into `pelican-quickstart` and the [custom heroku buildout](https://github.com/getpelican/heroku-buildpack-pelican)!
