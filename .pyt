def analyze_scam(text):

    text = text.lower()

    score = 0
    reasons = []

    urgency_words = [
        "urgent",
        "immediately",
        "act now",
        "today",
        "last warning"
    ]

    sensitive_words = [
        "otp",
        "pin",
        "password",
        "cvv",
        "upi pin"
    ]

    threat_words = [
        "account blocked",
        "account suspended",
        "legal action",
        "blocked today"
    ]

    reward_words = [
        "you won",
        "lottery",
        "prize",
        "congratulations",
        "claim your reward"
    ]

    # Check urgency
    for word in urgency_words:
        if word in text:
            score += 15
            reasons.append("Uses urgency to pressure you")

    # Check sensitive information
    for word in sensitive_words:
        if word in text:
            score += 30
            reasons.append("Requests sensitive information")

    # Check threats
    for word in threat_words:
        if word in text:
            score += 20
            reasons.append("Uses threatening language")

    # Check rewards
    for word in reward_words:
        if word in text:
            score += 20
            reasons.append("Offers suspicious rewards")

    # Limit score to 100
    score = min(score, 100)

    # Determine risk
    if score >= 56:
        risk = "HIGH RISK"
    elif score >= 26:
        risk = "SUSPICIOUS"
    else:
        risk = "LOW RISK"

    return {
        "risk_score": score,
        "risk_level": risk,
        "reasons": list(set(reasons))
    }