

The goal of [polished]() is to show the awesome progression and amount of tweaks that go into any website. My resume
is a good example, dozens of hours of work and tweaking to come up with this pretty basic final product. Showing that
blood, sweat and hilarious tears in between should be pretty entertaining. Watch pages undulate, stretch, break,
grow, and shrink into place.


## How does it work?

Once you've installed polished, it works like this:
1. Fires up selected backend (for example, PelicanBackend if you use the [Pelican]() blog site generator)
2. Get the history of your git repo
3. Traverse that history, prepare the page and screen cap it

## Installation

Requires:

* [ImageMagick]()
* [PhantomJS]()


    pip install polished


For more detailed instructions please check out the [repo readme](https://github.com/ckcollab/polished).

## Usage

`polished` The default behavior is to capture `"http://localhost:8000/"`

`polished output/index.html` Local file

`polished http://localhost:8000/` Local server


**By default the files are saved to `polished/00001.polished.png`**






Title: polished
Date: 2014-4-16 15:10
Status: draft





    convert *.JPG -delay 10 -morph 10 %05d.morph.jpg

^ We could use imagemagick and that would morph images together, takes all JPG and converts frame 1 to frame 2 with 10 frames in between




