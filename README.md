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
    Flask.app(debug=True)

```