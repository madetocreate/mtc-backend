def log(msg):
    with open("logs/agent.log", "a") as f:
        f.write(msg + "\n")
