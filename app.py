from flask import Flask, render_template, request,flash
from search import search, unique
HOST_NAME = "localhost"
HOST_PORT = 8080
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
@app.route('/', methods=['GET', 'POST'])
def index():
    search_keys = ['fullname', 'cin', 'cne','date_birthday', 'gender', 'address', 'phone', 'email']
    if request.method == 'POST':
        value = request.form['search']
        key = request.form['search_key']
        users = search(key,value,100)
        flash(f"{len(users)} results." if len(users)  != 0 else f"No results about {value}. Make sure that all words are spelled correctly.")
    else:
      users = []
      flash("Search use fullName,Birthday,Address,CIN,CEN,Phone,Email) Over-k :D")
    return render_template('index.html', search_keys=search_keys,users=users)

if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
