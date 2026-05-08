def extract_actions(text):
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    action_keywords = [
        "review", "rebalance", "plan", "invest",
        "update", "check", "analyze", "send"
    ]

    actions = []

    for sentence in sentences:
        if any(keyword in sentence.lower() for keyword in action_keywords):
            actions.append(sentence)

    return actions