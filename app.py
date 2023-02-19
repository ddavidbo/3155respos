from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    current_datetime = now.strftime("%Y-%m-%d %I:%M:%S %p")
    return f"The current date and time is {current_datetime}"

if __name__ == '__main__':
    app.run()
