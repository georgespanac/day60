import smtplib

from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/734993bbc38cf4272af7").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message_sent = True;
        MY_EMAIL = "geo.butnaru@gmail.com"
        MY_PASSWORD = "ppooonwqdywylznt"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            msg = f"Subject:Messge from {request.form['name']}\n\n{request.form['message']}"
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg)
    else:
        message_sent = False

    return render_template("contact.html", message_sent=message_sent)


if __name__ == "__main__":
    app.run(debug=True)
