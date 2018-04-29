#!/bin/sh
cd photos
echo "Taking the Photo"
now=$1 #Now is the filename time stamp
#take pic with webcam
#fswebcam -d /dev/video0 $now.jpg
#Take video with PI Cam
#raspivid -o $now.h264 -t 10000
#Take still with PI Cam
raspistill -o $now.jpg
echo "Pic Taken"
echo""
#ring Bell
echo "Ringing Bell"
echo ""
echo ""
cd ..
omxplayer DBSE.mp3
