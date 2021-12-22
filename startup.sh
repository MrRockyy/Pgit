#!/bin/sh

mkdir -p ~/.config
sudo rm -r ~/.config/pgit 
cd ..
mv pgit ~/.config 
cd ~/.config/pgit
chmod +x pgit
sudo cp pgit /usr/bin/pgit



