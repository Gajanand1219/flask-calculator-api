
from flask import Flask, render_template,request
from datetime import datetime,date
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def age():
    result1 = ""
    result2 = ""
    result3 = ""

    if request.method == 'POST':
        current_date_str = request.form["date"]
        birth_date_str = request.form["date1"]
        today = date.today()  # Get today's date

        current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        result1 = current_date.day - birth_date.day
        result2 = current_date.month - birth_date.month
        result3 = current_date.year - birth_date.year

    return render_template('age.html', result1=result1, result2=result2, result3=result3)

    


@app.route("/calculater",methods=['GET',"POST"])
def calculator():
    result = None
    if request.method == 'POST':
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                 result = num1 / num2
                
    return render_template('cal.html', result=result)

    

@app.route("/conversion",methods=['GET','POST'])
def conversition():
    result=""
    result1=""
    result2=""
    result3=""
    Gram=""
    KG_gram=""
    Meter=""
    cm=""
    if request.method =='POST':
        num = float(request.form['num'])
        operation = request.form["operation"]

        if operation =='kg_to_gram':
            result = num * 1000
            Gram='Gram'
        elif operation =='gram_to_kg':
            result1 = num /1000
            KG_gram='KG_gram'
        elif operation =='me_to_cm':
            result2 = num * 100.0
            cm='cm'
        elif operation =='cm_to_me':
            result3 = num/100
            Meter='Meter'

    return render_template('conversion.html',result=result,result1=result1,result2=result2,result3=result3,Gram=Gram,KG_gram=KG_gram,
                           Meter=Meter,cm=cm)

@app.route("/table", methods=['GET', 'POST'])
def tables():
    result = []
    if request.method == 'POST':
        num = int(request.form['num'])
        for i in range(1, 11):
            print(result.append(f"{num} × {i} = {i * num}  ") )
    return render_template('table.html', result=result)

@app.route("/operation",methods=['GET','POST'])
def sqrt():
    sqrt=""
    fact=""
    cube=""
    if request.method=='POST':
        num=int(request.form['num'])
        operation=request.form['operation']
        if operation == 'sqrt':
            sqrt =math.sqrt(num)
        elif operation =='fact':
            fact=math.factorial(num)
        elif operation =='cube':
            cube= num*num*num

    return render_template('operation.html',sqrt=sqrt,fact=fact ,cube=cube)
    
if __name__ == '__main__':
    app.run(debug=True)





