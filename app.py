from flask import Flask, render_template, request
from collections import OrderedDict

app = Flask(__name__)


# create a function named "converter" which convert to romen numbers. 
def converter(num):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


@app.route('/', methods=['POST', 'GET'])
def main_post():
    if request.method == 'POST':
        alpha = request.form['number']
        if not alpha.isdecimal():
            return render_template('index.html', developer_name='Kasim', not_valid=True)
        number = int(alpha)
        if not 0 < number < 4000:
            return render_template('index.html', developer_name='Kasim', not_valid=True)
        return render_template('result.html', number_decimal = number , number_roman= converter(number), developer_name='Serdar')
    else:
        return render_template('index.html', developer_name='Kasim', not_valid=False)
    

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
   #app.run(debug=True)