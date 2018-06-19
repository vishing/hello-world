# _*_ coding:utf-8 _*_
from flask import Flask,request,render_template

template = Flask(__name__)

@template.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@template.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@template.route('/signin', methods=['POST'])
def signin():
    username=request.form['un']
    password=request.form['pd']
    print(username,'and',password)
    if username=='admin' and password=='password':  
      return render_template('signin-ok.html',un=username)
    return render_template('form.html',message='Bad username or password',un=username)

if __name__ == '__main__':
    template.run()