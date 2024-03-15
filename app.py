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
    recipients = [
        {'access_key': 'c7b61e5e-e90c-4550-966d-09501ca9a413'},
        {'access_key': 'f7a528e9-d257-4d81-8583-af838851cacc'}
    ]
    return render_template('contact.html', recipients=recipients)

@app.route('/contact2.html')
def contact2():
    return render_template('contact2.html')

if __name__ == '__main__':
    app.run(debug=True)
