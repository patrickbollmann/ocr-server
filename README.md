# ocr-server
Simple docker container with an ocr server

small api to return ocr content as string from pdf and images.
Run ``docker-compose up`` to start server
get ocr response with POST request to ``http://localhost:5101/ocr`` with parameter ``file`` (contains the file) in body

WARNING! ABSOLUTELY NO SECURITY BUILT IN DO NOT EXPOSE PORTS!
