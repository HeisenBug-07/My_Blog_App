from flask import render_template, request
from myproject import app
from myproject.modles import Posts
from sqlalchemy import desc


@app.route('/')
@app.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    post = Posts.query.order_by(desc(Posts.s_no)).paginate(page=page, per_page=4)
    return render_template('home.html', post=post)


@app.route('/info')
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(debug=True)