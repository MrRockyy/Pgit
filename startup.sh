#!/bin/sh

mkdir -p ~/.config
cd ..
mv pgit ~/.config 
cd ~/.config/pgit
chmod +x pgit
sudo cp pgit /usr/bin/pgit



