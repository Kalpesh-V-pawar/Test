import os
from flask import Flask, request, jsonify, render_template_string, redirect, url_for
import sqlite3
import requests

app = Flask(__name__)

HTML_page = """"
<!DOCTYPE html>
<html lang="en">
<html>
    <head>
        <title>Hiii</title>
    </head>
    <body>
      <form action = "/submit" method = "POST">
         <input type="text" id="item_name" name="item_name" required>
         <input type="text" id="item_name1" name="item_name1" required>
         <button type = "submit">Submit</button>
      </form> 
         <!-- Button to navigate to the second page -->
       <form action="{{ url_for('Second_page') }}" method="get">
            <button type="submit">Go to Second Page</button>
       </form>
    </body>

</html>
"""


Second_pages = """
    <html>
    <body>
        <h1>Welcome to the Second Page!</h1>
        
    </body>
    </html>
"""

def init_db():
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "data.db"))
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inputs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text_input TEXT NOT NULL,
        text2_input TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template_string(HTML_page)

@app.route("/Second_page")
def Second_page():
    return render_template_string(Second_pages)

@app.route("/submit", methods=["POST"])
def submit1() :
    inputtext = request.form.get("item_name")
    inputtext1 = request.form.get("item_name1")
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), "data.db"))
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO inputs (text_input, text2_input) VALUES (?, ?)", (inputtext , inputtext1))
    conn.commit()
    conn.close()




    return f"You submitted: {inputtext} and {inputtext1}"
    print(inputtext)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
