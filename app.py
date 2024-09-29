from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/swap', methods=['POST'])
def swap():
    a = int(request.form['a'])
    b = int(request.form['b'])
    a, b = b, a 
    return render_template('index.html', result=f'Swapped: a = {a}, b = {b}')

@app.route('/odd_even',methods=['POST'])
def odd_even():
    num = int(request.form['num'])
    if num % 2 == 0:
        result = f'{num} is even'
    else:
        result = f'{num} is odd'
    return render_template('index.html', result = result)

@app.route('/ascii', methods=['POST'])
def ascii():
    ascii_char = request.form['ascii_char']
    if len(ascii_char) == 1:
        ascii_num = ord(ascii_char)
        result = f'ASCII value of {ascii_char} is {ascii_num}'
    else:
        result = "please enter a Single Character"
    return render_template('index.html', result = result)


if __name__ == '__main__':
    app.run(debug=True)