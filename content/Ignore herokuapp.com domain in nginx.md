Title: Ignore herokuapp.com domain in nginx
Date: 2014-4-23 01:50
Category: snippets
Tags: heroku, nginx, snippets
Summary: I was having some trouble with duplicate content from my blog `ericcarmichael.com` being replicated on `ericcarmichael.herokuapp.com`. <br><br> I added this little bit to my [Pelican buildout fork](https://github.com/ckcollab/heroku-buildpack-pelican) and now requests to `myapp.herokuapp.com` domain are denied by nginx!



I was having some trouble with duplicate content from my blog `ericcarmichael.com` being replicated on `ericcarmichael.herokuapp.com`.

I added this little bit to my [Pelican buildout fork](https://github.com/ckcollab/heroku-buildpack-pelican) and now
 requests to `myapp.herokuapp.com` domain are denied by nginx!


    http {
        server {
            listen <%= ENV["PORT"] %> default;
            rewrite ^ $scheme://myapp.com$request_uri? permanent;
        }

        server {
            listen <%= ENV["PORT"] %>;

            server_name myapp.com www.myapp.com;
        }
    }


The first server block catches all and denies them, the second only accepts requests from where we want! Yay!
