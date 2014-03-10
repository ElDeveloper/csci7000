from flask import Flask, request, render_template
from string import upper

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/resume/')
@app.route('/resume/<name>')
def resume(name=None):
    return render_template('resume.html', name=name)

@app.route('/find', methods=['GET'])
def find():
    locations = {'CSCI1300':'ATLAS 100', 'CSCI2240':'ITTL 1B50'}

    try:
        course = request.args.get('course', '')
    except KeyError:
        return 'No brah, you cannot go there'

    location = locations.get(course, 'Sorry no result for %s' % course)

    return 'Find the classroom for %s ... %s' % (course, location)

@app.route('/notification')
def notification():
    print 'boom goes the dynamite '
    return 'Get a notification. To be implemented'

if __name__ == "__main__":
    app.run()