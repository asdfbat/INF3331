case $1 in
	no)
		export TZ=Europe/Oslo ;;
	us)
		export TZ=America/New_York ;;
	sk)
		export TZ=Asia/Seoul
esac

while [ true ]
do
	clear
	x=$(date +%T)
	echo $x
	sleep 1
done
