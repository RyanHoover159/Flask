from flask import Flask, render_template, request

app = Flask(__name__)

def check_number(number):
    try:
        num = int(number)
        if num % 2 == 0:
            return "Even number"
        else:
            return "Odd number"
    except ValueError:
        return "Not an integer"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number = request.form['number']
        result = check_number(number)
        return render_template('result.html', result=result)
    return render_template('home.html')

@app.route('/result')
def result():
    return "Error: No query parameter included. Please enter a number."

if __name__ == '__main__':
    app.run(debug=True)
