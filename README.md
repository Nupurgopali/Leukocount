# MOTIVATION BEHIND LEUKOCOUNT
LEUKOCOUNT aids in automating the process of detection of blood-based diseases. White blood cell (WBC) count is a valuable metric for assisting with 
diagnosis or prognosis of various diseases such as coronary heart disease, type 2 diabetes, or infection. In the current pandemic situation, with number of patients increasing 
exponentially each day. It is difficult to manually count and keep track of their white blood cells.

It is crucial to maintain ideal count of white blood cells, drastic decrease in the number of WBC's leads to higher risk of getting an infection and an abnormal 
increase in the number could indicated diseases such as bone-marrow, cancer, etc.

Apart from this a WBC count can detect hidden infections within your body and alert doctors to undiagnosed medical conditions, such as autoimmune diseases, 
immune deficiencies, and blood disorders. This test also helps doctors monitor the effectiveness of chemotherapy or radiation treatment in people with cancer.

Recent studies have revealed that raised white blood cell and neutrophil counts along with a fall in lymphocyte count are seen in some patients with COVID-19.
Other studies have shown that determining the neutrophil-to-lymphocyte ratio could serve as a biomarker that could predict the infection's outcome.

# LEUKOCOUNT
This motivated me to use deep learning architecture to automate the process of counting different types of White Blood Cells present in a blood sample.

LEUKOCOUNT uses deep learning models to detect four different types of WBC's:
1. EOSINOPHIL
2. LYMPHOCYTE
3. MONOCYTE
4. NEUTROPHIL 
and counts each type of WBC's present in the sample.
It attempts in making the entire process of detecting and counting number of WBC's efficient, effortless, cheap and timing-saving.

# DATA

The data was procured from kaggle. Source:https://www.kaggle.com/paultimothymooney/blood-cells.
The dataset contains 12,500 augmented images of various types of white blood cells (JPEG) with metadata in CSV form. 
That includes 3,000 images divided into 4 different white blood cell types (classes).This data was further broken down into training and testing dataset,in order to 
train and evaluate the model performance.

More data was generated using image augumentation.

# ARCHITECTURE

I used transfer learning techinique to build a deep learning model that could identify different types of white blood cells.The model used for transfer learning was VGG19.
Architecture of VGG19 is shown below:



![llustration-of-the-network-architecture-of-VGG-19-model-conv-means-convolution-FC-means](https://user-images.githubusercontent.com/53776611/101287184-b7dac000-3814-11eb-9f47-9b85a3d800a3.png)


<p>The weights were taken from the VGG19 model using transfer learning and the laster layer was modified according to the input classes.(i.e. 4 classes).The model was trained on the training data
and it was evaluated on the testing data.</p>

#### TECHNOLOGIES USED:
![image](https://user-images.githubusercontent.com/53776611/102008028-94070500-3d53-11eb-8689-5e65fd21e0bb.png)
![image](https://user-images.githubusercontent.com/53776611/102008058-cf093880-3d53-11eb-80ad-8dcb008e2ea4.png)
![image](https://user-images.githubusercontent.com/53776611/102008097-0841a880-3d54-11eb-8c69-7401a0b15529.png)
![image](https://user-images.githubusercontent.com/53776611/102008113-23141d00-3d54-11eb-9bf5-b662f9783ee8.png)


# PERFORMANCE OF THE MODEL:

<li>The traing accuracy of the model was: 98%</li>
<li>The test accuracy of the model was: 91.5%</li>


#### The classification report of the model:

![image](https://user-images.githubusercontent.com/53776611/101287551-e6f23100-3816-11eb-8d27-74bfb91207d2.png)

#### The confusion matrix of the classification model is as follows:

![image](https://user-images.githubusercontent.com/53776611/101287596-2ae53600-3817-11eb-8a67-75e0b4c79fd5.png)

The classification and confusion matrix indicates that the model has good performance and can be used for identifying different types of WBC's.

# RESULT

The result was produced in form of a graph that indicated the number of different types of WBCs present in the sample. A sample result is shown here:


![image](https://user-images.githubusercontent.com/53776611/102007912-eb58a580-3d52-11eb-8bb6-7caafd319bbd.png)

# ADVANTAGE

Currently the different types of WBC's in a sample are being counted manually which requires expensive medical equipments,is a very time consuming process, leads to delay
in the diagnosing a particular disease,since WBC's play an important role in diagnosing almost all types of diseases.

#### The primary advantages of using LEUKOCOUNT are:
<li>1. It does not require any expensive medical tools to identify and count the different types of WBC present in the sample.</li>
<li>2. It makes the entire process faster and provides accurate results within few hours reduces the patients wait time by weeks.It provides rapid result on a large scale of 
blood cell counting, almost instantly.</li>
<li>3.It makes it easier for the doctors to formulate a treatment plan, incase the patient has been diagnosed with a disease.Especially in the current pandemic situation
where the number of patient's is increasing day by day.It allows doctor to get faster result and allow them to quickly jump start on the treatment plan.</li>

## RUN

To run, download the source code. Open the source code directory in any editor(preferably VS-Code) and run app.py file.
<p>Using terminal then use the command: python app.py </p>
<p>Visit :http://127.0.0.1:5000/ link to interact with the website!</p>
