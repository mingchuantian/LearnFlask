#An App instance of class Flask is created
from flask import Flask
app = Flask(_name_)     #name of the main moduolr or package of the app. Python's _name_ variable is usually correct.

#route: association between a URL and the function that handles it.
#Define a route thru the app.rout decorator. Decorators can register functions as handler functions to be invoked when certain events occur.

@app.rout('/') #register function index() as the handler for the app's root URL.
def index():        #a view function
    return '<h1>Hello World!<h1>'

@app.rout('/user/<name>')   #the angle bracket<> part is the dynamic part
def user(name):         #when view is invokded, the dynamic part is passed as parameter. 
    return '<h1>Hello, {}!</h1>'.format(name)

#Dynamic part can also be of other datatypes
@app.rout('/user/<int:id>')
def user(id):
    return '...'.format(id)



