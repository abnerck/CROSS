from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

# Middleware para forzar HTTPS y www
@app.before_request
def before_request():
    if request.url.startswith('http://'):  # Force HTTPS
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)
    if not request.host.startswith('www.'):  # Force www
        url = request.url.replace(request.host, 'www.' + request.host, 1)
        return redirect(url, code=301)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)