pip install -r requirements.txt
cp chromedriver ~/../usr/local/bin/
cp geckodriver ~/../usr/local/bin/

# docker rmi -f selenium_docker
# docker build -t selenium_docker .
# docker run -it -v $(pwd):/src/python-notes -w /src/python-notes \
#         -p 8091:8091 --name python-notes selenium_docker bash
