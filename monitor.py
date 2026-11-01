import time
import random

# Simulate the status of a critical logistics service
# In a real-world scenario, this would be an external API call
# or checking a service's health endpoint.

def check_service_status(service_name):
    """Simulates checking the uptime of a service."""
    # Randomly simulate downtime (e.g., 10% chance of being down)
    is_up = random.random() > 0.1
    if is_up:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {service_name}: UP")
        return True
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {service_name}: DOWN - ALERT!")
        return False

if __name__ == "__main__":
    services_to_monitor = [
        "Cargo Tracking API",
        "Warehouse Management System",
        "Route Optimization Service"
    ]

    print("Starting Uptime Monitoring Simulation...")
    print("--------------------------------------")

    while True:
        for service in services_to_monitor:
            check_service_status(service)
        # Check every 60 seconds
        time.sleep(60)
