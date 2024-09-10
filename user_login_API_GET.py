from flask import jsonify,Flask,render_template,request
app2=Flask(__name__)
user_cred={'username':'admin','password':'admin1234'}
@app2.route('/login',methods=['GET'])
def login():
    username=request.args.get('username')
    password=request.args.get('password')
    print('username:',username)
    print('password:',password)
    if username==user_cred['username'] and password==user_cred['password']:
        return jsonify({'status':'successful','result':'successful login'})
    else:
        return jsonify({'status':'unsuccessful','result':'unsuccessful login'})
    
if __name__=='__main__':
    app2.run()
