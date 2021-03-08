from flask import Flask, render_template, flash, redirect, url_for, session,request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt 

from data import Articles
app = Flask(__name__)

# config mysql
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'myflaskapp'
# allow the calls to return key value pairs rather than tuples 
app.config['MYSQL_CURSORCLASS']= 'DictCursor'

# init mysql
mysql= MySQL(app)


Articles = Articles()
# This will create a route at /, which return the value index
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about ():
    return render_template('about.html')

@app.route('/articles')
def articles ():
    return render_template('articles.html',articles = Articles )

@app.route('/article/<string:id>/')
def article (id):
    return render_template('article.html',id = id )

class RegisterForm(Form):
    name = StringField('Name', validators=[validators.Length(min=1, max=25)])
    username  = StringField('Username', validators=[validators.Length(min=4, max=25)])
    email  = StringField('Email', validators=[validators.Length(min=5, max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Password does not match')
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register ():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor 
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)', (name, email,username,password))
        # close 
        mysql.connection.commit()
        cur.close()
        flash('you are now registered and can log in', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form = form)


if __name__ == '__main__':
    app.secret_key = '123123'
    app.run(debug = True)