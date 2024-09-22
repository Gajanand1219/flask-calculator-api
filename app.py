from flask import Flask ,jsonify ,request

app=Flask(__name__)

@app.route('/')
def home():
    return "hellow python"

# @app.route('/api',methods=['GET'])
# def end():
#     get_data={
#         'name':'gaju',
#         'age':12,
#         'class':'fybsc_cs'
#     }
#     return jsonify(get_data)




@app.route('/api',methods=['POST'])
def end():
    get_data1={
        'name':'gaju',
        'age':12,
        'class':'fybsc_cs'
    }
    return jsonify(get_data1)




if __name__=='__main__':
    app.run(debug=True)