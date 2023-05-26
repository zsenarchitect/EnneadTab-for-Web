import requests

data = {
    'key1': 'value1',
    'key2': 'value2',
    # Add any additional data fields as needed
}

response = requests.post('https://zsenarchitect-enneadtab-for-web-enneadtab-webapp-z8q0ab.streamlit.app/', json=data)

if response.status_code == 200:
    print('Data sent successfully!')
else:
    print('Error sending data:', response.text)
