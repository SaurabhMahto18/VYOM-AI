from core.intent import detect_intent
from core.permissions import is_allowed

from tools.apps import open_app
from tools.browser import open_website, google_search


def execute_command(user_input):

    intent = detect_intent(user_input)

    action = intent["action"]
    target = intent["target"]

    # -----------------------------------
    # NORMAL CHAT
    # -----------------------------------

    if action == "none":

        return False, None

    # -----------------------------------
    # PERMISSION
    # -----------------------------------

    permission_action = action

    if action == "google_search":
        permission_action = "open_browser"

    if not is_allowed(permission_action):

        return True, (
            "I don't have permission "
            "to perform that action."
        )

    # -----------------------------------
    # OPEN APP
    # -----------------------------------

    if action == "open_app":

        success, message = open_app(target)

        return True, message

    # -----------------------------------
    # OPEN WEBSITE
    # -----------------------------------

    if action == "open_browser":

        success, message = open_website(target)

        return True, message

    # -----------------------------------
    # GOOGLE SEARCH
    # -----------------------------------

    if action == "google_search":

        success, message = google_search(target)

        return True, message

    return True, (
        "I don't know how to perform "
        "that action."
    )