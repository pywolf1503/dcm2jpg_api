# dcm2jpg_api
A python API built using Flask, Receives a dcm image, and returns its jpeg.

How to use?

1- install the requirements: Flask, pillow, pydicom.
2- Host the script.

Note: I've included a test.py to test the api using requests library, for that u need to replace the url in test.py with your target/convert. You also need to have a test.dcm included in same directory as your test.py, make sure the api is online and run the script. a result.jpg is what you should see on your directory after a succesful request!
