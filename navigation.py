def choose_path(distance, obstacle_risk, signal_strength):
    score = distance - obstacle_risk + signal_strength

    if score > 10:
        return "🟢 Safe path selected"
    else:
        return "🔄 Rerouting needed"