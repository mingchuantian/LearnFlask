#An App instance of class Flask is created
from flask import Flask
app = Flask(_name_)     #name of the main moduolr or package of the app. Python's _name_ variable is usually correct.

#route: association between a URL and the function that handles it.
@app.rout('/')
def index():
    return '<h1>Hello World!<h1>'

app.add_url_rule('/','index',index)



