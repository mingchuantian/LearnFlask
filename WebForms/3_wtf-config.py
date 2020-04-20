#Flas-WTF supports communication between the server and webforms
#it doesn't require initialize in the front of the .py file. However, it needs a secret key to be configured. 
app = Flask(__name__)
app.config['SECRET_KEY'] = '960812'
#app.config is a general-purpose place to store configuration variables used by Flask, extensions, etc,. 

