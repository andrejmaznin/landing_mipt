import os

from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route('/')
def main():
    return render_template('main_page.html')


if __name__ == "__main__":
    application.run()
