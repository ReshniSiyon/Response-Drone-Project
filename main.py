from datetime import datetime

print("=== RESPONSE DRONE SYSTEM ===")

file = open("requests.txt", "w")

for request_id in range(1001, 1004):

    print("\n--- New Emergency Request ---")

    village = input("Enter village name: ")
    emergency = input("Enter emergency type: ")

    if emergency.lower() == "medicine":
        priority = "HIGH"
        drone = "Drone-1"
        time = "10 Minutes"
    elif emergency.lower() == "food":
        priority = "MEDIUM"
        drone = "Drone-2"
        time = "20 Minutes"
    else:
        priority = "LOW"
        drone = "Drone-3"
        time = "30 Minutes"

    current_time = datetime.now()

    print("\nEmergency Request Received!")
    print("Request ID:", request_id)
    print("Village:", village)
    print("Emergency:", emergency)
    print("Priority Level:", priority)
    print("Assigned Drone:", drone)
    print("Estimated Delivery Time:", time)

    file.write(f"Request ID: {request_id}\n")
    file.write(f"Date & Time: {current_time}\n")
    file.write(f"Village: {village}\n")
    file.write(f"Emergency: {emergency}\n")
    file.write(f"Priority: {priority}\n")
    file.write(f"Drone: {drone}\n")
    file.write(f"Time: {time}\n\n")

file.close()

print("\nAll requests saved successfully!")