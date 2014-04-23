Title: Ignore herokuapp.com domain in nginx
Date: 2014-4-22 15:10
Category: snippets
Tags: heroku, nginx, snippets


I was having some trouble with duplicate content from my blog `ericcarmichael.com` being replicated on `myapp.herokuapp.com`.

I added this little bit to my [Pelican buildout fork](https://github.com/ckcollab/heroku-buildpack-pelican) and now
 requests directly to the `herokuapp.com` domain are denied by nginx!


    http {
        server {
            listen <%= ENV["PORT"] %> default;
            deny all;
        }

        server {
            listen <%= ENV["PORT"] %>;

            server_name yourapp.com www.yourapp.com;
        }
    }


The first server block catches all and denies them, the second only accepts requests from where we want! Yay!
