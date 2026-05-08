from utils.scoring import compute_score

def classify_action(action, client_type):
    action_lower = action.lower()

    # Impact
    if "rebalance" in action_lower or "invest" in action_lower:
        impact = 5
    elif "review" in action_lower or "plan" in action_lower:
        impact = 3
    else:
        impact = 2

    # Urgency
    if "urgent" in action_lower or "immediately" in action_lower:
        urgency = 5
    elif "soon" in action_lower:
        urgency = 3
    else:
        urgency = 2

    # Risk signal
    if "risk" in action_lower or "drift" in action_lower:
        risk = 5
    else:
        risk = 2

    # Client weight
    client_weight = 5 if client_type == "HNI" else 3

    score = compute_score(impact, urgency, client_weight, risk)

    return score


def prioritize(actions, client_type):
    results = []

    for action in actions:
        score = classify_action(action, client_type)

        if score >= 4:
            priority = "HIGH"
        elif score >= 3:
            priority = "MEDIUM"
        else:
            priority = "LOW"

        reason = generate_reason(action, score)

        results.append({
            "action": action,
            "score": score,
            "priority": priority,
            "reason": reason
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)


def generate_reason(action, score):
    if score >= 4:
        return "High financial impact and/or risk-driven decision"
    elif score >= 3:
        return "Moderate planning relevance"
    else:
        return "Administrative or low-impact action"