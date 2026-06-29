import re

def extract_information(text: str) -> None:
    """Extracts and formats emails, phone numbers, and dates from raw text."""
    
    print("\n" + "━"*50)
    print(" 🕵️‍♂️ REGEX INFORMATION EXTRACTOR")
    print("━"*50)

    # 1. Extract Emails using re.findall()
    # Pattern: letters/numbers/symbols + @ + letters/numbers + . + domain(2+ chars)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    
    print(f"\n📧 EMAILS FOUND ({len(emails)}):")
    for email in emails:
        print(f"  • {email}")

    # 2. Extract Dates using re.findall()
    # Pattern: 2 digits + separator (-, /, .) + 2 digits + separator + 4 digits
    date_pattern = r'\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'
    dates = re.findall(date_pattern, text)
    
    print(f"\n📅 DATES FOUND ({len(dates)}):")
    for date in dates:
        print(f"  • {date}")

    # 3. Extract and Clean Phone Numbers using re.finditer() and re.sub()
    # Pattern: Optional country code, followed by various 10-digit formats
    phone_pattern = r'(\+\d{1,3}[-\s]?)?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}'
    
    # We use finditer to get match objects so we can process them individually
    phone_matches = list(re.finditer(phone_pattern, text))
    
    print(f"\n📱 PHONE NUMBERS ({len(phone_matches)}):")
    for match in phone_matches:
        raw_phone = match.group()
        # Optional Task: Clean the formatting using re.sub()
        # This removes all non-digit characters to standardize the output
        clean_digits = re.sub(r'\D', '', raw_phone)
        
        # Reformat into a standard (XXX) XXX-XXXX layout (assuming 10 digits for display)
        if len(clean_digits) >= 10:
            formatted_phone = f"({clean_digits[-10:-7]}) {clean_digits[-7:-4]}-{clean_digits[-4:]}"
            print(f"  • {formatted_phone} (Raw: {raw_phone})")
        else:
            print(f"  • {raw_phone}")

    print("\n" + "━"*50 + "\n")


def main():
    """Main CLI execution block."""
    sample_text = """
    Hello Team,
    Please review the logs for user ransh.engineer@sppu.edu. We also have a secondary 
    contact at support-team_99@domain.co.in. 
    
    The server migration started on 12/08/2026 and should conclude by 15-08-2026.
    If there are critical failures, contact the on-call dev at +91-9876543210 
    or the regional office at (555) 123-4567.
    """
    
    print("Processing Sample Text block...")
    extract_information(sample_text)

if __name__ == "__main__":
    main()