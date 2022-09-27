from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'eebb2c58cc974ff7833f182cc71dfd9e'

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


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. please check Username and Password')
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)