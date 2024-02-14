import re
import dns.resolver  # Make sure to install the 'dnspython' library using pip

def is_valid_email(email):
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
