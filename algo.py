# Assume we have vehicle counts for North-South and East-West directions
vehicle_count_ns = 10
vehicle_count_ew = 5

# Default green time for both directions
green_time_ns = 30
green_time_ew = 30

# Adjust green time based on vehicle count
if vehicle_count_ns > vehicle_count_ew:
    green_time_ns += (vehicle_count_ns - vehicle_count_ew) * 2  # Adding extra time
    green_time_ew -= (vehicle_count_ns - vehicle_count_ew) * 2  # Reducing time for East-West

elif vehicle_count_ew > vehicle_count_ns:
    green_time_ew += (vehicle_count_ew - vehicle_count_ns) * 2
    green_time_ns -= (vehicle_count_ew - vehicle_count_ns) * 2

# Ensuring that green times don't drop below a minimum threshold
green_time_ns = max(green_time_ns, 15)  # Minimum green time 15 seconds
green_time_ew = max(green_time_ew, 15)
