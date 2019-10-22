from flask import (
                    Flask,
                    render_template,
                    request
                  )

app = Flask(__name__)


@app.route('/get-student-info/<string:id>')
def hello_world(id=None):
    return 'Hello World!'

@app.route('/')
@app.route('/my-new-route')
def my_route():
    users = {
        'John': 'New user',
        'Alex': 'New user',
        'Jenny': 'Old user'
    }

    my_list = ['1', '2', '3', '4']
    title = 'main_page'
    return render_template('index.html',
                           data='my data',
                           title=title,
                           users=users,
                           template_list=my_list)



if __name__ == '__main__':
    app.run(debug=True)