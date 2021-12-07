echo "Generating will be started, just press enter to stop!"
sleep 5
python3 coordinate.py &
python3 cowsinsight.py &
python3 speed.py &
python3 temperature.py &
python3 anomaly.py &
read 1
killall python3