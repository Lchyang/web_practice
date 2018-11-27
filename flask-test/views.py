#conding: utf-8

from flask import Flask,render_template,request
from flask import redirect
from flask import session
from flask import url_for
from decorators import login_required
import config
from exts import db
from models import User,Article,Comment



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
@login_required
def index():
    content = {
        'articles':Article.query.order_by('-create_time').all()
    }
    return render_template('index.html',**content)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')

        tel = User.query.filter(User.telephone==telephone).first()
        passw = User.query.filter(User.password==password).first()
        if tel and passw:
            session['user_id'] = tel.id

            session.permanent=True
            return redirect(url_for('index'))
        else:
            return 'mi ma huo yong hu ming cuo wu '


@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        tel = User.query.filter(User.telephone == telephone).first()
        if tel:
            return 'shoujihao yijing zhuce '
        else:
            if password2 != password1:
                return 'ma ma buyizhi '
            else:
                user = User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))



@app.route('/logout/')
def logout():
    # session.pop('user')
    # del session['user']
    session.clear()
    return redirect(url_for('login'))


@app.route('/article/',methods=['GET','POST'])
@login_required
def article():
    if request.method == 'GET':
        return render_template('article.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        article = Article(title=title,content=content)
        db.session.add(article)
        db.session.commit()
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        Article.author = user
        return redirect(url_for('index'))


@app.route('/detail/<article_id>')
def detail(article_id):
    article_model = Article.query.filter(Article.id == article_id).first()
    return render_template('detail.html',article=article_model)



@app.route('/comment/',methods=['POST'])
@login_required
def comment():
    content = request.form.get('comment_content')
    article_id = request.form.get('article_id')
    comment = Comment(content=content)
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    comment.author = user
    article = Article.query.filter(Article.id == article_id).first()
    comment.article = article
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('detail',article_id=article_id))



