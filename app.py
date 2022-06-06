import streamlit as st
import pickle
import xgboost

#Importing the model
with open('sales_analysis-2.pkl', 'rb') as f:
    bst = pickle.load(f)
bst._Booster.save_model('your_model_binary.model')
model = bst.load_model('your_model_binary.model')

#Prediction Part
def predict_note_authentication(SKU_number,Strengthfactor,PriceReg,ItemCount):
    prediction=classifier.predict([[SKU_number,Strengthfactor,PriceReg,ItemCount]])
    print(prediction)
    return prediction

#Formatting CSS
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

#Header
st.title("Sales analysis")
st.subheader("Classifying a product to be manufactured or not by analysing the sales pattern")

#Getting inputu from user
SKU_number = st.number_input('Insert a SKU_number')
st.write('The current number is ', SKU_number)
Strengthfactor = st.number_input('Insert a Strengthfactor')
st.write('The current number is ', Strengthfactor)
PriceReg = st.number_input('Insert a priceamount')
st.write('The current number is ', PriceReg)
ItemCount = st.number_input('Insert a Item Count')
st.write('The current number is ', ItemCount)

#result
result=""
if st.button("Predict"):
    result=predict_note_authentication(SKU_number,Strengthfactor,PriceReg,ItemCount)
st.success('The output is {}'.format(result))

#image
from PIL import Image
image = Image.open('stonks.png')
st.image(image, width=500, channels="RGB", output_format="auto")

