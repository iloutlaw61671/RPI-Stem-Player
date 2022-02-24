#!bin/bash
#cd Downloads
echo "Which song?"  #string to rename song
read SONG
cd Downloads
mmv completed_live_86617bc5b47b15b6437be80f67679f7b\* $SONG\#1     #replaces Completed.... with songname with _*stem*
cd ..
mv Downloads/*.wav musicproj  #moving from downloads from project directory

$SHELL
