while :
do
  echo ping && ping -c 1 $1 || echo reset && python ./powerOperationsByIP.py $1 reset
  echo sleep && sleep 180
done
