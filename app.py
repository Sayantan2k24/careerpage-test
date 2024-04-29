from flask import Flask, render_template,jsonify # from flask module import Flask Class

# next create an object from flask and puting it in the variable
# if the program is invoked by python app.py --> then print(__name__) ==> will be output as main

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'DevOps Engineer',
        'location': 'Jaipur, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Linux Admin',
        'location': 'Mumbai, India',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Cloud Engineer',
        'location': 'San Fransisco, US',
        'salary': 'Rs. $120,000'
    }    
]
# then need to create a route
# register a route
# @ --> decorator
@app.route("/") # now define a function  below the decorator
def hello_profile():
    return render_template('home.html', jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__': #we are checking if we are running this python script as python app.py --> then do start this app by app.run --> and these are the arg --> and debug is True --> update on the fly
    app.run('0.0.0.0', debug=True)

