from Services.auth_service import auth_menu


if __name__ == "__main__":
    try:
        auth_menu()
    except KeyboardInterrupt:
        print("\n\nProgram stopped. Goodbye!")
