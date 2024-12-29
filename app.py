

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact2.html')
def contact2():
    return render_template('contact2.html')

if __name__ == '__main__':
    app.run(debug=True)
