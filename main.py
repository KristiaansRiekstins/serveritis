from flask import Flask, render_template, request
from proc_file import read_file

app = Flask(__name__)

@app.route('/')
def index():
  return "Hi!"

@app.route('/home')
def home():
  return render_template("home.html", aktiva_lapa ="home")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/contacts')
def contacts():
  return render_template("contacts.html")

@app.route('/params')
def params():
  args = request.args
  for key, value in args.items():
    print(f"{key}:{value}")
  return args

@app.route('/params_table')
def params_table():
  args = request.args
  return render_template('params_table.html', args = args)

@app.route('/chat')
def chat():
  return render_template("chat.html")

@app.route('/post_req', methods = ['POST'])
def post_req():
  return request.args

@app.route('/read_file')
def read_from_file():
  content = read_file()
  return content

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, threaded = True, debug = True)