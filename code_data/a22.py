import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    while True:
        email = input("Enter an email address to validate (or type 'exit' to quit): ")
        if email.lower() == 'exit':
            break
        if is_valid_email(email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")

if __name__ == "__main__":
    main()
