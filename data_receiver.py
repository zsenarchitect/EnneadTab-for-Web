import streamlit as st
from flask import Flask, request
from streamlit.report_thread import get_report_ctx

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    ctx = get_report_ctx()
    session_id = ctx.session_id
    data = request.json
    # Process the received data
    st.write("Session ID:", session_id)
    st.write("Received data:", data)
    return 'Data received successfully!'

if __name__ == '__main__':
    app.run()
