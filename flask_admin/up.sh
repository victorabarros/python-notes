docker rm -f flask-admin
docker rmi -f flask-admin-image:1.0
docker build -t flask-admin-image:1.0 .
docker run -d -p 8090:8090 --name flask-admin flask-admin-image:1.0
sleep .5 && echo
docker image ls && echo
docker ps && echo
curl -X GET http://localhost:8090/admin/
