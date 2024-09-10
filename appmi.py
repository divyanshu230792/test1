from flask import Flask,render_template,request,jsonify
app2=Flask(__name__)
@app2.route('/')
def test1():
    print('*'*50)
    print('we creating new webframe')
    print('*'*50)
    return 'hello flask'

if __name__=='__main__':
    app2.run()