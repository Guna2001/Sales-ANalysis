import streamlit as st
import pickle
import sklearn

model = pickle.load(open("sales_analysis.pkl", 'rb'))

html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Sales Analysis </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

#Header
st.title("Sales analysis")
st.subheader("Classifying a product to be manufactured or not by analysing the sales pattern")

#Getting input from user
SKU_number = st.number_input('Insert a SKU_number')
st.write('The current number is ', SKU_number)
Strengthfactor = st.number_input('Insert a Strengthfactor')
st.write('The current number is ', Strengthfactor)
PriceReg = st.number_input('Insert a priceamount')
st.write('The current number is ', PriceReg)
ItemCount = st.number_input('Insert a Item Count')
st.write('The current number is ', ItemCount)

#result
if st.button("Predict"):
    result=model.predict([[SKU_number,Strengthfactor,PriceReg,ItemCount]])
    st.success('The output is {}'.format(result))

#image
from PIL import Image
image = Image.open('stonks.png')
st.image(image, width=500, channels="RGB", output_format="auto")
