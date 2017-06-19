# cadasta-blog
This is a simple blog where I share my first job experience as a software developer [Outreachy](https://www.gnome.org/outreachy/) intern at [Cadasta](http://cadasta.org).

The frontend for the blog is hosted on [gh-pages](http://c-w.github.io/blog/). It's built using VueJS and MaterializeCSS and pulls data from this repository.

# Data Scheme

```json
{
  "content": [
    {
    "date": "YYYY-MM-DD",
    "summary": "string",
    "title": "string",
    "topics": [
      "string"
    ],
    "type": "string",
    "url": "string"
    }
  ],
  "meta": 
    {
    "title": "string",
    "about": 
       {
        "avatar": "string",
        "blurb": "string"
       }
     }
}
```

# Clone repository in your computer 

If you haven't done it already, in your terminal clone and enter the master branch 
```
$ git clone git@github.com:laura-barluzzi/cadasta-blog.git
$ cd cadasta-blog
```
# How to set up and enter the virtual environment
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

# How to add a post and update the rss.xml
Add a new post inside the `data.json` file. A new post is simply a new list item in `data.json["content"]`. Make sure to save it after you are done. The text in `data.json` applies the [common markdown syntax](https://guides.github.com/features/mastering-markdown/).

In order to update the `rss.xml` file with the new changes from `data.json`, in the terminal you need to run:
```
$ python3 rss_feed_generator.py           # on your machine or if you entered (venv)
or
$ venv/bin/python rss_feed_generator.py   # if venve set up but you don't want to enter
```

# Publishing changes in Git Hub
```
$ git add -p
$ git commit -m "add post and its rss feed"
$ git push
```
