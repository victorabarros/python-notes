
##### Clean up all containers and images
```shell
docker rm -f $(docker ps -aq)

docker rmi -f $(docker image ls -aq)
docker image ls -a && docker ps -a
```

##### Run Script with docker
```shell
docker build --rm -t app-image:1.0 .
docker run -it -d --rm --name running-app app-image:1.0
docker exec -it running-app bash
```
