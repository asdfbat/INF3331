IOfilename=$HOME/.bookmarks


while IFS='|' read name loc
do
	export $name="$loc"
done < $IOfilename


if [ $# -lt 2 ]
then
	echo "You forgot to supply the bookmarkname."
	exit
fi


case $1 in
	-a)
		echo "$2|$PWD" >> $IOfilename
		export $2="$PWD"
		;;
	-r)
		sed -i "/$2|/d" $IOfilename
		unset $2
		;;
	*)
		echo "$1 is not a valid command."
		exit
		;;
esac
