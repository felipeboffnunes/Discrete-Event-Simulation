def logger(mode, *args):
    log = {
        "Serving": "{0} STARTED BEING SERVED AT QUEUE {1} AT {2:.2f} - SERVICE DURATION: {3:.2f}",
        "Served": "{0} SERVED AT QUEUE {1} AT {2:.2f} - SERVICE DURATION: {3:.2f}",
        "LostRedirect": "{0} LOST WHILE REDIRECTING TO {1}. FULL QUEUE.",
        "Lost": "{0} LOST. {1} FULL.",
        "Redirected": "{0} REDIRECTED TO {1}",
        "Arrive": "{0} ARRIVES SYSTEM AT {1:.2f}",
        "Enter": "{0} ENTERS QUEUE {1} AT {2:.2f}",
        "Left": "{0} LEFT QUEUE {1} AT {2:.2f}"
    }
    return log[mode].format(*args)
