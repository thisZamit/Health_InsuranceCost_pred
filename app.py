import numpy as np
import pickle
import streamlit as st
def cost_prediction(Height,Weight,Age,Smoker):
  DTRmodel = pickle.load(open('DTRmodel.pkl','rb'))
  bmi = int(Weight/(Height*Height))
  if(Smoker.lower()=='yes'):
    smoker=1
  else:
    smoker=0
  res = DTRmodel.predict(np.array([[bmi,smoker,Age]]))
  return res

def main():
    st.title("Health insurance cost prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Health insurance cost Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Height = st.number_input("Enter height in meters(1.2)")
    Weight = st.number_input("Weight")
    Age = st.number_input("Age")
    Smoker = st.text_input("Smoker","Type yes or no")
    result =[0.0]
    if st.button("Predict"):
        result=cost_prediction(Height,Weight,Age,Smoker)
        st.success('Your cost for basic health insurance would be {} rupees'.format(round(result[0])))

if __name__ == '__main__':
  main()
