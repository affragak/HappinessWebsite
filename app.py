from flask import Flask, render_template


app = Flask (__name__)

@app.route("/")
def hello():
  return render_template("home.html")

@app.route("/planning")
def planning():
  return render_template("planning.html")  

@app.route("/flowerd")
def flowerd():
  return render_template("flowerd.html")  

@app.route("/about")
def about():
  return render_template("about.html")  

@app.route("/contact")
def contact():
  return render_template("contact.html")  


if __name__ == '__main__': app.run(host='0.0.0.0', debug=True)
  