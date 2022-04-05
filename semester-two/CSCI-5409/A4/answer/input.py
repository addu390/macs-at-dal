def select_tier(email, message):
    tier = "UNKNOWN"
    message = message.lower()
    if any(word in message for word in ["account", "password"]):
        tier = "TIER_1"
    if any(word in message for word in ["computer", "laptop", "printer"]):
        tier = "TIER_2"
    if email.strip() == "rhawkey@dal.ca":
        tier = "TIER_3"

    return tier


def form_input(event, context):
    tier = select_tier(event["email"], event["message"])
    return {
        "email": event["email"],
        "message": event["message"],
        "tier": tier
    }

