##
# 
# python -m streamlit run EnneadTab_WebApp.py

import streamlit as st
import os
import getpass
import time
from streamlit_autorefresh import st_autorefresh
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    # Process the received data
    st.subheader("Received data:", data)

def get_local_data():
    st.subheader(os.path.expanduser("~/Documents"))
    return
    folder = "{}\Documents\EnneadTab Settings\Local Copy Dump".format(os.environ["USERPROFILE"])
    st.subheader(folder)


def main_draft():
    # CSS to change the background color
    css = """
        <style>
        body {
            background-color: #f0f0f0;
        }
        </style>
    """

    # Render the CSS
    st.markdown(css, unsafe_allow_html=True)
    
    
    
    pace = 2 # refresh every X seconds
    max_life = 60 * 60 * 1 # 1 hour max life
    count = st_autorefresh(interval = pace * 1000, 
                        limit = max_life / pace, key="EA_counter")


    st.title('EnneadTab for Web')




    user_name = getpass.getuser()
    print (user_name)
    st.subheader('Hello {}'.format(user_name))

    try:
        user_name = os.getlogin()
        print (user_name)
        st.subheader('Hello {}'.format(user_name))
    except Exception as e:
        st.subheader(e)


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
    st.metric('Warning changes:', 100, -32)
    st.image('imgs/logo.png',use_column_width=True, caption="This App is created by Sen Zhang")

    with st.sidebar:
        st.radio('Select one:', [1, 2])
        
    get_local_data()
    
    
    st.text('test get POST')
    app.run( )
    st.text('test done')
        
        
if __name__ == '__main__':
    main_draft()