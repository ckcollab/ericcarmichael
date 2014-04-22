Title: Polished
Date: 2014-4-18 15:10
Category: python
Tags: python, polished, web development, development

The goal of [polished](http://github.com/ckcollab/polished) is to show all of the meticulous tweaks that go into a website. My resume
is a good example, dozens of hours of work and tweaking to come up with this pretty basic final product. Showing that
blood, sweat and hilarious tears in between should be pretty entertaining. Watch pages undulate, stretch, break,
grow, and shrink into place.


## How does it work?

Once you've installed polished, it works like this:

1. Fires up selected backend (for example, PelicanBackend if you use the [Pelican](https://github.com/getpelican/pelican) blog site generator)
2. Get the history of your git repo
3. Iterate through that history, preparing each page and finally screen cap it
4. If after reviewing the images you find bugs, you can go in and `@polish` out the kinks so it's a nice smooth video


## Examples

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/J4sBUXP7zoo?rel=0" frameborder="0" allowfullscreen></iframe>
<p align="center">
Resume page video without polishing
</p>

<iframe width="640" height="360" class="youtube" src="https://www.youtube-nocookie.com/embed/Yi5fHkGqe38?rel=0" frameborder="0" allowfullscreen></iframe>
<p align="center">
Polished resume page video
</p>

And I had to "polish" these videos to get them just right, fix bad links for some commits:

    :::python
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from polished.backends import PelicanBackend
    from polished.decorators import polish


    class EricPelicanBackend(PelicanBackend):

        def _patch_image_srcs(self):
            wait = WebDriverWait(self.DRIVER, 10)
            element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'img')))

            self.DRIVER.execute_script("""
                var img_array = document.getElementsByTagName('img');

                for(var i=0; i<img_array.length; i++) {
                    var href_replaced = img_array[i].getAttribute('src').replace(/^\/images/, "../images");
                    img_array[i].setAttribute("src", href_replaced);
                }
            """)

        @polish(urls=["output/pages/about.html"], commit_indexes=range(112, 135))
        def fix_image_links_on_about_me_page(self):
            self._patch_image_srcs()

        @polish(urls=["output/pages/resume.html"], commit_indexes=range(68,134))
        def fix_resume_page_broken_images(self):
            self._patch_image_srcs()

## Installation

Requires:

* [NodeJS](http://nodejs.org/)
* [PhantomJS](http://phantomjs.org/)

Then the usual


    :::bash
    > pip install polished


For more detailed instructions please check out the [repo readme](https://github.com/ckcollab/polished).

## Usage

    > polished

The default behavior is to capture `"index.html"` each commit

    > polished output/index.html

Local file

    > polished http://localhost:8000/

Local server


By default the files are saved to `polished_output/<commit count>.<sha>.polished.png` and `polished_output/output.mp4`
