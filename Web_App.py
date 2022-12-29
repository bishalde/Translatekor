from flask import Flask
app=Flask(__name__)

@app.route('/homepage')
@app.route('/')
def homepage():
    return '<marquee><h1>Homepage</h1></marquee>'

app.run(debug=False,port='0.0.0.0')