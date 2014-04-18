from selenium.webdriver.support import expected_conditions as EC

from polished.backends import PelicanBackend
from polished.decorators import polish


class EricPelicanBackend(PelicanBackend):





    # you can call execute javascript to reset A tag urls and shit!!! so smart

    @polish(urls=["tree trunk.html"])
    def test_func(self):
        self.DRIVER.execute_script("""
            var img_array = document.getElementsByTagName('img');

            for(var i=0; i<img_array.length; i++) {
                var href_replaced = img_array[i].getAttribute('src').replace(/^\/images/, "../images");
                img_array[i].setAttribute("src", href_replaced);
            }
        """)

