from flask import Flask, render_template, request
from script import get_instagram_video_url  # Import the function from script.py
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() in ['true', '1', 't', 'y', 'yes']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    instagram_url = request.form['instagram_url']
    success, video_url_or_error = get_instagram_video_url(instagram_url)
    if success:
        return render_template('index.html', video_url=video_url_or_error, error=None)
    else:
        return render_template('index.html', video_url=None, error=video_url_or_error)

if __name__ == '__main__':
    app.run()
