from flask import Flask, render_template, request
import requests
import pandas as pd
import json
import os

app = Flask(__name__)

@app.route('/task-1')
def index():
    selected_fields = request.args.get('selectedFields')
    if selected_fields is None:
        selected_columns = None
    else:
        selected_columns = json.loads(selected_fields)

    response = requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
    if(response.status_code != 200):
        return f"Failed to fetch data. Check the API or try again! Status code: {response.status_code}"
    else:
        if selected_columns is None:
            selected_columns = ['title', 'price', 'popularity']
        data = response.json()
        products_data = data['products']
        data_list = [{'pid': key, **value} for key, value in products_data.items()]
        df = pd.DataFrame(data_list)
        df['popularity'] = df['popularity'].astype(int)
        df = df.sort_values(by=['popularity'], ascending=False)
        df = df[selected_columns]
        # df.drop(columns=['pid','subcategory'], inplace=True)
        table_html = df.to_html(index=False)
        return render_template('index_1.html', table_html=table_html)
        # return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/')
def index_2():
    return render_template('index_2.html')

@app.route('/task-2')
def index_3():
    return render_template('index_2.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port)

