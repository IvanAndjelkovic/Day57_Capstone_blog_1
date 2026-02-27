from flask import Flask, render_template

import requests


app = Flask(__name__)

blog_url="https://api.npoint.io/c790b4d5cab58020d391"

response=requests.get(blog_url)
blog_post_json=response.json()

@app.route('/')
def home():
    # blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    
    # response=requests.get(blog_url)
    # blog_post_json=response.json()

    return render_template("index.html", blog_posts=blog_post_json)

@app.route('/<blog_number>')
def blog(blog_number):
    blog_number=int(blog_number) - 1
    if int(blog_number) > len(blog_post_json):
        pass
    else:
        return render_template("post.html", blog_posts=blog_post_json,number=blog_number)


if __name__ == "__main__":
    app.run(debug=True)
