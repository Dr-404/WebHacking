<h1 align="center">ZD Lab Installation for Pentest</h1>

## Steps for Lab Installation

1. Install docker software in Linux
2. Pull the docker image 
3. kill server
4. Scripting




## Install Docker in Linux
`sudo apt install docker.io`

## Enable Docker

`sudo systemctl enable docker --now`


## You can now get started with using docker, with sudo. If you want to add yourself to the docker group to use docker without sudo, an additional step is needed:???

`sudo usermod -aG docker $USER`



## Pull the docker imag and install it

> ## Interactive mode

> `sudo docker run -p 8080:80 -it zdresearch/advanced-web-hacking http://localhost:8080`

> ## Demon Mode
> `sudo docker run -p 8080:80 -td zdresearch/advanced-web-hacking http://localhost:8080`

## How to kill server

`sudo docker kill imageid`