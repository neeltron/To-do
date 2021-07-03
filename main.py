from flask import Flask, render_template, request, make_response, redirect, url_for
from replit import db



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

# Index page and Rendering Basic Templates
@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == "POST":
    todo = request.method.get("item")
    priority = request.method.get("priority")
    db[priority] = todo
  return render_template('index.html')



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
