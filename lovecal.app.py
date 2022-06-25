# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 02:23:40 2022

@author: user
"""

import streamlit as st
st.set_page_config(page_title="Love calculator", page_icon="❤️", layout="centered")
st.title("❤️ Love calculator")



#form = st.form(key='submit')


with st.form(key='submit'):
    
     cols = st.columns((1, 1))
     
     input_one = cols[0].text_input ("Enter fist and lastname of First Person:")
     
     
     
     input_two = cols[1].text_input ("Enter first and lastname of Second Person:")
                                     
     input1 = len(input_one)
     input2 = len(input_two)
        
     percentage = 100 - abs(input1 * input2) - 13
     submitted =st.form_submit_button(label =  "Submit")
     
     if submitted :
         st.success("Calcultor processing...")
         st.write("**Match** = " , int(abs(percentage/2.4)), "%")
         st.balloons() 
         
         
         
         if percentage > 60:
             st.write("That is an almost good match")
             
            
             
         else: 
             st.write("That is fair; better luck next time")
             
        
         
         
         
         
         
#     else:
         #st.experimental_rerun()

     
     