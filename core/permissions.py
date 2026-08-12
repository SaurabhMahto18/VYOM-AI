ALLOWED_ACTIONS = {
    "open_app": True,
    "open_browser": True,
    "file_access": False,
    "send_message": False,
    "make_call": False,
    "delete_file": False,
}


def is_allowed(action):

    return ALLOWED_ACTIONS.get(
        action,
        False
    )