def compute_score(impact, urgency, client_weight, risk):
    return round(
        (impact * 0.4) +
        (urgency * 0.25) +
        (client_weight * 0.2) +
        (risk * 0.15), 2
    )