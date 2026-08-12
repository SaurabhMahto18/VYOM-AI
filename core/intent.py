def detect_intent(user_input):

    text = user_input.lower().strip()

    app_aliases = {
        "chrome": "chrome",
        "google chrome": "chrome",
        "notepad": "notepad",
        "calculator": "calculator",
        "calc": "calculator",
        "file explorer": "file explorer",
        "explorer": "explorer",
    }

    open_words = [
        "open",
        "start",
        "launch",
        "run",
        "kholo",
        "khol",
        "chalao",
        "chala",
    ]

    for word in open_words:

        if word in text:

            for name, app in app_aliases.items():

                if name in text:

                    return {
                        "action": "open_app",
                        "target": app
                    }

    return {
        "action": "none",
        "target": ""
    }