from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_time():
   now = datetime.now()
   return f'Current Time: {now.strftime("%Y-%m-%d %H:%M:%S")}'

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')