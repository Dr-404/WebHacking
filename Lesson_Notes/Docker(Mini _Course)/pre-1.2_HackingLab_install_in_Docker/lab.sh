#!/bin/bash


read -p "Enter port number you want to bind: " port
sudo docker run -p $port:80 -it zdresearch/advanced-web-hacking http://localhost:$port

