def run_command(cmd):
    commands = {
        "start": "System starting",
        "stop": "System stopping",
        "status": "System status OK"
    }
    return commands.get(cmd, "Unknown command")

print(run_command("start"))
