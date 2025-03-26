from flask import Flask ,jsonify ,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home/<name>")

def home(name=None):
    return render_template('home.html', name=name)  

@app.route("/info" ,methods=['POST'])
def retrunSomething ():

    return jsonify({'info':'This is a POST request'})

# def index():
#     return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)