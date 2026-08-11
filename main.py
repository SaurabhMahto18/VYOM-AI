from core.brain import ask_vyom
from voice.speech_to_text import listen


def main():

    print("=" * 50)
    print("                  VYOM AI")
    print("          Virtual Yielding Omni Mind")
    print("              Think. Learn. Act.")
    print("=" * 50)

    print("\nVYOM: Hello! I am VYOM.")
    print("VYOM: Speak to me. Say 'exit' to stop.\n")

    while True:

        user_input = listen()

        if not user_input:
            continue

        print("You:", user_input)

        if user_input.lower() in [
            "exit",
            "quit",
            "bye",
            "goodbye"
        ]:
            print("VYOM: Goodbye!")
            break

        try:

            response = ask_vyom(user_input)

            print("\nVYOM:", response)
            print()

        except Exception as error:

            print("\nVYOM: Something went wrong.")
            print("Error:", error)


if __name__ == "__main__":
    main()