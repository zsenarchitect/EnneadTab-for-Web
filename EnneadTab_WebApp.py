##
# 
# python -m streamlit run EnneadTab_WebApp.py

import streamlit as st
import os
import getpass

user_name = getpass.getuser()
print (user_name)


st.title('EnneadTab for Web')


st.subheader('Hello {}'.format(user_name))



print ("Done!")