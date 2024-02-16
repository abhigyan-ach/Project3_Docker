To execute the docker container, you can build it from the docker file:
##Building image from Dockerfile:
```docker build -t image_name .  ```

You may check the docker images created using:
```docker images```

Additionally, you can remove images using:
```docker rmi -f image_name```

##Map host OS directory to docker directory ( to access text files from python script ) and running Docker container:
```docker run -it -v "$(pwd)":/home/data image name ```





