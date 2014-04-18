Title: Polished
Date: 2014-4-18 15:10
Category: python
Tags: python, polished, web development, development

The goal of [polished](http://github.com/ckcollab/polished) is to show the awesome progression and amount of tweaks that go into any website. My resume
is a good example, dozens of hours of work and tweaking to come up with this pretty basic final product. Showing that
blood, sweat and hilarious tears in between should be pretty entertaining. Watch pages undulate, stretch, break,
grow, and shrink into place.


## How does it work?

Once you've installed polished, it works like this:
1. Fires up selected backend (for example, PelicanBackend if you use the [Pelican](https://github.com/getpelican/pelican) blog site generator)
2. Get the history of your git repo
3. Traverse that history, prepare the page and screen cap it

## Examples

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/J4sBUXP7zoo?rel=0" frameborder="0" allowfullscreen></iframe>
<p align="center">
Resume
</p>

<iframe width="640" height="360" class="youtube" src="//www.youtube-nocookie.com/embed/aVm0rIgwluw?rel=0" frameborder="0" allowfullscreen></iframe>
<p align="center">
Blog index
</p>

## Installation

Requires:

* [NodeJS](http://nodejs.org/)
* [PhantomJS](http://phantomjs.org/)


    pip install polished


For more detailed instructions please check out the [repo readme](https://github.com/ckcollab/polished).

## Usage

`polished` The default behavior is to capture `"index.html"` each commit

`polished output/index.html` Local file

`polished http://localhost:8000/` Local server


**By default the files are saved to `polished/<commit count>.<sha>.polished.png`**
