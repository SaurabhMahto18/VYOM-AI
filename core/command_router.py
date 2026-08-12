from core.intent import detect_intent
from core.permissions import is_allowed
from tools.apps import open_app


def execute_command(user_input):

    intent = detect_intent(user_input)

    action = intent["action"]
    target = intent["target"]

    if action == "none":

        return False, None

    if not is_allowed(action):

        return True, "I don't have permission to perform that action."

    if action == "open_app":

        success, message = open_app(target)

        return True, message

    return True, "I don't know how to perform that action."