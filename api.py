from flask import Flask, request, Response
import io
import pydicom
from PIL import Image

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    # Get DICOM file from request
    dicom_file = request.files['dicom_file'].read()

    # Convert to JPEG
    jpeg_data = convert_to_jpeg(dicom_file)

    # Return JPEG file as response
    response = Response(jpeg_data, mimetype='image/jpeg')
    response.headers['Content-Disposition'] = 'attachment; filename=result.jpg'

    return response

def convert_to_jpeg(dicom_file):
    # Load DICOM file
    ds = pydicom.dcmread(io.BytesIO(dicom_file))

    # Extract image data
    img = ds.pixel_array

    # Convert to PIL image
    pil_img = Image.fromarray(img)

    # Save as JPEG
    with io.BytesIO() as output:
        pil_img.save(output, format='JPEG')
        jpeg_data = output.getvalue()

    return jpeg_data

if __name__ == '__main__':
    app.run(debug=True)