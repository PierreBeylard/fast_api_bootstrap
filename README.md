https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864

# fast_api_bootstrap
Personnal project to learn how to render custom html within fastapi.
use of Bootstrap to customise layout of html


# Project tree:
├── app <br />
│   ├── __init__.py   <br />
│   ├── library <br />
│   │   ├── helpers.py <br />
│   │   ├── __init__.py <br />
│   ├── main.py <br />
│   ├── pages <br />
│   │   ├── about.md <br />
│   │   ├── home.md <br />
│   │   └── info.md <br />
│   └── routers <br />
│       ├── accordion.py <br />
│       ├── __init__.py <br />
│       ├── twoforms.py <br />
│       └── unsplash.py <br />
├── README.md <br />
├── requirements.txt <br />
├── static <br />
│   ├── css <br />
│   │   ├── mystyle.css <br />
│   │   └── style3.css <br />
│   └── images <br />
│       ├── favicon.ico <br />
└── templates <br />
    ├── accordion.html <br />
    ├── base.html <br />
    ├── include <br />
    │   ├── sidebar.html <br />
    │   └── topnav.html <br />
    ├── page.html <br />
    ├── twoforms.html <br />
    └── unsplash.html <br />

# app :
## library :
helpers.py : <br />
You can add all your helper codes in the app/library directory. <br />
Here we add a helper function. This function takes a markdown file in the app/pages and convert it to HTML and return it..
## pages :
All the website pages written in markdown format
## routers
https://fastapi.tiangolo.com/tutorial/bigger-applications/

Structure API code and create a different path per API module (main, accordion, twoforms....)

## twoforms.py
Line 1: We import Form from fastapi. <br />
Line 2: Add HTMLResponse for rendering HTML. <br />
Line 15 & 21: We create two different end-points. <br />
Line 16 & 22: We specify the number parameter. The number field will be uploaded as form data and receive it in each post function. <br />

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
Main Jinja template with common code used in each different website pages. <br />
Jinja template uses {% block head %}{% end block %}, {% block page_content %}{% endblock %} <br />
and {% block scripts %}{%endblock %} to insert contents from a child HTML. <br />
Use {% include 'include/sidebar.html' %} to include another HTML file. <br />

## page.html
{% extends "base.html" %} tells the template engine that this template “extends” another template, the base.html <br />
 The{{ super() }} makes sure to load the parent contents

## twoforms :
Line 14–16: Jinja’s if-statement to show the result. <br />
By using {{variable}}, we show the value sent from the app/twoforms.py file.

Same concept apply for accordion

## Global information :
If new pages are created : <br />
 Uupdate templates/include/sidebar and templates/include/topnav. <br />
Allows us to add this pages in the navbar and side bar
