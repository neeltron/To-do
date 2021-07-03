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
    todo = request.form.get("item")
    priority = request.form.get("priority")
    db[priority] = todo
  return render_template('index.html', obj = db)



@app.route('/delete', methods = ['GET', 'POST'])
def delete():
  if request.method == "POST":
    for i in range(0, 100):
      del db[str(i)]
    return redirect(url_for(index()))



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
