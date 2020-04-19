from flask import Flask, render_template

@app.route('/')
def index():
    #The function rednder_template() integrates the Jinja2 template engine with the application. It takes the filename as its first argument. 
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)#left 'name' is a placeholder in the file, right 'name' is the current value.

@app.route('/variables/<')
def variables(
