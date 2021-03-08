from flask import Flask, render_template, flash, redirect, url_for, session,request, logging
from flask.logging import create_logger
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt 
from functools import wraps
from data import Articles

app = Flask(__name__)
LOG = create_logger(app)
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

# Home
@app.route('/')
def index():
    return render_template('home.html')

# About
@app.route('/about')
def about ():
    return render_template('about.html')

# Articles
@app.route('/articles')
def articles ():
    return render_template('articles.html',articles = Articles )

# Single article 
@app.route('/article/<string:id>/')
def article (id):
    return render_template('article.html',id = id )

# register form class
class RegisterForm(Form):
    name = StringField('Name', validators=[validators.Length(min=1, max=25)])
    username  = StringField('Username', validators=[validators.Length(min=4, max=25)])
    email  = StringField('Email', validators=[validators.Length(min=5, max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message = 'Password does not match')
    ])
    confirm = PasswordField('Confirm Password')

# user registration 
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

# user login
@app.route('/login', methods=['GET', 'POST'])
def login ():
    app.logger.info('-------------from login route-------------')

    if request.method == "POST" :
        username = request.form['username']
        password_check = request.form['password']
        # create cursor 
        cur = mysql.connection.cursor()
        result = cur.execute('SELECT * FROM users WHERE username =%s',[username] )

        if result> 0:
            data= cur.fetchone()
      
            password = data['password']
            # compare the password
            if sha256_crypt.verify(password_check, password):
                session['logged_in']= True
                session['username'] = username

                flash('you are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                return render_template('login.html', error= 'Password did not match')
        else:
            return render_template('login.html', error= 'user not found')

        # close 
        mysql.connection.commit()
        cur.close()
   
        # flash('you are now logged in', 'success')

    return render_template('login.html')

# check if logged in
def is_logged_in(f):
    @wraps(f)
    def wrap (*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return redirect(url_for('login')) 
    return wrap


# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard ():
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM articles')
    articles = cur.fetchall()
    if result>0:
        return render_template('dashboard.html', articles= articles)
    else:
        return render_template('dashboard.html', msg ="No Articles Found")
    cur.close()

# Logout
@app.route('/logout')
@is_logged_in
def logout ():
    session.clear()
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', validators=[validators.Length(min=1, max=255)])
    body  = TextAreaField('Body', validators=[validators.Length(min=40)])

# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article ():
    form = ArticleForm(request.form)
    if request.method =='POST' and form.validate():
        title= form.title.data
        body= form.body.data

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO  articles(title, body, author) VALUES(%s,%s,%s)',(title, body, session['username']))
        mysql.connection.commit()
        cur.close()
        flash('Article Created', 'success')
        return redirect(url_for('dashboard'))
    return render_template('add_article.html', form=form)



if __name__ == '__main__':
    app.secret_key = '123123'
    app.run(debug = True)
    
    