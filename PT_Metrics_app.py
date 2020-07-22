
# A very simple Flask Hello World app for you to get started with...

'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

'''



from flask import Flask, request, render_template
from metrics import get_ad_news_metrics, get_ad_petition_metrics, get_ad_totals_metrics, get_petition_metrics
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        #HORRIBLE design but just testing. Next steps is one function to accept type and dropdown for user
        if type == 'petition':
            metrics = get_petition_metrics('file', 'keyword', 'saw_str', 'petition_name')
            return render_template('upload.html', metrics=metrics)

        elif type == 'ad_news':
            metrics = get_ad_news_metrics('file', 'keyword')
            return render_template('upload.html', metrics=metrics)

        elif type == 'ad_petition':
            metrics = get_ad_petition_metrics('file', 'keyword', 'petition_name')
            return render_template('upload.html', metrics=metrics)

        elif type == 'ad_totals':
            metrics = get_ad_totals_metrics('file', 'keyword', 'petition_name')
            return render_template('upload.html', metrics=metrics)

        df = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', metrics=df.shape)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

