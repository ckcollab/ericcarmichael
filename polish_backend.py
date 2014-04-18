from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from polished.backends import PelicanBackend
from polished.decorators import polish


class EricPelicanBackend(PelicanBackend):

    @polish(urls=["output/pages/about.html"], commit_indexes=[112, 135])
    def fix_image_links_on_about_me_page(self):
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%% DOIN IT!'

        wait = WebDriverWait(self.DRIVER, 10)
        element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'img')))

        self.DRIVER.execute_script("""
            var img_array = document.getElementsByTagName('img');

            for(var i=0; i<img_array.length; i++) {
                var href_replaced = img_array[i].getAttribute('src').replace(/^\/images/, "../images");
                img_array[i].setAttribute("src", href_replaced);
            }
        """)

