from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r'C:\Users\DELL\OneDrive\Desktop\Semister 1_DA\Python_DAB111\.venv\Group7_Project\Group7_Project')
db_name = "supermarket.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    supermarkets = cursor.execute("SELECT * FROM supermarkets_sales LIMIT 50").fetchall()
    con.close()

    return render_template("data.html", supermarkets_sales = supermarkets)

if __name__=="__main__":
    app.run(debug=True)
