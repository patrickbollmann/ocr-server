FROM python:3.8
EXPOSE 5000

# Updating apt
RUN apt-get -y update
# Install required packages
RUN apt-get install tesseract-ocr -y
RUN apt-get install poppler-utils -y

COPY . /app
WORKDIR /app
# update pip
RUN pip install --upgrade pip
#download required python packages
RUN pip install -r requirements.txt
#run server
CMD ["python", "./ocr-server.py"]