def enrich_context(meeting_type):
    if meeting_type == "Portfolio Review":
        return "Focus on performance, allocation, and rebalancing"
    elif meeting_type == "Tax Planning":
        return "Focus on tax-saving opportunities and compliance"
    else:
        return "General advisory discussion"