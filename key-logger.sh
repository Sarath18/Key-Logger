xinput --list

echo -n "Enter your keyboard id: "
read id

echo "Logging key data: "
xinput --test $id > log.txt