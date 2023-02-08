from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_1.html')

@app.route('/page2')
def page2():
    return render_template('index_2.html')

if __name__ == '__main__':
    """
        Dummy flask app generated with the help of ChatGPT
    """
    app.run(debug=True)