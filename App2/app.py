from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home2.html')

@app.route('/result', methods=['GET'])
def result():
    number = request.args.get('number')
    if number is None:
        result = "No number provided!"
    else:
        try:
            number = int(number)
            if number % 2 == 0:
                result = "even"
            else:
                result = "odd"
        except ValueError:
            result = "not an integer"
    return render_template('result2.html', result=result)

if __name__ == '__main__':
    app.debug = True
    app.run()
