from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"
# this is just an example
# @app.post("/")
# def homePost():
# return "hello from flask post"

# Endpoints
@app.get("/test")
def test():
    return "hello from the test server"

# Endpoint using Json
@app.get("/api/about")
def aboutGet():
    name = {"name": "Adrian"}
    return json.dumps(name)

# create a new route /greet/{name}, this route should accept name 
# as part of the url and return an html message saying hello {name}

@app.get("/greet/<name>")
def greet(name):
    return f"""
<h1 style=color:blue>Hello {name}!</h1>"""

# by creating the farewell message
@app.get("/farewell/<name>")
def farewell(name):
    return f"""
<h1 style=color:red>bye bye {name}!</h1>"""

app.run(debug=True)