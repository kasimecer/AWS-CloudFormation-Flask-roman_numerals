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





# Create a function named `index` which uses template file named `index.html` 
# send a number as template variable to the app.py and assign route of no path ('/') 
@app.route("/")
def index():
    return render_template("index.html", methods=["GET"])


# convert using "convert" function, then sent the result to the 
# "result.hmtl" file and assign route of path ('/calc'). 
# When the user comes directly "/calc" path, "Since this is a GET request, LCM has not been calculated" string returns to them with "result.html" file
@app.route("/convert", methods=["GET", "POST"])
def convert():
    if request.method == "POST":
        num = request.form.get("number")
        return render_template("result.html", number_decimal = num, number_roman = converter(int(num))) # , developer_name = 'Kasim'
    else:
        return render_template("result.html")  # , developer_name = "Kasim"



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
   #app.run(debug=True)