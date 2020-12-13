import numpy as np
from flask import Flask, request, jsonify, render_template,redirect,url_for
import flask
import matplotlib.pylab as plt
import tensorflow as tf
from tensorflow import keras
from keras.applications.vgg19 import VGG19
from keras.applications import VGG19
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import glob
import os
import random
#import pygal 
from werkzeug.utils import secure_filename
import plotly
import plotly.graph_objs as go
import numpy as np
import plotly.express as px
import json
#import plotly.plotly as py
from plotly.graph_objs import *


UPLOAD_FOLDER = 'static/uploaded/'
DETAILS_FOL='static/eoss/'
eos=lymph=mono=neutro=0
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DETAILS_FOL']=DETAILS_FOL

model = tf.keras.applications.VGG19(include_top=False, weights='imagenet',input_shape=(150,150,3))
loadmodel=load_model(r'model\savemodelvgg19.h5')


def create_plot(classes,val):


    N = 40
    fig=go.Bar(
            x=classes, # assign x as the dataframe column 'x'
            y=val,
            marker_color='rgb(55, 83, 109)',
            
        )
    data = [
        go.Bar(
            x=classes, # assign x as the dataframe column 'x'
            y=val,
            marker_color='rgb(55, 83, 109)',
           
            
        )
    ]
    layout=Layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    fig=Figure(data=data,layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
def home():
    return render_template('register.html')


@app.route('/registered',methods=["POST","GET"])
def registered():
    global username
    global age
    global gender
    username=request.form['name']
    age=request.form['age']
    gender=request.form['gender']
    #print(name," ",age," ",gender)
    return render_template('index.html')




@app.route('/upload_cellimage',methods=["POST","GET"])

def upload_cellimage():
   
    uploaded_files = flask.request.files.getlist("file")
    #eos=lymph=mono=neutro=0
    global eos,lymph,mono,neutro
    classes=['EOSINOPHIL','LYMPHOCYTE','MONOCYTE','NEUTROPHIL']
    my_colors = ['r','g','b','c']
   
    #print(type_cell)
    for i in uploaded_files:
        #print(i)
        i.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(i.filename)))
        name=i.filename
        #print(name)
        file = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(i.filename))
        #print(file)
        image=load_img(file,target_size=(150,150))
        image=img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image/=255.
        bt_prediction = model.predict(image) 
        singlepred = loadmodel.predict_classes(bt_prediction)
        #print(classes[int(singlepred)])
        if(classes[int(singlepred)]=='EOSINOPHIL'):
            eos=eos+1
            
        elif(classes[int(singlepred)]=='LYMPHOCYTE'):
            lymph=lymph+1
            
        elif(classes[int(singlepred)]=='MONOCYTE'):
            mono=mono+1
            
        else:
            neutro=neutro+1
            
    val=[eos,lymph,mono,neutro]
    print(val)
    
    """bars=plt.bar(classes,val,color=my_colors,width=0.3)
    plt.xlabel('Types of cell')
    plt.ylabel('Count')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x()+0.10, yval + .005, yval)
    num=random.randint(0,10000)
    plt.savefig('static/graph/{}'.format(name))"""
   
    text="YOUR RESULT IS SHOWN BELOW! DON'T FORGET TO SHARE YOUR RESULT WITH YOUR DOCTOR FOR FURTHER EXAMINATION. "
    bar = create_plot(classes,val)
    
    count=eos+lymph+mono+neutro
    print("COUNT",count)
    result=''
    eos_per=eos/count*100
    lymph_per=lymph/count*100
    mono_per=mono/count*100
    neutro_per=neutro/count*100
    if(40<neutro_per<80 and 20<lymph_per<40 and 2<mono_per<8 and 1<eos_per<4 ):
      result='Normal White Blood Cell Distribution.It is still advised to share your result with your doctor for further dignosis.'
    else:
        result='White Blood Cell Distribution is not within normal range.It is advised to contact your doctor at the earliest for further dignosis. '
    folder=UPLOAD_FOLDER+'/*' 
    img=glob.glob(folder)
    for i in img:
        os.remove(i)
    
    return render_template('index.html', plot=bar,title=text,username=username,age=age,gender=gender,result=result)




if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=False) 
    
