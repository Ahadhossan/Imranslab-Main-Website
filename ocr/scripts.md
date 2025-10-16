### build image from Dockerfile
```bash
docker build -f Docker.debugger -t pydebugger2 ..
```

### Create container from image
1. way 1
```bash
docker run -d -p 5678:5678 --name pydebugger1 debugger1
```
2. way 2
```bash
 
```

### Start created container
```bash
docker start python-debug-server
```

### Check running container
```bash
docker ps
```

### Check logs of a container
```bash
docker logs pydebugger1
```

### Delete docker image
```bash 
docker rmi e17dc104caec
```

### Delete docker container
```bash 
docker rm pydebugger
```

### Check all images
```bash 
docker images
```

### docker login
```bash 
docker login
```

###

```bash
docker compose down && docker compose build && docker compose up
```


########### Jenkins ###########
## For Slave

### Install Java JRE in slave
```bash
sudo su -i
sudo apt update; sudo apt upgrade -y
sudo apt install openjdk-17-jre curl git -y
```
### Install docker-compose, docker
```bash
# Update package database
sudo apt update

# Install dependencies
sudo apt install -y curl jq

# Download the latest stable version of Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r .tag_name)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Set permissions to make docker-compose executable
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker-compose --version


sudo apt update

# Install Docker
sudo apt install -y docker.io

# Start Docker service
sudo systemctl start docker

# Enable Docker to start on boot
sudo systemctl enable docker

# Verify Docker installation
docker --version

```
### Connect slave to master.
slave username : slave
slave Pass : national

```bash
cd /opt/
mkdir jenkins 
chmod 755 jenkins
cd jenkins

ssh-keygen
cd ~/.ssh/
cat id_rsa
```

########### Permissions ################
command : chmod 755 <folder-name> 
Description : https://grok.com/share/c2hhcmQtMg%3D%3D_bfc2e070-596d-457a-92c9-186cdf686d38
    
