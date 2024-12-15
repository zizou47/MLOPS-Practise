from flask import Flask, render_template, request

"""
"""
# WSGI app
app = Flask(__name__)

@app.route('/')  # URL must start with /
def welcome():
        return "<!DOCTYPE html><html><head><title>Simple Page</title></head><body><h1>Hello, World!</h1></body></html>"

@app.route('/index')
def index():
    return render_template('./index.html')


@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello{name}'
    return render_template('./form.html')

    




if __name__ == '__main__':

    app.run(debug = True) # run the app in debug mode which u can change without restarting the server