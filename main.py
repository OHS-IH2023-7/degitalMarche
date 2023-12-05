from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def helloworld():
    # return 'Hello World.'

    return render_template('index.html')

@app.route('/product_detail')
def product_detail():

    return render_template('product_detail.html')
@app.route('/top')
def helloworl():
    return render_template('top.html')

@app.route('/product_resistration')
def product_resistration():
    # return 'Hello World.'

    return render_template('product_resistration.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)