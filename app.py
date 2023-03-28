from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Luke Bennett!' ' I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/favorite-course')
def favoritecourse():  # put application's code here
    print('Course Entered: ' + request.args.get('course_name'))
    print('Course Number Entered: ' + request.args.get('course_number'))

    return render_template('favorite-course.html')

@app.route('/contact')
def contact():  # put application's code here
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()

