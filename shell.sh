#!bin/bash
#cd Downloads
echo "Which song?"
read SONG
cd Downloads
mmv completed_live_cea497b9b68b6a27e21b11c6f5129788\* $SONG\#1
cd ..
mv Downloads/*.mp3 musicproj

$SHELL
