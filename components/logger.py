def logger(mode, *args):
    log = {
        "Serving": "{0} STARTED BEING SERVED AT QUEUE {1} AT {2:.2f} - SERVICE DURATION: {3:.2f}".format(*args),
        "Served": "{0} SERVED AT QUEUE {1} AT {2:.2f} - SERVICE DURATION: {3:.2f}".format(*args),
        "Lost": "{0} LOST WHILE REDIRECTING TO {1}. FULL QUEUE.".format(*args),
        "Redirected" : "{0} REDIRECTED TO {1}".format(*args),
        "Arrive" : "{0} ARRIVES SYSTEM AT {1:.2f}".format(*args),
        "Enters" : "{0} ENTERS QUEUE {1} AT {2:.2f}".format(*args),
        "Left": "{0} LEFT QUEUE {1} AT {2:.2f}".format(*args),
        "Entity" : "ENTITY {}".format(*args)
    }
    return log[mode]