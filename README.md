# fast_api_bootstrap
Personnal project to learn how to render custom html within fastapi.
use of Bootstrap to customise layout of html


# Project tree:
├── app
│   ├── __init__.py
│   ├── library
│   │   ├── helpers.py
│   │   ├── __init__.py
│   ├── main.py
│   ├── pages
│   │   ├── about.md
│   │   ├── home.md
│   │   └── info.md
│   └── routers
│       ├── accordion.py
│       ├── __init__.py
│       ├── twoforms.py
│       └── unsplash.py
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   ├── mystyle.css
│   │   └── style3.css
│   └── images
│       ├── favicon.ico
└── templates
    ├── accordion.html
    ├── base.html
    ├── include
    │   ├── sidebar.html
    │   └── topnav.html
    ├── page.html
    ├── twoforms.html
    └── unsplash.html

# app :
## library :
helpers.py :
You can add all your helper codes in the app/library directory.
Here we add a helper function. This function takes a markdown file in the app/pages and convert it to HTML and return it..
## pages :
All the website pages written in markdown format
## routers
https://fastapi.tiangolo.com/tutorial/bigger-applications/

Structure API code and create a different path per API module (main, accordion, twoforms....)

## twoforms.py
Line 1: We import Form from fastapi.
Line 2: Add HTMLResponse for rendering HTML.
Line 15 & 21: We create two different end-points.
Line 16 & 22: We specify the number parameter. The number field will be uploaded as form data and receive it in each post function.

same concept apply for other routers

# static :
## css :
Custom CSS Code for html pages
## images :
Project images

# templates :
All html template used by fastapi to display api results and forms.

## include
Components bootstraps

## base html :
Main Jinja template with common code used in each different website pages.
Jinja template uses {% block head %}{% end block %}, {% block page_content %}{% endblock %}
and {% block scripts %}{%endblock %} to insert contents from a child HTML.
Use {% include 'include/sidebar.html' %} to include another HTML file.

## page.html
{% extends "base.html" %} tells the template engine that this template “extends” another template, the base.html
 The{{ super() }} makes sure to load the parent contents

## twoforms :
Line 14–16: Jinja’s if-statement to show the result.
By using {{variable}}, we show the value sent from the app/twoforms.py file.

Same concept apply for accordion

## Global information :
If new pages are created :
 Uupdate templates/include/sidebar and templates/include/topnav.
Allows us to add this pages in the navbar and side bar
