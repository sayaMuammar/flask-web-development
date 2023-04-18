from flask import Flask, render_template

app = Flask(__name__)
print(app)


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def works(page_name):
    return render_template(page_name)


if __name__ == "__main__":
    app.run(debug=True)