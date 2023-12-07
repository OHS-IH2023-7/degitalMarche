from flask import Flask,render_template
#import pymysql
#
#print("動いてる")
#
#connection = pymysql.connect(
#    host="localhost",
#    db="degitalMarche",
#    user="root",
#    password="",
#    charset="utf8",
#    cursorclass=pymysql.cursors.DictCursor
#)
#
#def sqlConnect(sql):
#    cursor = connection.cursor()
#    cursor.execute(sql)
#    result = cursor.fetchall()
#    return result 

app = Flask(__name__)

@app.route('/')
def helloworld():
    # return 'Hello World.'
    return render_template('top.html')
#    sql = "SELECT * FROM test"
#    result = sqlConnect(sql)
#    return render_template('top.html',result=result)

@app.route('/product_detail')
def product_detail():

    return render_template('product_detail.html')

@app.route('/input_info')
def product_info():
    return render_template('product_info.html')

@app.route('/buy_check')
def buy_check():
    return render_template('buy_check.html')

@app.route('/complete')
def complete():
    return render_template('complete.html')

@app.route('/top')
def top():
    return render_template('top.html')

@app.route('/rogin_customer',methods=["post"])
def rogin():
    return render_template('rogin_customer.html')

@app.route('/product_resistration',methods=["post"])
def product_resistration():
    # return 'Hello World.'

    return render_template('product_resistration.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)