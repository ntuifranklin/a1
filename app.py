from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/home')
def home():
    return hello_world()

# define a post method to handle post request
@app.route('/predictions', methods=['POST'])
def post():
    # get the data sent through the form
    data = request.form['data']
    print(data)
    return 'Post request' + data

if __name__ == '__main__':
    app.run()