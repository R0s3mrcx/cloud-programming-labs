def run_command(cmd):
    match cmd:
        case "start":
            return "STARTING"
        case "stop":
            return "STOPPING"
        case "status":
            return "STATUS"
        case _:
            return "UNKNOWN_COMMAND"


print(run_command("start"))
print(run_command("stop"))
print(run_command("status"))
print(run_command("restart"))
