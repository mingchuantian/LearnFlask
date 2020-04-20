#links can be distributed dynamically by 'url_for()' function.

@app.route('/')
def index():
    respone = make_response('<p>this is the index</p>')
    response.status_code(200)
    return reponse

#url_for('user', name='john') will return /user/john
#url_for('index') will return /
#url_for('user', name='john', _external=True) will return http://localhost:5000/user/john

#url_for('user',name='john', page=2, version=1) will return /user/john?page=2&version=1

#!!! static files can also be retrieved using the auto-generated URLs!!!
#url_for('static', filename='css/style.css', _external\True)  will return http://localhost:5000/static/css/style.css
#Flask looks for static files in a subdirectory called 'static' located in the application's root folder. 



