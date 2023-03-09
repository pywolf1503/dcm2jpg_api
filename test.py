import requests

url = 'http://127.0.0.1:5000/convert'  # replace with your app's URL

with open('test.dcm', 'rb') as f:
    response = requests.post(url, files={'dicom_file': f})

# Check if the request was successful (HTTP status code 200)
if response.ok:
    # Save the JPEG response to a file
    with open('result.jpg', 'wb') as f:
        f.write(response.content)
else:
    print('Error:', response.text)