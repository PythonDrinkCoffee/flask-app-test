import os
from flask import Flask, render_template, jsonify
from markupsafe import escape

app = Flask(__name__)

PROJECTS = [
    {
        "title": "Project 1",
        "data" : "10.10.2023",
        "costs": "1230$",
        "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
    },
    {
        "title": "Project 2",
        "data" : "12.10.2023",
        "costs": "5230$",
        "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
    },
    {
        "title": "Project 3",
        "data" : "12.10.2023",
        "costs": "21230$",
        "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
    },
    {
        "title": "Project 4",
        "data" : "12.10.2023",
        "costs": "21230$",
        "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
    },
    {
        "title": "Project 5",
        "data" : "13.12.2023",
        "costs": "230$",
        "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
    },
    {
        "title": "Project 6",
        "data" : "13.12.2023",
        "costs": "230$",
        "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
    },
]

RATINGS = [
    {
        "title" : "Project 1",
        "rate" : "5.0/5.0",
        "comment": "Lorem ipsum dolor sit amet, consectetur...",
        "picture": "address",
        "user": "Rajesh Suomediani",
    },
    {
        "title" : "Project 2",
        "rate" : "5.0/5.0",
        "comment": "Lorem ipsum dolor sit amet, consectetur...",
        "picture": "address",
        "user": "Rajesh Suomediani",
    },
    {
        "title" : "Project 3",
        "rate" : "5.0/5.0",
        "comment": "Lorem ipsum dolor sit amet, consectetur...",
        "picture": "address",
        "user": "Rajesh Suomediani",
    },
    {
        "title" : "Project 4",
        "rate" : "5.0/5.0",
        "comment": "Lorem ipsum dolor sit amet, consectetur...",
        "picture": "address",
        "user": "Rajesh Suomediani",
    },
    {
        "title" : "Project 5",
        "rate" : "5.0/5.0",
        "comment": "Lorem ipsum dolor sit amet, consectetur...",
        "picture": "address",
        "user": "Rajesh Suomediani",
    },
    {
        "title" : "Project 6",
        "rate" : "5.0/5.0",
        "comment": "Lorem ipsum dolor sit amet, consectetur...",
        "picture": "address",
        "user": "Rajesh Suomediani",
    },
]

@app.route('/', methods=['GET'])
def hello():
    title = "First App - flask 2023"
    description = "Welcome to my first application built with Flask framework"
    return render_template("index.html", 
                           title=title, 
                           description=description,  
                           projects=PROJECTS,
                           ratings=RATINGS
                           )

@app.route('/api/projects')
def projects():
    return jsonify(PROJECTS)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
