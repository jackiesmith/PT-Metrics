from flask import Flask, request, render_template, url_for
from metrics import get_ad_news_metrics, get_ad_petition_metrics, get_ad_totals_metrics, get_petition_metrics
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/readme', methods=['GET', 'POST'])
def readme():

    return render_template('readme.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        type = request.form['type']

        #HORRIBLE design but just testing. Next steps is one function to accept type and dropdown for user

        if type == 'petition':

            file = request.files.get('file')
            keyword = request.form['keyword']
            saw_str = request.form['saw_str']
            petition_name = request.form['petition_name']
            metrics = get_petition_metrics(file, keyword, saw_str, petition_name)
            return render_template('upload.html', metrics=metrics)

        elif type == 'ad_news':
            file = request.files.get('file')
            keyword = request.form['keyword']
            metrics = get_ad_news_metrics(file, keyword)
            return render_template('upload.html', metrics=metrics)

        elif type == 'ad_petition':
            file = request.files.get('file')
            keyword = request.form['keyword']
            petition_name = request.form['petition_name']
            metrics = get_ad_petition_metrics(file, keyword, petition_name)
            return render_template('upload.html', metrics=metrics)

        elif type == 'ad_totals':
            file = request.files.get('file')
            metrics = get_ad_totals_metrics(file)
            return render_template('upload.html', metrics=metrics)
        '''
        NOTES:
        request.form['name']: use indexing if you know the key exists
        request.form.get('name'): use get if the key might not exist
        request.args: the key/value pairs in the URL query string
        request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
        request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
        '''
    return render_template('upload.html', metrics = '')

if __name__ == '__main__':
    app.run(debug=True)

