# Import Flask modules
from flask import Flask, render_template, request

# Create an object named app
app = Flask(__name__)

# convert the given number to the roman numerals
def convert(decimal_num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
            50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i] * (decimal_num // i)
        decimal_num %= i
    return num_to_roman

@app.route('/', methods = ["GET", "POST"])
def mert():
    if request.method == "POST":
        mynumber = request.form.get("number")
        if mynumber.isalnum() and (0 < int(mynumber) < 4000) and mynumber.isdecimal():
            return render_template('result.html', number_decimal = mynumber, number_roman = convert(int(mynumber)), developer_name = "Huseyin")
        else:
            return render_template('index.html', not_valid = True, developer_name = "Huseyin")
    else:
        return render_template('index.html', developer_name = "Huseyin", not_valid = False)
# Add a statement to run the Flask application which can be debugged.
if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host='0.0.0.0', port=80)