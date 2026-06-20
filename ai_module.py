def detect_obstacle(obstacle_detected):
    if obstacle_detected:
        return "🚧 Obstacle detected → Change direction"
    else:
        return "✅ Path is clear"


def detect_emergency(smoke_level):
    if smoke_level > 5:
        return "🚨 Emergency detected (Fire/Smoke zone)"
    return "🟢 Normal area"