import requests
import json

# JSON data to send
data = {
    'key1': 'value1',
    'key2': 'value2',
    # Add any additional data fields as needed
}

# Send POST request with JSON data
main_url = "https://zsenarchitect-enneadtab-for-web-enneadtab-webapp-z8q0ab.streamlit.app/data"
test_url = "https://zsenarchitect-enneadtab-for-web-data-receiver-wd0la7.streamlit.app/data"

fake_url = "https://zsenarchitect-enneadtab-for23f-web-data-receiver-wd0la7.streamlit.app/data"

print (data)
response = requests.post(main_url, json=data)
print (response)
# Check the response status
if response.status_code == 200:
    print('Data sent to main successfully!')
else:
    print('Error sending main data:', response.text)


response = requests.post(test_url, json=data)
print (response)
# Check the response status
if response.status_code == 200:
    print('Data sent  test successfully!')
else:
    print('Error sending test data:', response.text)
    
    
    
response = requests.post(fake_url, json=data)
print (response)
# Check the response status
if response.status_code == 200:
    print('Data sent  fake successfully!')
else:
    print('Error sending fake data:', response.text)