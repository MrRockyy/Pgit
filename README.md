# Pgit

pgit is a real time control of versions tool

## installation 

`git clone https://github.com/MrRockyy/pgit.git`

`cd pgit`

`chmod +x startup.sh`

`./startup.sh`

## how to use?

1. use `pgit init` in the main folder of your project for initilized git in your main folder 
2. use `pgit real` in the main folder  of your project in other terminal to activate  automatic upload when it detect changes
  
- use `pgit upload` for upload the current version of your project 

- use `pgit ntag ` for create a featured version 

example: v1.0.01 v1.0.12

- for remove a tag use `git tag -d <tag>`
- for remove a publish tag use ` git push origin --delete <tag>`

