import subprocess
import webbrowser
def launch(value):
    try:
        subprocess.Popen(f"start {value}", shell=True)
        return "Success"
    except:
        return f"{value} could not be found in Start Menu Programs."

def run_action(action, value):
    if action == "launch":
        return launch(value)
