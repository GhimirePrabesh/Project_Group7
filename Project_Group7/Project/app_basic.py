from flask import Flask, render_template
import sqlite3
import pathlib 


current_directory = pathlib.Path(__file__).parent
db_name = "supermarket.db"
db_path = current_directory / db_name
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
