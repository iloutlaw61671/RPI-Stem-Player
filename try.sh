#!/bin/bash

echo "Welcome to VIK'S STEMPLAYER"

echo "Enter 's' to select audio or 'd' to download via YouTube"

read AUDCH

echo $AUDCH

if [ "$AUDCH" == 's' ]; then
	echo "Select a local song"
	ls
	#$SHELL
	echo "Choose the audio files you would like to use"
	read -r FIRST SECOND THIRD FOURTH FIFTH
	echo "Enter auth Tokem"
	read AUTH
	python audio.py $AUTH $FIRST $SECOND $THIRD $FOURTH $FIFTH                #Command to play audio with files as argument

elif [ "$AUDCH" == 'd' ]; then
	echo "Enter preferred YouTube url"
	read URL
	echo $URL
	echo "Name the song"
	read SONG
	youtube-dl --extract-audio --audio-format wav -o "$SONG.%(ext)s" $URL           #Command to download audio in .wav format
	echo "Go to main directory and run \"bash shell.sh\" to find the audio"	
fi
