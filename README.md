# setup

basic calculator 

#!/bin/bash

x=0
while ((x!=99))
do
 echo "1.Add "
 echo "2.Sub "
 echo "3.Mul "
 echo "4.Div "
 echo "99. to quit"

read -p " Enter your choice " choice

if (($choice == 99)); then
    echo "Exiting..."
    break
fi

read -p "Enter your first number" num1
read -p "Enter your second number" num2


case $choice in
        1)
         echo "The sum is : $((num1 + num2))"
        ;;
        *)
         echo "worng input"
esac
done
