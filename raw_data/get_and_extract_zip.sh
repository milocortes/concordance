#/bin/bash
DIR=$1
URL=$2

echo "$DIR $URL"
cd $DIR 
wget $URL
unzip *.zip
pwd 
ls
rm *.xml
rm *.zip
