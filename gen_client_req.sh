#!/bin/bash

commands=(
    "curl --interface enp3s0 -w '%{time_total}\n' -o /dev/null -s -X GET http://192.0.2.17:8000"
)

total_time=0
total_requests=0

start_time=$(date +%s.%N)

for i in {1..1000}
do
    for cmd in "${commands[@]}"
    do
        response_time=$(eval "$cmd")
        total_time=$(echo "$total_time + $response_time" | bc)
        total_requests=$((total_requests + 1))
    done
done

end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)
average_time=$(echo "scale=4; $total_time / $total_requests" | bc)
rate=$(echo "scale=2; $total_requests / $duration" | bc)

echo "Average response time: $average_time seconds"
echo "Total requests sent: $total_requests"
echo "Total duration: $duration seconds"
echo "Effective request rate: $rate requests/sec"
