#!/bin/sh

mkdir -p ~/.config
rm -r ~/.config/pgit
cd ..
mv pgit ~/.config 
cd /.config/pgit
chmod +x pgit
rm -r /usr/bin/pgit
sudo mv pgit /usr/bin/



