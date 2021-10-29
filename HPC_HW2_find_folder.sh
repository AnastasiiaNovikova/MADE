#!bin/bash

if [ -f "./linux" ] ; then
    echo course
else
   echo very easy
   touch linux
   echo "course is easy" > linux
fi
