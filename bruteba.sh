#!/system/bin/sh


c=1000000000000000
hashedC="6a4ef24cb01aa0e97da4186c067128b828532db703db8872fa736a0cc0b363b1" #sha256 of 1000000000000000
knownHash=" your hash here "

start=`date +%s`
let c++
#until [ "$c" == "1000000010000000" ] #for benchmark
until [ "$hashedC" == "$knownHash" ]
do
	if [ ${#c} == "16" ]; then
		let c++
		hashedC=$(echo -n $c | sha256sum | awk '{print $1}')
		echo "$c - $hashedC"
	elif [ ${#c} == "17" ]; then
		echo "limit reached"
		end=`date +%s`
		echo $(echo "$end - $start" | bc -l)
		exit 1
	fi
done
    echo "FOUND THE CODE"
	echo $hashedC >> found.txt
	echo $c >> found.txt
	end=`date +%s`
	echo $(echo "$end - $start" | bc -l)
	exit 1