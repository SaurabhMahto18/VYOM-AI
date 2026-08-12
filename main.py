import threading
import tkinter as tk

from core.brain import ask_vyom
from core.command_router import execute_command

from voice.speech_to_text import listen
from voice.text_to_speech import speak

from ui.window import VYOMWindow


def update_state(app, state):

    app.root.after(
        0,
        lambda: app.set_state(state)
    )


def update_user_text(app, text):

    app.root.after(
        0,
        lambda: app.set_user_text(text)
    )


def assistant_loop(app):

    while True:

        # -----------------------------
        # LISTENING
        # -----------------------------

        update_state(app, "listening")

        user_input = listen()

        if not user_input:
            continue

        update_user_text(app, user_input)

        # -----------------------------
        # EXIT
        # -----------------------------

        if user_input.lower().strip() in [
            "exit",
            "quit",
            "bye",
            "goodbye",
            "stop"
        ]:

            update_state(app, "speaking")

            speak("Goodbye! See you soon.")

            app.root.after(
                0,
                app.root.destroy
            )

            break

        try:

            # -----------------------------
            # THINKING
            # -----------------------------

            update_state(app, "thinking")

            handled, result = execute_command(
                user_input
            )

            # -----------------------------
            # COMPUTER COMMAND
            # -----------------------------

            if handled:

                response = result

            # -----------------------------
            # NORMAL AI CONVERSATION
            # -----------------------------

            else:

                response = ask_vyom(
                    user_input
                )

            # -----------------------------
            # SPEAKING
            # -----------------------------

            update_state(app, "speaking")

            speak(response)

            update_state(app, "idle")

        except Exception as error:

            print("Error:", error)

            update_state(app, "error")

            speak(
                "Sorry, something went wrong."
            )

            update_state(app, "idle")


def main():

    app = VYOMWindow()

    assistant_thread = threading.Thread(
        target=assistant_loop,
        args=(app,),
        daemon=True
    )

    assistant_thread.start()

    app.run()


if __name__ == "__main__":
    main()