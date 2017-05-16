# cadasta-blog
A blog to share my experience as an open source Outreachy intern at Cadasta.

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

# How to add a post and update the rss.xml

1) Clone the master branch in your local machine with 
```
$ git clone git@github.com:laura-barluzzi/cadasta-blog.git
```
and enter in the folder by typing the following in the terminal
```
$ cd cadasta-blog
```

2) Add a new post inside the `data.json` file. A new post is simply a new list item in `data.json["content"]`. Save the file.

3) In your terminal run `rss_feed_generator.py`
```
$ python3 rss_feed_generator.py
```
Note: this updates the `rss.xml` file with the new changes from `data.json`. It requires Python3.

4) Then you need to add, commit and push the new changes.
```
$ git add .
$ git commit -m "add post and its rss feed"
$ git push
```
