from flask import Flask, render_template, request, redirect , url_for , flash, jsonify
from database import Entry, get_db
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from joblib import load

def create_df(bedrooms, bathrooms, sqft_living, view, grade, sqft_above, sqft_basement, lat, sqft_living15):
    df = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'sqft_living': [sqft_living],
        'view': [view],
        'grade': [grade],
        'sqft_above': [sqft_above],
        'sqft_basement': [sqft_basement],
        'lat': [lat],
        'sqft_living15': [sqft_living15]
    })
    return df

def predict_price(df):
    model = load('model/model3.joblib')
    return model.predict(df)[0]

app = Flask(__name__)

def load_data():
   df = pd.read_csv('dataset/house_pricing_dataset.csv')
   return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        sqft_living = request.form['sqft_living']
        view = request.form['view']
        grade = request.form['grade']
        sqft_above = request.form['sqft_above']
        sqft_basement = request.form['sqft_basement']
        lat = request.form['lat']
        sqft_living15 = request.form['sq15']
        df = create_df(bedrooms, bathrooms, sqft_living, view, grade, sqft_above, sqft_basement, lat, sqft_living15)
        price = predict_price(df)
        return render_template('home.html', price=price)
    return render_template('home.html')

@app.route('/graph/1')
def graph_1():
   df=load_data()
   fig1 = px.histogram(df, x = 'price')
   fig2 = px.histogram(df, x = 'bedrooms')
   fig3 = px.histogram(df, x = 'bathrooms')
   fig4 = px.histogram(df, x = 'sqft_living')
   fig5 = px.histogram(df, x = 'floors')
   fig6 = px.histogram(df, x = 'sqft_above')
   fig7 = px.histogram(df, x = 'grade')
   fig8 = px.histogram(df, x = 'lat')
   fig9 = px.histogram(df, x = 'sqft_living15')
   fig10 = px.scatter(df , x = 'price' , y='bedrooms' )
   fig11 = px.scatter(df , x = 'price' , y='bathrooms' )
   fig12 = px.scatter(df , x = 'price' , y='sqft_living' )
   fig13 = px.scatter(df , x = 'price' , y='lat' )
   fig14 = px.scatter(df , x = 'price' , y='sq15' )
   return render_template('graph1.html',
                            fig1 = fig1.to_html(), 
                            fig2 = fig2.to_html(),
                            fig3 = fig3.to_html(),
                            fig4 = fig4.to_html(),
                            fig5 = fig5.to_html(),
                            fig6 = fig6.to_html(),
                            fig7 = fig7.to_html(),
                            fig8 = fig8.to_html(),
                            fig9 = fig9.to_html(),
                            fig10 = fig10.to_html(),
                            fig11 = fig11.to_html(),
                            fig12 = fig12.to_html(),
                            fig13 = fig13.to_html(),
                            fig14 = fig14.to_html()
                        )

@app.route('/graph/2')
def graph_2():
   
   return render_template('graph2.html')
        

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=False)
 