from flask import Flask, render_template, url_for, request,redirect
import csv

app = Flask(__name__)
print(app)

@app.route("/")
def hello_world():
    return "Hellooooo,Ibrahim,zaoj Aaish!"

@app.route("/blog")
def my_blog():
    return render_template('index.html')

@app.route("/component")
def my_comp():
    return render_template('components.html')
def store_base(data):
    with open('database.txt', mode='a') as database:
        email= data['email']

        subject= data['subject']

        message= data['message']
        file = database.write(f'\n {email},{subject},{message}')

def write_cvs(data):
    with open('database.csv', mode='a') as database2:
        email= data['email']

        subject= data['subject']

        message= data['message']
        csv_write= csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method== 'POST':
      try:
          data= request.form.to_dict()
          write_cvs(data)
          return redirect('/cont.html')
      except:
          return 'did not save to data base'
  else:
      return 'something went wrong. try again later'




@app.route("/about.html")
def about():
    return render_template('about.html')