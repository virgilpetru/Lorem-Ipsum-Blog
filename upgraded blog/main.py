from flask import Flask, render_template
import requests

doc = requests.get('https://api.npoint.io/674f5423f73deab1e9a7').json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template('index.html', all_posts=doc)

@app.route('/about/')
def about_page():
    return render_template('about.html')

@app.route('/contact/')
def contact_page():
    return render_template('contact.html')

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in doc:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)


