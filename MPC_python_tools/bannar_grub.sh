#!/bin/bash

DEFAULT_PORT=80

print_usage() {
  echo -e "Usage: $0 \e[1;33m<ip_address>\e[0m [\e[1;33mport\e[0m]"
  exit 1
}

grab_banner() {
  local ip_address=$1
  local port=${2:-$DEFAULT_PORT}

  echo -e "=============================================="
  echo -e "\e[1;34mBanner Grabbing Results\e[0m"
  echo -e "----------------------------------------------"
  echo -e "\e[1;33mTarget IP:\e[0m\t\t\t${ip_address}"
  echo -e "\e[1;33mTarget Port:\e[0m\t\t\t${port}"
  echo -e "\e[1;33mServer Header:\e[0m\t\t\t${result}"
  echo -e "=============================================="
}

if [[ $# -eq 0 ]]; then
  print_usage
fi

ip_address=$1
port=$2

if [[ -z "${ip_address}" ]]; then
  echo -e "\e[1;31mYou must provide an IP address.\e[0m"
  print_usage
fi

echo -e "\e[1;34mAttempting to grab the Server header of ${ip_address}\e[0m"
result=$(curl -sI "${ip_address}:${port}" | awk -F': ' '/Server/ {print $2}')
grab_banner "$ip_address" "$port"
