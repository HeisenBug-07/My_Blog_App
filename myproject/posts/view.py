from datetime import datetime
from flask import render_template, redirect, url_for, Blueprint, session
from myproject.modles import db, Posts, Contacts
from myproject.posts.forms import AddPosts, EditPosts, LoginForm
from sqlalchemy import desc

posts_blueprint = Blueprint('Posts', __name__, template_folder='templates/posts')


@posts_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'admin' in session and session['admin'] == 'shubham@gmail.com':
        return redirect(url_for('Posts.dashboard'))
    if form.validate_on_submit():
        if form.password.data == 'hacked' and form.email.data == 'shubham@gmail.com':
            session['admin'] = 'shubham@gmail.com'
            return redirect(url_for('Posts.dashboard'))

    return render_template('login.html', form=form)


@posts_blueprint.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'admin' in session and session['admin'] == 'shubham@gmail.com':
        post = Posts.query.order_by(desc(Posts.s_no)).all()
        return render_template('dashboard.html', post=post)
    return redirect(url_for('Posts.login'))


@posts_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    if 'admin' in session and session['admin'] == 'shubham@gmail.com':
        form = AddPosts()
        if form.validate_on_submit():
            posts = Posts(heading=form.heading.data, sub_heading=form.sub_heading.data,
                          content=form.content.data, date=datetime.utcnow(), slug=form.heading.data)
            db.session.add(posts)
            db.session.commit()

            return redirect(url_for('home'))
        return render_template('add.html', form=form)
    return redirect(url_for('Posts.login'))


@posts_blueprint.route('/post/<string:post_slug>')
def post(post_slug):
    posts = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', posts=posts)


@posts_blueprint.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):
    if 'admin' in session and session['admin'] == 'shubham@gmail.com':
        form = EditPosts()
        post = Posts.query.filter_by(s_no=sno).first()
        if form.validate_on_submit():

            posts = Posts.query.filter_by(s_no=sno).first()
            posts.heading = form.heading.data
            posts.sub_heading = form.sub_heading.data
            posts.content = form.content.data
            posts.date = datetime.utcnow()
            posts.slug = form.heading.data

            db.session.commit()

            return redirect(url_for('home'))
        return render_template('edit.html', form=form, p=post)
    return redirect(url_for('Posts.login'))


@posts_blueprint.route('/delete/<string:sno>')
def delete(sno):
    if 'admin' in session and session['admin'] == 'shubham@gmail.com':
        post = Posts.query.filter_by(s_no=sno).first()
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('Posts.dashboard'))
    return redirect(url_for('Posts.login'))


@posts_blueprint.route('/feedback')
def feedback():
    if 'admin' in session and session['admin'] == 'shubham@gmail.com':
        f_back = Contacts.query.order_by(desc(Contacts.s_no)).all()
        return render_template('feedback.html', f_back=f_back)
    return redirect(url_for('Posts.login'))


@posts_blueprint.route('/remove/<string:sno>')
def delete_feedback(sno):
    if 'admin' in session and session['admin'] == 'shubham@gmail.com':
        comment = Contacts.query.filter_by(s_no=sno).first()
        db.session.delete(comment)
        db.session.commit()
        return redirect(url_for('Posts.feedback'))
    return redirect(url_for('Posts.login'))


@posts_blueprint.route('/logout')
def logout():
    session.pop('admin')
    return redirect(url_for('home'))
