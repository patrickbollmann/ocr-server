import flask
from flask import request
from flask import send_file
from flask import after_this_request
from werkzeug.utils import secure_filename
import json
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import os

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

app = flask.Flask(__name__)
app.config["DEBUG"] = False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_img_from_pdf(file):
    pages = convert_from_path(file, 350)
    image_name = "pdfAsImg.jpg"
    pages[0].save(image_name, "JPEG")
    file = "pdfAsImg.jpg"
    return file

def doOCR(file):
    filename, fileextension = os.path.splitext(file)
    if(fileextension == ".pdf"):
        file = get_img_from_pdf(file)
    ocr = pytesseract.image_to_string(Image.open(file))
    return ocr


@app.route('/', methods=['GET'])
def home():
    return "<h1>OCR Server</h1><p>use post request at /ocr to receive a string with the ocr results from your file. Just send the File in request body everything else will be handled automatically. Supported filetypes: {'pdf', 'png', 'jpg', 'jpeg'}</p>"


@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files['file']
    if file.filename == '':
            return "no file selected", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(filename)
    else:
        return "filetyoe not supported. Supproted file extensions are: {'pdf', 'png', 'jpg', 'jpeg'}", 400

    return doOCR(filename)


app.run(host='0.0.0.0')