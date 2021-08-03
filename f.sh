#!/bin/bash
echo "Printing text with newline"
echo -n "Printing text without newline"
echo -e "\nRemoving \t backslash \t characters\n"
valid=true
count=1
while [ $valid ]
do
echo $count
if [ $count -eq 5 ];
then
break
fi
((count++))
done
for (( counter=10; counter>0; counter-- ))
do
echo -n "$counter "
done
printf "\n"
echo "Enter Your Name"
read name
echo "Enter Your lastname: "
read lastname
echo "Welcome $name $lastname"