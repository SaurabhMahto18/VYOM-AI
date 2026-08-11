from core.brain import ask_vyom


def main():
    print("=" * 45)
    print("              VYOM AI")
    print("      Virtual Yielding Omni Mind")
    print("           Think. Learn. Act.")
    print("=" * 45)

    print("\nVYOM: Hello! I am VYOM.")
    print("VYOM: Type 'exit' to close.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("VYOM: Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = ask_vyom(user_input)
            print("\nVYOM:", response)
            print()

        except Exception as error:
            print("\nVYOM: Something went wrong.")
            print("Error:", error)


if __name__ == "__main__":
    main()