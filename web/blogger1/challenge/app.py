from flask import Flask, render_template, request, redirect, flash, session
from util import get_db_connection, create_tables, authenticate_user, user_exists, create_user, check_token
import os
from uuid import uuid4
from flask_cors import CORS
from admin import run_pupp


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'my_secret_key')


@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/login')
    if 'token' not in session:
        return redirect('/login')
    user_id = session.get('user_id')
    token = session.get('token')
    if check_token(user_id, token) is False:
        flash('Invalid token.', 'error')
        return redirect('/login')
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        SELECT posts.id, posts.content, users.username, posts.title
        FROM posts 
        INNER JOIN users ON posts.user_id = users.id where posts.user_id = ?
    ''', (user_id,))
    posts = c.fetchall()

    conn.close()

    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate_user(username, password)
        if user:
            session['user_id'] = user['id']
            session['token'] = user['token']
            # Set the current user in session or token mechanism
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if user_exists(username):
            flash('Username already exists.', 'error')
        elif len(password) <8 :
            flash('Password should be at least 8 characters long.', 'error')
        else:
            create_user(username, password)
            flash('Account created successfully!', 'success')
            return redirect('/login')

    return render_template('signup.html')


@app.route('/report/<string:post_id>', methods=['POST'])
def report(post_id):
    if 'user_id' not in session or 'token' not in session or len(post_id) > 6:
        return "something went wrong"
    run_pupp("https://blogger.challenge.alphabit.club/post/" + post_id)
    flash('Report has been sent.', 'success')
    return redirect('/')


@app.route('/add_post', methods=['POST'])
def add_post():
    if 'user_id' not in session or 'token' not in session or not request.form['content'] or not request.form['title']:
        return "something went wrong"
    content = request.form['content']
    title = request.form['title']
    user_id = session.get('user_id')
    id = str(uuid4()).replace('-', '')[2:8]
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO posts (id, content, user_id, title) VALUES (?, ?, ?, ?)",
              (id, content, user_id, title))
    conn.commit()
    conn.close()
    flash('Post has been created.', 'success')
    return redirect('/')


@app.route('/post/<string:post_id>', methods=['GET'])
def get_post(post_id):
    if 'user_id' not in session or 'token' not in session:
        return redirect('/login')
    c = get_db_connection().cursor()
    if session.get('user_id') != 1:
        c.execute("SELECT * FROM posts WHERE id=? and user_id=?",
                  (post_id, session.get('user_id')))
        post = c.fetchone()
    else:
        c.execute("SELECT * FROM posts WHERE id=?",
                  (post_id,))
        post = c.fetchone()
    if not post:
        return "Post not found", 404
    comments = c.execute(
        "SELECT content FROM comments WHERE post_id=? ", (post_id,))
    comments = comments.fetchall()
    print(comments)
    if not post:
        return "Post not found", 404
    return render_template('post.html', post=post, comments=comments)


@app.route('/delete/<string:post_id>', methods=['POST'])
def delete(post_id):
    if 'user_id' not in session or 'token' not in session:
        return "something went wrong"
    user_id = session.get('user_id')
    token = session.get('token')
    if check_token(user_id, token) is False:
        flash('Invalid token.', 'error')
        return redirect('/login')
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM posts WHERE id=? and user_id=? ", (post_id, user_id))
    conn.commit()
    conn.close()
    flash('Post has been deleted.', 'success')
    return redirect('/')


@app.route("/comment/<string:post_id>", methods=["POST"])
def add_comment(post_id):
    if 'user_id' not in session or 'token' not in session or not request.form['content']:
        return "something went wrong"
    content = request.form['content']
    user_id = session.get('user_id')
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO comments (content, user_id, post_id) VALUES (?, ?, ?)",
              (content, user_id, post_id))
    conn.commit()
    conn.close()
    flash('Comment has been created.', 'success')
    return redirect('/post/' + post_id)


create_tables()
if __name__ == '__main__':
    app.run(debug=False)
