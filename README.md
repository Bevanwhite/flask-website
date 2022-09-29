# flask-website
making my own way to learn from [`Corey Shafer`](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) youtube videos and put my knowledge into it.

### install pip in arch linux
`sudo pacman -S  python-pip`

### create a venv using pip
`python -m venv venv`

### create a gitignore file remove the venv folder
`touch .gitignore`

### to activate the vitual environment
`. venv/bin/activate`

### how to run the flask code
`export FLASK_APP=origami.py`<br>
then use `flask run`

### how to on the debug mode
`export FLASK_DEBUG=1`

### how to on the flask debug using the script it self
```
if '__name__' == '__main__':
    app.run(debug=True)
```
run this command terminal <br>
`python origami.py`

`origami variable` - is list of dictionaries

how to put the jinja2 code into html

on the base.html
`{% block content %} {% endblock content %}`

on other `<html>` files that you want to show your code,
```
{% extends "layout.html"%}
{% block content %}
    <!-- your code goes here -->
{% endblock content %}
```

coming to css files

there is to ways that you can add the css file. first of all you need to create a folder called<br> static and then you can access it from there.

so what i have done is i have make it like `static\css' <br>
inside that you can find the style.css. 

then on templates goto the layout.html <br> 
add these codes<br>
first one<br>
`<link rel="stylesheet" href="static/css/style.css" />`<br>
below code is python way of adding css<br>
`<link rel="stylesheet" type="text/css" href="{{url_for('static',filename='css/style.css')}}">`<br>
