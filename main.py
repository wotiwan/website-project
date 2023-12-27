import os
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Post, Likes
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from . import db
from flask import current_app as app

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

main = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@main.route('/')
def index():
    posts = Post.query.all()
    postarr = []
    for i in posts:
        likes = Likes.query.filter_by(post_id=i.id).count()
        postarr.append(tuple([i,likes]))
    return render_template('index.html', posts=postarr[::-1])

@main.route('/profile')
@login_required
def profile():
    posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', name=current_user.name, posts=posts)

@main.route('/settings', methods=["POST"])
@login_required
def settings():
    if request.method == 'POST':
        cur_password = request.form['cur_password']
        if check_password_hash(current_user.password, cur_password):
            new_password = request.form['new_password']
            name = request.form['name']
            file = request.files['ava_pic']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = str(current_user.id) + '.' + filename.rsplit('.', 1)[1]
                if file and current_user.icon!="base.png":
                    os.remove(os.path.join('/home/ivan/project/static/users/', current_user.icon))
                file.save(os.path.join('/home/ivan/project/static/users/', filename))
                if file:
                    current_user.icon = filename
            if new_password:
                current_user.password = generate_password_hash(new_password, method='pbkdf2')
            if name:
                current_user.name = name
            db.session.commit()
    return redirect(url_for('main.profile'))

@main.route('/new_post', methods=['GET','POST'])
@login_required
def new_post():
    if request.method == 'POST':
        post_desc = request.form['post_desc']
        file = request.files['post_pic']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_post = Post(img=filename,description=post_desc, user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            filename = str(new_post.id)+'.'+filename.rsplit('.', 1)[1]
            new_post.img = filename
            file.save(os.path.join('/home/ivan/project/static/posts/', filename))
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/edit/<post_id>', methods=['POST'])
@login_required
def edit(post_id):
    post = Post.query.get(post_id)
    new_description = request.form['editdesc']
    new_pic = request.files['editpic']
    if new_pic and allowed_file(new_pic.filename):
        filename = secure_filename(new_pic.filename)
        filename = str(post_id)+'.'+filename.rsplit('.', 1)[1]
        os.remove(os.path.join('/home/ivan/project/static/posts/', post.img))
        new_pic.save(os.path.join('/home/ivan/project/static/posts/', filename))
        post.img = filename
    post.description = new_description
    db.session.commit()
    return redirect(url_for('main.profile'))

@main.route('/delete/<post_id>')
@login_required
def delete(post_id):
    Likes.query.filter_by(post_id=post_id).delete()
    post = Post.query.get(post_id)
    os.remove(os.path.join('/home/ivan/project/static/posts', post.img))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('main.profile'))

@main.route('/like/<post_id>')
@login_required
def like(post_id):
    like = Likes.query.filter_by(user_id=current_user.id, post_id=post_id).first()
    if like:
        db.session.query(Likes).filter(Likes.id==like.id).delete()
    else:
        new_like = Likes(user_id=current_user.id, post_id=post_id)
        db.session.add(new_like)
    db.session.commit()
    return redirect(url_for('main.index'))
