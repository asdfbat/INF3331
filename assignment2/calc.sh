
# Alternative unreadable syntax for checking validity of operator. Actually readable syntax below.
# [ $1 == "S" ] || [ $1 == "P" ] && [ $1 == "M" ] || [ $1 == "m" ] && echo "$1 is not a valid operator."; exit
# operator = $1

case $1 in
	S)
		operation="S" ;;
	P)
		operation="P" ;;
	M)
		operation="M" ;;
	m)
		operation="m" ;;
	*)
		echo "$1 is not a valid operator."; exit ;;
esac

shift
result=$1
shift
for arg in $@
do
	case $operation in
		S)
			let "result+=$arg" ;;
		P)
			let "result*=$arg" ;;
		M)
			[ $arg -gt $result ] && result=$arg ;;
		m)
			[ $arg -lt $result ] && result=$arg ;;
	esac
done

echo $result
