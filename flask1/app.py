from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_date():
   now = datetime.now()
   return f'Current Date: {now.strftime("%Y-%m-%d")}'

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')

