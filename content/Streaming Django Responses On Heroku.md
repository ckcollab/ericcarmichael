Title: Streaming Django Responses on Heroku
Date: 2016-5-17 15:10
Category: web development
Tags: python, web development, django 


Django comes with a nice utility class for returning a stream of responses
back to the user. This is useful for returning subprocess stdout or keeping
up with the progress during processing of some file.

Not enough people use this helper! 

## Streaming Django Responses

Here's a small example:

```python
import time
from django.http import HttpResponse, StreamingHttpResponse

def _valley_girl_stream():
    # Get ready to be streamed 50 seconds of this nonsense
    for _ in range(50):
        yield "like, whatever\n"
        time.sleep(1)

def some_endpoint(request):
    return StreamingHttpResponse(_valley_girl_stream())

```

You pass `StreamingHttpResponse` a generator and it does all of the hard
work for you. So, so handy!

<p align="center" class="image-wrapper">
    <img src="images/valley_girl.jpg" class="img-responsive" alt="Valley Girl">
</p>


## Gotch'ya!
 
Watch out for problems with your WSGI servers and buffering data.

<p align="center" class="image-wrapper">
    <img src="images/buffering.jpg" class="img-responsive" alt="Buffering problems">
    <i><small>Buffering problems</small></i>
</p>

For example, with [Waitress](http://docs.pylonsproject.org/projects/waitress/en/latest/) and this code:

```python
def _watch_process_import(xml_data):
    yield "Starting..."
    for something in whatever_dad:
        yield something
    yield "Done!"


def do_import(request):
    if request.method == 'POST':
        xml_data = request.FILES['file'].read()
        return StreamingHttpResponse(_watch_process_import(xml_data))
```

If you run this with a normal Waitress config, it will not send until the connection is closed and flushed.
To make the messages actually stream realtime, I had to modify the first function:

```python
def _watch_process_import(xml_data):
    # this fills the buffer so the messages start streaming
    yield "@" * 50 * 1024
    
    # and now we get back to business...
    yield "Starting..."
    ...
```

Obviously, that's not very pretty and makes us feel dirty for having to do it.

So, to fix that, add the arg `--send-bytes=1` for Waitress to your `Procfile`, like this:

```
web: waitress-serve --port=$PORT --send-bytes=1 wsgi:application
```


That makes waitress flush the buffer as soon as it contains >= 1 byte, 
aka all the time with no delay!

