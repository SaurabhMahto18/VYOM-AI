import webbrowser
from urllib.parse import quote


SAFE_SITES = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chatgpt.com",
}


def open_website(site):

    site = site.lower().strip()

    if site not in SAFE_SITES:
        return False, f"I don't have {site} in my safe website list."

    try:

        webbrowser.open(SAFE_SITES[site])

        return True, f"Opening {site.title()}."

    except Exception as error:

        return False, str(error)


def google_search(query):

    query = query.strip()

    if not query:
        return False, "Please tell me what to search."

    url = (
        "https://www.google.com/search?q="
        + quote(query)
    )

    try:

        webbrowser.open(url)

        return True, f"Searching Google for {query}."

    except Exception as error:

        return False, str(error)