docker rm -f flask-excel
docker rmi -f flask-excel-image:1.0
docker build -t flask-excel-image:1.0 .
docker run -d -p 8090:8090 --name flask-excel flask-excel-image:1.0
sleep .5 && echo
echo 'docker image ls'
docker image ls -a | grep REPOSITORY && docker image ls -a | grep flask-excel-image && echo
echo 'docker ps'
docker ps -a | grep CONTAINER && docker ps -a | grep flask-excel && echo
