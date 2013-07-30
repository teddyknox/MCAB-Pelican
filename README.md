# Rocket Blog

Hosted at blog.rocketlistings.com in an s3 bucket with the same name. It's powered by a Python static site generator called [Pelican](http://docs.getpelican.com/en/3.2/).

This [Getting started](http://docs.getpelican.com/en/3.2/getting_started.html) documentaiton gives a pretty good idea of how how the framework works.

###  Posting Workflow

The general outline is clone, add/edit a post in the `content` folder, test and deploy.

Cloning is pretty straightforward. Next we install the python dependencies with pip. I recommend setting up a virtualenv for the site (`mkvirtualenv rocketblog`). 

    pip install -r requirements.txt

To start working on a post, create a file in the `content` folder. The file's name is not used as its title on the site, but it's still good to be descriptive. Its file extension should be .md, .rst, or .html. 

At the begining of every post file should be metadata associated with the post. The post's  title, post date, category, tags, author, url slug, and summary are all declared in its metadata. Below are metadata templates for the three formats (pulled right from the Pelican docs).

`.md`

	Title: My super title
	Date: 2010-12-03 10:20
	Category: Python
	Tags: pelican, publishing
	Slug: my-super-post
	Author: Alexis Metaireau
	Summary: Short version for index and feeds

	This is the content of my super blog post.

`.rst`

    My super title
    ##############

    :date: 2010-10-03 10:20
    :tags: thats, awesome
    :category: yeah
    :slug: my-super-post
    :author: Alexis Metaireau
    :summary: Short version for index and feeds

    This is the content I think.

`.html`

    <html>
        <head>
    	    <title>My super title</title>
    	    <meta name="tags" contents="thats, awesome" />
    	    <meta name="date" contents="2012-07-09 22:28" />
    	    <meta name="category" contents="yeah" />
    	    <meta name="author" contents="Alexis Métaireau" />
    	    <meta name="summary" contents="Short version for index and feeds" />
    	</head>
    	<body>
                This is the content of my super blog post.
    	</body>
    </html>

All the details of how to do syntax highlighting and internal file linking is described in the pelican documentation.

To test, run `make html` and then `make serve` from the project directory. Normally you would have to go through this process every time you wanted to see changes in the files reflected, but for active develoment there's the devserver, which automatically recompiles the site whenever it detects a single file has changed. Run it with `make devserver`. Stop it with `./develop_server.sh stop`. Sometime you might have to stop the server twice... it's a little weird.

If you commit and push then I can deploy for now. If you're super interested in deployment look at [http://lexual.com/blog/setup-pelican-blog-on-s3/](http://lexual.com/blog/setup-pelican-blog-on-s3/).

