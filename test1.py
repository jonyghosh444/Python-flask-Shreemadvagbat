from flask import Flask, render_template, request, session, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail
import os
from werkzeug.utils import secure_filename
import math

with open("config.json","r") as c:
    params = json.load(c)["params"]
local_server = True
app = Flask(__name__)
'''secret key'''
app.secret_key = 'the random string'
'''upload'''
app.config['UPLOAD_FOLDER'] = params['upload_loacation']
'''for flask_mail'''
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params["gmail_user"],
    MAIL_PASSWORD = params["gmail_pass"]
)
mail = Mail(app)

if(local_server):
    '''  'mysql+pymysql://username:password@localhost/db_name' '''
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)

"""Table"""

class Massage(db.Model):
    '''sno,name,email,phoneno,massage,date'''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phoneno = db.Column(db.String(16), nullable=False)
    massage = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=True)

class Chapter(db.Model):

    srlno = db.Column(db.Integer, primary_key=True)
    chapno = db.Column(db.String(1000), nullable=False)
    chapname = db.Column(db.String(1000), nullable=False)

class Slok(db.Model):
    """chapnoen,chapnobn,chapnamebn,slksnoen,slksnobn,slok,anubad,tatporjo"""

    allslkno = db.Column(db.Integer, primary_key=True)
    chapnoen = db.Column(db.Integer, nullable=False)
    chapnobn = db.Column(db.String(1000), nullable=False)
    chapnamebn = db.Column(db.String(1000), nullable=False)
    slksnoen = db.Column(db.Integer, nullable=False)
    slksnobn = db.Column(db.String(1000), nullable=False)
    slok = db.Column(db.String(1000), nullable=False)
    anubad = db.Column(db.String(1000), nullable=False)
    tatporjo = db.Column(db.String(1000), nullable=False)

class Blog(db.Model):
    """blogsno,title,content,user,date"""
    blogsno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(999999), nullable=False)
    content = db.Column(db.String(999999), nullable=False)
    user = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=True)
    banite = db.Column(db.String(50), nullable=True)





"""ADMIN"""


@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():

    if('user' in session and session['user'] == params['admin_uname']):
        chapter = Chapter.query.all()
        return render_template('admin dashboard.html', params=params,chapter=chapter)

    if request.method=='POST':
        username = request.form.get('uname')
        password = request.form.get('pass')
        if(username==params['admin_uname'] and password==params['admin_pass']):
            session['user'] = username
            chapter = Chapter.query.all()

            return render_template('admin dashboard.html', params=params, chapter=chapter)




    return render_template('adminlogin.html', params=params)

@app.route('/form/<string:srlno>', methods = ['GET', 'Post'])

def form(srlno):
    if ('user' in session and session['user'] == params['admin_uname']):
        chap = Chapter.query.filter_by(srlno=srlno).first()
        serial = chap.srlno
        chapterno = chap.chapno
        chaptername = chap.chapname
        if (request.method == 'POST'):
            '''Add entry to the database'''
            sloknoen = request.form.get('sloknoen')
            sloknobn = request.form.get('sloknobn')
            slok = request.form.get('slok')
            anubad = request.form.get('anubad')
            tatporjo = request.form.get('tatporjo')

            """chapnoen,chapnobn,chapnamebn,slksnoen,slksnobn,slok,anubad,tatporjo"""

            entry = Slok(chapnoen=serial, chapnobn=chapterno, chapnamebn=chaptername, slksnoen=sloknoen, slksnobn=sloknobn,
                         slok=slok, anubad=anubad, tatporjo=tatporjo)
            db.session.add(entry)
            db.session.commit()
            return render_template('form.html', params=params, chap=chap)

        return render_template('form.html', params=params, chap=chap, serial=serial)



@app.route('/newchap',methods = ['GET', 'POST'])
def add_new_chap():
    if ('user' in session and session['user'] == params['admin_uname']):
        if (request.method == 'POST'):
            '''Add entry to the database'''

            chapnob = request.form.get('chapnob')
            chapnoe = request.form.get('chapnoe')
            chapname = request.form.get('chapname')

            '''srlno,chapno,chapname'''

            entry = Chapter(srlno=chapnoe, chapno=chapnob, chapname=chapname)
            db.session.add(entry)
            db.session.commit()

        return render_template('newchap.html', params=params)

"""Admin Book page"""

@app.route('/chappage/<string:srlno>', methods = ['GET', 'Post'])

def chap_page(srlno):
    if ('user' in session and session['user'] == params['admin_uname']):
        chap = Chapter.query.filter_by(srlno=srlno).first()
        serial = chap.srlno
        slok = Slok.query.filter_by(chapnoen=serial)

        return render_template('chappage.html', params=params, chap=chap, serial=serial, slok=slok)


@app.route('/edit/<string:srlno>/<string:allslkno>', methods = ['GET', 'Post'])

def Edit_slok(srlno,allslkno):
    if ('user' in session and session['user'] == params['admin_uname']):
        chap = Chapter.query.filter_by(srlno=srlno).first()
        slok = Slok.query.filter_by(allslkno=allslkno).first()
        if request.method == "POST":
            updated_slok = request.form.get('slok')
            updated_anubad = request.form.get('anubad')
            tatporjo = request.form.get('tatporjo')
            slok = Slok.query.filter_by(allslkno=allslkno).first()
            slok.slok = updated_slok
            slok.anubad = updated_anubad
            slok.tatporjo = tatporjo
            db.session.commit()
            return redirect('/edit/' + srlno + '/' + allslkno)

        return render_template('editslok.html', params=params, slok=slok, chap=chap)

@app.route('/fullslok/<string:srlno>/<string:allslkno>', methods = ['GET', 'Post'])

def Full_slok(srlno,allslkno):
    if ('user' in session and session['user'] == params['admin_uname']):
        chap = Chapter.query.filter_by(srlno=srlno).first()
        slok = Slok.query.filter_by(allslkno=allslkno).first()

        return render_template('fullslok.html', params=params, slok=slok, chap=chap)

@app.route('/delete/<string:srlno>/<string:allslkno>', methods = ['GET', 'Post'])

def Slok_delete(srlno,allslkno):
    if ('user' in session and session['user'] == params['admin_uname']):
        Chapter.query.filter_by(srlno=srlno).first()
        slok = Slok.query.filter_by(allslkno=allslkno).first()
        db.session.delete(slok)
        db.session.commit()

        return redirect('/chappage/'+srlno)



@app.route('/upload', methods = ['GET', 'Post'])

def File_uploader():
    if ('user' in session and session['user'] == params['admin_uname']):
        if request.method == "POST":
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully"
        return render_template('imageupload.html')

@app.route('/logout', methods = ['GET', 'Post'])

def Logout():
    session.pop('user')
    return redirect('/dashboard')

"""ADMIN BLOG page"""

@app.route('/adminblog', methods = ['GET', 'Post'])

def Admin_blog():
    if ('user' in session and session['user'] == params['admin_uname']):
        blog = Blog.query.all()
        lastpage = math.ceil(len(blog) / int(params['userblog_post_num']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        blog = blog[(page - 1) * int(params['userblog_post_num']):(page - 1) * int(params['userblog_post_num']) + int(
            params['userblog_post_num'])]
        if (page == 1):
            prev = "#"
            next = "/blog?page=" + str(page + 1)
        elif (page == lastpage):
            prev = "/blog?page=" + str(page - 1)
            next = "#"
        else:
            prev = "/blog?page=" + str(page - 1)
            next = "/blog?page=" + str(page + 1)

        
        return render_template('Adminblog.html',params=params,blog=blog,prev=prev,next=next)

@app.route('/createblog', methods=['GET', 'Post'])

def Admin_create_blog():
    if ('user' in session and session['user'] == params['admin_uname']):
        if (request.method == 'POST'):
            '''Add entry to the database'''

            user = request.form.get('user')
            title = request.form.get('title')
            banite= request.form.get('title')
            content = request.form.get('content')

            """blogsno,title,content,user,date"""

            entry = Blog(title=title,banite=banite, user=user, content=content,date=datetime.now())
            db.session.add(entry)
            db.session.commit()
        return render_template('createblog.html')


@app.route('/admin_full_blog/<string:sno>', methods=['GET', 'Post'])
def Admin_full_blog(sno):
    if ('user' in session and session['user'] == params['admin_uname']):
        blog = Blog.query.filter_by(blogsno=sno).first()

        return render_template('Adminfullblog.html', params=params, blog=blog)

@app.route('/editblog/<string:blogsno>', methods = ['GET', 'Post'])

def Edit_blog(blogsno):
    if ('user' in session and session['user'] == params['admin_uname']):
        blog = Blog.query.filter_by(blogsno=blogsno).first()
        if request.method == "POST":
            title = request.form.get('title')
            banite = request.form.get('banite')
            content = request.form.get('content')
            user = request.form.get('user')
            blog = Blog.query.filter_by(blogsno=blogsno).first()
            blog.title = title
            blog.banite = banite
            blog.content = content
            blog.user = user
            db.session.commit()
            return redirect('/editblog/'+blogsno)

        return render_template('editblog.html', params=params, blog=blog)

@app.route('/delete/<string:blogsno>', methods = ['GET', 'Post'])

def Blog_delete(blogsno):
    if ('user' in session and session['user'] == params['admin_uname']):
        blog = Blog.query.filter_by(blogsno=blogsno).first()
        db.session.delete(blog)
        db.session.commit()

        return redirect('/adminblog')

"""USER"""


@app.route('/')
def home():
    
    return render_template('index.html', params=params)


@app.route('/about')
def about():
        return render_template('about.html', params=params)


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''

        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        '''sno,name,email,phoneno,massage,date'''

        entry = Massage(name=name, email=email, phoneno=phone,  massage=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New message in shrimodvogbot" +" from "+name,
                          sender=email,
                          recipients=[params["gmail_user"]],
                          body = message+"\n"+"phone:-"+phone)

    return render_template('contact.html', params=params)


"""Grantha"""

@app.route('/grantha', methods = ['GET', 'POST'])
def Grantha():
    chapter = Chapter.query.all()
    return render_template('grantha.html', params=params,chapter=chapter)

"""Book page"""

@app.route('/userchappage/<string:srlno>', methods = ['GET', 'Post'])

def user_chap_page(srlno):
    chap = Chapter.query.filter_by(srlno=srlno).first()
    serial = chap.srlno
    slok = Slok.query.filter_by(chapnoen=serial)

    return render_template('Userchappage.html', params=params, chap=chap, serial=serial, slok=slok)


"""USER SLOK DETAILS"""

@app.route('/userfullslok/<string:srlno>/<string:allslkno>', methods = ['GET', 'Post'])

def User_Full_slok(srlno,allslkno):
    chap = Chapter.query.filter_by(srlno=srlno).first()
    slok = Slok.query.filter_by(allslkno=allslkno).first()

    return render_template('Userfullslok.html', params=params, slok=slok, chap=chap)


'''Blog'''

@app.route('/blog', methods=['GET', 'Post'])

def Blog_page():
    blog = Blog.query.filter_by().all()
    lastpage = math.ceil(len(blog)/int(params['userblog_post_num']))
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    blog = blog[(page-1)*int(params['userblog_post_num']):(page-1)*int(params['userblog_post_num'])+int(params['userblog_post_num'])]
    if (page==1):
        prev = "#"
        next = "/blog?page="+str(page+1)
    elif(page==lastpage):
        prev = "/blog?page="+str(page-1)
        next = "#"
    else:
        prev = "/blog?page="+str(page-1)
        next = "/blog?page="+str(page+1)



    return render_template('blog.html', params=params,blog=blog, prev=prev,next=next)


@app.route('/User_full_blog/<string:sno>', methods=['GET', 'Post'])

def User_full_blog(sno):
    blog = Blog.query.filter_by(blogsno=sno).first()

    return render_template('user_full_blog.html', params=params, blog=blog)





if __name__ == '__main__':
    app.run(debug= True)

