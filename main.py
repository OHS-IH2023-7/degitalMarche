from flask import Flask,render_template
import pymysql

print("動いてる")

connection = pymysql.connect(
    host="anaconda-postgres_devcontainer-mysql-1",
    db="test",
    user="test",
    password="test",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def sqlConnect(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result 
sql = "SELECT * FROM test"

app = Flask(__name__)

@app.route('/')
def helloworld():
    # return 'Hello World.'
    sql = "SELECT * FROM test"
    result = sqlConnect(sql)
    return render_template('index.html',result=result)

@app.route('/product_detail')
def product_detail():

    return render_template('product_detail.html')
@app.route('/top')
def top():
    return render_template('top.html')
@app.route('/rogin_customer')
def rogin():
    return render_template('rogin_customer.html',methods=["post"])

@app.route('/product_resistration',methods=["post"])
def product_resistration():
    # return 'Hello World.'

    return render_template('product_resistration.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)