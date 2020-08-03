from flask import Flask
from flask import Flask, request, jsonify,render_template  
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return render_template("app.html")
