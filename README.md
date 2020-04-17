# Music Mangement Application

A platform to upload, stream and share music files at large scale. 

## TODO

- [x] Flask app config
- [x] Sqlalchemy and migrations
- [x] Flask CRUD
- [x] create async job
- [x] s3 client and upload
- [x] Frontend streaming and download
- [x] User authentication
- [x] File Sharing
- [x] Containerization of application using docker

## PREREQUISITES

INSTALL DOCKER AND DOCKER-COMPOSE TO RUN MULTIPLE MICRO SERVICES AT EASE

refer <https://docs.docker.com/get-docker/> for installtion of docker
refer <https://docs.docker.com/compose/install/> for installation of docker-compose

## INSTALLATION

NOTE: Redis server must not be installed in your system. If installed please stop the service using:

```bash
sudo systemctl stop redis.service
```

Run this command in project and the project is deployed on your local system.

```bash
docker-compose up
```

The website will be live on your <http://127.0.0.1:5000>