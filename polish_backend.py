from polished.backends import PelicanBackend
from polished.decorators import polish


class EricPelicanBackend(PelicanBackend):





    # you can call execute javascript to reset A tag urls and shit!!! so smart

    @polish(urls=["tree trunk.html"])
    def test_func(self):
        print 'riddeeee'

    @polish(commit_indexes=range(1, 5))
    def test_funcer(self):
        print 'riddeeee'
