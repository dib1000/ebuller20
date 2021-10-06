# Cashew (Shriya Anand, Emma Buller, William Chen)
# SoftDev
#K10-Putting Little Pieces Together
#2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

#We predict that nothing be printed in the terminal. The webpage should say "No hablo queso"
