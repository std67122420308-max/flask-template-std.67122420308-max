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
  email = 'std.67122420308@ubru.ac.th'
  mobile = '063-2354-5545'
  age = 20
  return render_template('about.html', title=title,
                                      name=name,
                                      email=email,
                                      mobile=mobile,
                                      age=age)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorits Foods Page'
  foods = ['ก๋วยเตี๋ยว','ก๋วยจั๊บ','กะเพรา']
  return render_template('favorite_foods.html',
                          title = title,
                            foods = foods)

@app.route('/favorite/sports')
def favorite_sports():
  title = 'Favorite Sports Page'
  sports = ['ฟุตบอล', 'ฟุตซอล', 'ตะกร้อ']
  return render_template('favorite_sports.html', title=title, sports=sports)

@app.route('/favorite/movies')
def favorite_movies():
  title = 'Favorite Movies Page'
  movies = ['มหาเวทย์ผนึกมาร', 'ข้างบ้าน', 'หมู่บ้านโคกะโหลก','จอมขมังเวทย์','นาคี 2']
  return render_template('favorite_movies.html', title=title, movies=movies)