#!/bin/bash

read -p 'Write your commit?: ' commit
cd /home/Dr.404/Desktop/myClass/webhacking
git add * & git commit -m $commit & git push -u origin main
