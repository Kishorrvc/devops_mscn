# <3MSCN[>
from flask import Flask  
app = Flask(__name__)  

@app.route("/")  
def hello():  
    return "<br><br><br><br><br><br>Hello from DevOps Pipeline!"  

app.run(debug=False, host="0.0.0.0", port=5001)

