from flask import Flask, render_template

app = Flask(__name__)

origami = [
    {
        'author' : 'Jeffery White',
        'title': 'Origami Post 1',
        'content': 'first origmai post of the day',
        'date_posted': 'April 20, 2018'
    },
    {
        'author' : 'Dulika Foneska',
        'title': 'Origami Post 2',
        'content': 'Second origmai post of the day',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=origami)

@app.route("/about")
def about():
    return render_template('about.html', title='Cascade')


if __name__ == '__main__':
    app.run(debug=True)