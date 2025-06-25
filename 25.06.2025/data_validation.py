# Filename:  data_validation.py
def validate_email(email):
    if "@" not in email or "." not in email.split("@")[1]:
        return False
    return True

def validate_phone(phone):
    return len(phone) == 10 and phone.isdigit()

email = "test@example.com"
phone = "1234567890"

print(f"Email '{email}' is valid: {validate_email(email)}")
print(f"Phone '{phone}' is valid: {validate_phone(phone)}")