#!/bin/bash

read -p "Please port nubmer your want to bind : " port
read -p "Please enter name for container : " name

sudo docker run --name $name -p $port:9000 -v "/var/run/docker.sock:/var/run/docker.sock" portainer/portainer-ce

