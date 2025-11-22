LOG_FILE="system_health.log"
CPU_THRESHOLD=80
MEM_THRESHOLD=20

CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
MEM_AVAILABLE=$(free | grep Mem | awk '{printf "%.0f", $7/$2 * 100}')

if [ $CPU_USAGE -gt $CPU_THRESHOLD ] || [ $MEM_AVAILABLE -lt $MEM_THRESHOLD ]; then
	echo "High CPU Usage: $CPU_USAGE%" >> $LOG_FILE
	echo "Low Memory Available: $MEM_AVAILABLE%" >> $LOG_FILE
else
	echo "Normal CPU Usage: $CPU_USAGE%" >> $LOG_FILE
	echo "High Memory Available: $MEM_AVAILABLE%" >> $LOG_FILE
fi
