# main.py
import analytics  # Make sure this file exists in your repo

# 1. Add 15% to each price
def process_expenses(rawPrices):
    # Use analytics function to add percentage
    # Example: analytics.add_percentage(prices, pct)
    return analytics.add_percentage(rawPrices, 15)


# 2. Ask for n scores, return highest and average
def analyze_scores(n):
    scores = []
    for i in range(n):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)

    highest = analytics.find_max(scores)       # use analytics max function
    average = analytics.calculate_average(scores)  # use analytics average function
    return highest, average


# 3. Sanitize list of usernames
def sanitize_usernames(usernames):
    # Use analytics sanitize function
    # Example: analytics.clean_strings(list_of_strings)
    return analytics.clean_strings(usernames)


# 4. Return values over 100
def identify_outliers(values):
    # Use analytics filter function
    # Example: analytics.filter_greater_than(values, 100)
    return analytics.filter_greater_than(values, 100)


# 5. Search and report
def search_and_report(items):
    cleaned = analytics.clean_strings(items)  # sanitize first
    search_item = input("Enter item to search for: ").strip().lower()

    if analytics.is_sorted(cleaned):           # check if list is sorted
        return analytics.binary_search(cleaned, search_item)
    else:
        return analytics.linear_search(cleaned, search_item)