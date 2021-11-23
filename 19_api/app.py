# Lightning Cheese (Emma Buller and Deven Maheshwari)
# SoftDev
# K19 -- A RESTful Journey (Using RESTapis)
# 2021-11-23
# time spent:

from flask import Flask, render_template  #Q0: What happens if you remove render_template from this line?
import urllib.request
app = Flask(__name__)

@app.route("/")
def REST():
    d = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=uhAKVvq7ohfNOGPx5IMu3bUGcAsaikXHR7IYMtjw")
    x = json.loads(d)
    return render_template("main.html", img=x[url])

if __name__ == "__main__":
    app.debug = True
    app.run()
