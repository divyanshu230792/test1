from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/testing')
def testing():
    print('wee r testing html')
    return '''<!DOCTYPE html>
                <html>
                <body>

                <h1>My First Heading</h1>
                <p>My first paragraph.</p>

                </body>
                </html>

                
                <h1>This is heading 1</h1>
                <h2>This is heading 2</h2>
                <h3>This is heading 3</h3>
                

                <h1 style="background-color:DodgerBlue;">Hello World</h1>
                <p style="background-color:Tomato;">Lorem ipsum...</p>
                '''
if __name__=='__main__':
    app.run()