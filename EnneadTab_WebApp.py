##
# 
# python -m streamlit run EnneadTab_WebApp.py

import streamlit as st
import os
import getpass
import time
from streamlit_autorefresh import st_autorefresh



def main_draft():
    pace = 2 # refresh every X seconds
    max_life = 60 * 60 * 1 # 1 hour max life
    count = st_autorefresh(interval = pace * 1000, 
                        limit = max_life / pace, key="EA_counter")


    st.title('EnneadTab for Web')




    user_name = getpass.getuser()
    print (user_name)
    st.subheader('Hello {}'.format(user_name))

    user_name = os.getlogin()
    print (user_name)
    st.subheader('Hello {}'.format(user_name))


    st.title(time.time())
    st.write(max_life/pace - count)


    print ("Done!")

    st.text('Fixed width text')
    st.markdown('_Markdown_') # see *
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')

    st.code('for i in range(8): foo()')

    st.json({'foo':'bar','fu':'ba'})
    st.metric('My metric', 42, 2)### good for showing the diff

    st.image('imgs/logo.png')

    with st.sidebar:
        st.radio('Select one:', [1, 2])
        
        
if __name__ == '__main__':
    main_draft()