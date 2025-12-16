from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page'
  return render_template('index.html', title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Wichai Boonkerng'
  emali = 'std.671224203082ubru.ac.th'
  mobile = '066-555-4545'
  ags = 20
  return render_template('about.html', title=title,
                          name=name,
                          email=email,
                          mobile=mobile,
                          age=ags)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = ['กระเพราหมูสับ', 'ก๋วยเตี๋ยว', 'ตำป่า']
  return render_template('favorite_foods.htln', 
                          title=title,
                          foods=foods)
@app.route('/favorite/sports')
def favorite_foods():
  title = 'Favorite Sport Page'
  sports = ['ฟุตบอล', 'ฟุตซอล', 'ตะกร้อ']
  return render_template('favorite_sports.htln', 
                          title=title,
                          sports=sports)