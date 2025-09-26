import json


def open_data(file) -> list:
    with open(file) as f:
        jdata = json.load(f)
    return jdata.get('data')


def search_by_date(data: list, target_date: str) -> list:
    
    results = []
    for entry in data:
        # print(entry[3])
        if target_date in entry[3]:
            results.append(entry)
    return results


def check_format(target_date: str) -> str:
    """Check if the date is in the correct format 'YYYY-MMM-DD'.\n
    If the month is in lowercase, convert it to capitalized form.\n
    If the format is incorrect, raise a ValueError.\n
    :param target_date: The date string to check.
    :return: The date string in the correct format."""
    import re
    
    pattern = r'^\d{4}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{2}$'
    lower_pattern = r'^\d{4}-(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)-\d{2}$'
    
    if re.match(pattern, target_date):
        return target_date
    
    elif re.match(lower_pattern, target_date):
        parts = target_date.split('-')
        parts[1] = parts[1].capitalize()
        return '-'.join(parts)

    else:
        raise ValueError("Date format is incorrect. " 
                         "Please use 'YYYY-MMM-DD' format. " 
                         "Example: '2023-Jan-15'")


if __name__ == '__main__':
    data = open_data('data/cad.json')
    date = check_format(input("Enter the date (YYYY-MM-DD): "))
    print(f"Entries matching date '{date}':")
    matched_entries = search_by_date(data, date)
    for entry in matched_entries:
        print(entry)