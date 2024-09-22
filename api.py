from flask import Flask ,jsonify ,request 
from modul import add
app = Flask(__name__)

# sample root for home page

@app.route('/')
def home():
    return "welcome to python"

@app.route('/hi',methods=['GET'])      
def home1():
    greet1 = add()
    return greet1



if __name__=='__main__':
    app.run(debug=True)
