from flask import Flask, render_template

app = Flask(__name__,static_folder="static", static_url_path="")


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/about')
def about():
    return render_template('about.html')


def run():
    app.run(port=4000)


if __name__ == '__main__':
    run()
