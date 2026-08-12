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

    website_aliases = {
        "youtube": "youtube",
        "google": "google",
        "github": "github",
        "gmail": "gmail",
        "chatgpt": "chatgpt",
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

    search_words = [
        "search",
        "search karo",
        "search koro",
        "dhundo",
        "dhoondo",
        "find",
    ]

    # -----------------------------------
    # WEBSITE OPEN
    # -----------------------------------

    for word in open_words:

        if word in text:

            for name, site in website_aliases.items():

                if name in text:

                    return {
                        "action": "open_browser",
                        "target": site
                    }

    # -----------------------------------
    # GOOGLE SEARCH
    # -----------------------------------

    for word in search_words:

        if word in text:

            query = text

            for search_word in search_words:
                query = query.replace(
                    search_word,
                    ""
                )

            query = query.strip()

            if query:

                return {
                    "action": "google_search",
                    "target": query
                }

    # -----------------------------------
    # APP OPEN
    # -----------------------------------

    for word in open_words:

        if word in text:

            for name, app in app_aliases.items():

                if name in text:

                    return {
                        "action": "open_app",
                        "target": app
                    }

    # -----------------------------------
    # NORMAL CHAT
    # -----------------------------------

    return {
        "action": "none",
        "target": ""
    }