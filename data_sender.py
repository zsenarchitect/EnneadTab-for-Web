import requests
import json

# JSON data to send
data = {
    'key1': 'value1',
    'key2': 'value2',
    # Add any additional data fields as needed
}

# Send POST request with JSON data
response = requests.post('https://zsenarchitect-enneadtab-for-web-enneadtab-webapp-z8q0ab.streamlit.app/data', json=data)

# Check the response status
if response.status_code == 200:
    print('Data sent successfully!')
else:
    print('Error sending data:', response.text)
