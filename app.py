from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message

app = Flask (__name__)

app.secret_key = 'my_secrest_key'

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'
mail.init_app(app)


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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """ 
    From: %s <%s> 
    %s 
    """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return 'Form posted.'
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
    


if __name__ == '__main__': app.run(host='0.0.0.0', debug=True)
  