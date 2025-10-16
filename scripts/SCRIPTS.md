## You can run all the scripts from here

### Create a zip of address app
```bash
cd ../backend/address
zip -r address.zip .
mv address.zip ../../scripts
```
### Generate the files structure of the tree app
```bash
cd ../backend/address
tree -I 'node_modules' > ../../scripts/address-files-structure.md
```
### Install docker
```bash
sudo bash install_docker.sh
```
### Uninstall docker
```bash
sudo bash uninstall-docker.sh
```
### Restart docker services
```bash
cd ../backend
docker compose down
docker compose up --build
```

### Rebuild without cache
```bash
cd ../backend
docker-compose build --no-cache
docker-compose up -d
```

### Start Migration in Docker
```bash
#cd ..
docker exec -it backend_web_1 python manage.py makemigrations --noinput
docker exec -it backend_web_1 python manage.py migrate
```

### Run all Tests in Docker
```bash
docker exec -it backend_web_1 python manage.py test
```

### Create a new django project
```bash
cd ..
#django-admin startproject <project-name>
django-admin startproject imranslab
```

### create necessary files for docker setup
```bash
touch Dockerfile \
docker-compose.yml \
requirements.txt \
apt-requirements.txt \
.dockerignore
```