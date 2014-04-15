

Let's use webkit2png and some simple calls to git checkout, then calls to "make project"

https://stackoverflow.com/questions/2744191/how-do-i-use-python-webkit2png-to-take-many-screenshots-at-the-same-time


1. git checkout i
2. run whatever script/functions you need to make the repo work
3. webkit2png that shit



https://pythonhosted.org/GitPython/0.3.1/tutorial.html

    If you need paging, you can specify a number of commits to skip:

    repo.iter_commits('master', max_count=10, skip=20)

HA! It will generate our list of commits and we can even skip.. what a joy!


    ffmpeg -r 25 -qscale 2 -i %05d.morph.jpg output.mp4

`-r 25` is fps
`-qscale` is quality 1 highest, 32 lowest
00001.morph.jpg, 5 digit number 0 padded on the left


- OR -


    convert *.JPG -delay 10 -morph 10 %05d.morph.jpg

^ We could use imagemagick and that would morph images together, takes all JPG and converts frame 1 to frame 2 with 10 frames in between




Title: Web Developer vs Mobile App Developer
Date: 2014-4-15 1:10
Status: draft
