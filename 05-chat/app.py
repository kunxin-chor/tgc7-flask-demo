from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)

messages = []


@app.route('/')
def chatroom():
    print(messages)
    return render_template('chatroom.template.html', messages=messages)


@app.route('/', methods=["POST"])
def post_to_chatroom():
    username = request.form.get('username')
    chat = request.form.get('chat-message')
    msg = {
        "by": username,
        "content": chat
    }
    messages.append(msg)
    return redirect(url_for('chatroom'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
