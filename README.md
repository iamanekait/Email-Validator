# Email Validator

This Python script `email_validator.py` provides a simple function to validate email addresses using regular expressions and DNS MX record lookup.

## Prerequisites
- Python 3.x
- `dnspython` library. You can install it via pip:
  ```
  pip install dnspython
  ```

## Usage

```python
import re
import dns.resolver

def is_valid_email(email):
    """
    Check if the given email address is valid.

    Parameters:
    - email (str): The email address to be validated.

    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    # Define the regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Use the re.match() function to check if the email matches the pattern
    match = re.match(pattern, email)
    
    if not match:
        return False  # If email format is invalid, return False
    
    # Extract domain from email address
    domain = email.split('@')[1]

    try:
        # Perform DNS MX record lookup to verify domain existence
        dns.resolver.query(domain, 'MX')
        return True  # If domain exists, return True
    except dns.resolver.NoAnswer:
        return False  # If no MX records found for domain, return False
    except dns.resolver.NXDOMAIN:
        return False  # If domain does not exist, return False

# Example usage
email_to_check = input("Enter an email address: ")

if is_valid_email(email_to_check):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
```

## How it works

1. The function `is_valid_email()` takes an email address as input.
2. It checks the email format using a regular expression pattern.
3. If the format is valid, it extracts the domain from the email address.
4. It performs a DNS MX record lookup to verify the existence of the domain.
5. If the domain exists and has MX records, the function returns `True`, indicating a valid email address; otherwise, it returns `False`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
