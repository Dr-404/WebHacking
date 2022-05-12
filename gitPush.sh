#!/bin/bash

read -p 'Write your commit?: ' commit

git add * & git commit -m $commit & git push -u origin main
