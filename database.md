how to create a database to use in flask the easy way is to install `flask-sqlalchemy`<br>
how to install - 
```
pip install flask-sqlalchemy
```

after that you have to import the sqlalchemy libary to your app
```
from sqlalchemy import SQLAlchemy
```

then create the database URI for the application
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
```

then create a object from the SQLAlchemy class
```
db = SQLAlchemy(app)
```
to create the database follow this commands
```
from origami import db - # this can be vairy compare to your main file name
db.create_all() - # to create the database
```

to add the class and access data tables
```
from origami import User, Post
user_1 = User(username='Dulika',email='d@fonseka.com',password='password')
db.session.add(user_1) - # to add a user to the database but not save in the database
db.session.commit() - to save the added file to the database
```

how add data to the database
```
User.query.all()
User.query.first()
User.query.filter_by(username='bevan').first()

user = User.query.filter_by(username='bevan').first()
user.id
```

how to drop all that you have created
```
db.drop_all()
```