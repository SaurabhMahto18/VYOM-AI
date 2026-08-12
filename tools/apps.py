import subprocess


APP_COMMANDS = {

    "chrome": [
        "cmd",
        "/c",
        "start",
        "",
        "chrome"
    ],

    "google chrome": [
        "cmd",
        "/c",
        "start",
        "",
        "chrome"
    ],

    "notepad": [
        "notepad.exe"
    ],

    "calculator": [
        "calc.exe"
    ],

    "calc": [
        "calc.exe"
    ],

    "explorer": [
        "explorer.exe"
    ],

    "file explorer": [
        "explorer.exe"
    ],
}


def open_app(app_name):

    app_name = app_name.lower().strip()

    if app_name not in APP_COMMANDS:

        return False, f"I don't know how to open {app_name}."

    try:

        subprocess.Popen(
            APP_COMMANDS[app_name],
            shell=False
        )

        return True, f"{app_name.title()} opened."

    except Exception as error:

        return False, str(error)