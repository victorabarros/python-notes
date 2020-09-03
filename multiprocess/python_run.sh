docker rm -f apply-multi
docker rmi -f apply-multi-image:1
docker build -t apply-multi-image:1 .
docker run -p 8080:8080 --name apply-multi apply-multi-image:1
