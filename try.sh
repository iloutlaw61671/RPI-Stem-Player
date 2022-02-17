#!/bin/bash

echo "Welcome to VIK'S STEMPLAYER"

echo "Enter 's' to select audio or 'd' to download via YouTube"

read AUDCH

echo $AUDCH

if [ "$AUDCH" == 'S' ]; then
	echo "its s"
	ls
	#$SHELL
elif [ "$AUDCH" == 'd' ]; then
	echo "Enter preferred YouTube url"
	read URL
	echo $URL
	echo "Name the song"
	read SONG
	youtube-dl --extract-audio --audio-format wav -o "$SONG.%(ext)s" $URL	
fi
