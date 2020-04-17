#! /bin/bash

filename=$1
touch $filename
echo "#! /usr/bin/python3" >> $filename
echo "" >> $filename
echo "import sys" >> $filename
echo "" >> $filename
chmod u+x $filename
vim $filename
