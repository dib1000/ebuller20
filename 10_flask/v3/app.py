# Cashew (Shriya Anand, Emma Buller, William Chen)
# SoftDev
#K10-Putting Little Pieces Together
#2021-10-04

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

# We predict that the same as last version will be but now the "debug mode" should be "on" instead of "off"
# Post-Test: prediction was true and there is also a debugger PIN provided.
