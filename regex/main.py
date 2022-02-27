import re


def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    try:
        phone_number = match.group()
    except AttributeError:
        return None
    else:
        return phone_number


def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.findall(input)
    return match


def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False


phones = extract_all_phones("my number is 432 567-8976 or call me at 345 666-6789")
for phone in phones:
    print(is_valid_phone(phone))
