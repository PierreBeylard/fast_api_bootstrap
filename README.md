# fast_api_bootstrap
Bootstrap fast_api

base html :
Jinja template uses {% block head %}{% end block %}, {% block page_content %}{% endblock %}
and {% block scripts %}{%endblock %} to insert contents from a child HTML.
Use {% include 'include/sidebar.html' %} to include another HTML file.

page.html
{% extends "base.html" %} tells the template engine that this template “extends” another template, the base.html
 The{{ super() }} makes sure to load the parent contents

helpers.py :
You can add all your helper codes in the app/library directory.
Here we add a helper function. This function takes a markdown file in the app/pages and convert it to HTML and return it..

If new pages are created :
 Uupdate templates/include/sidebar and templates/include/topnav.


routers :
https://fastapi.tiangolo.com/fr/tutorial/bigger-applications/
permet de structurer le code de l'api
twoforms
Line 1: We import Form from fastapi.
Line 2: Add HTMLResponse for rendering HTML.
Line 15 & 21: We create two different end-points.
Line 16 & 22: We specify the number parameter. The number field will be uploaded as form data and receive it in each post function.
