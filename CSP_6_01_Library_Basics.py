import analytics


# 1. Returns list with 15% added value
def process_expenses(rawPrices):
    # Uses apply_markup from analytics
    return [analytics.apply_markup(p, 0.15) for p in rawPrices]


# 2. Asks for n scores, returns (highest, average)
def analyze_scores(n):
    scores = []
    for i in range(n):
        val = float(input(f"Enter score {i + 1}: "))
        scores.append(val)

    # Uses get_highest and get_average from analytics
    high = analytics.get_highest(scores)
    avg = analytics.get_average(scores)
    return high, avg


# 3. Removes spaces and lowercases strings
def sanitize_usernames(user_list):
    # Uses clean_text from analytics
    # Note: clean_text handles .strip() and .lower() as requested
    return analytics.clean_text(user_list)


# 4. Returns a version of the list with all values over 100
def identify_outliers(data):
    # Uses filter_threshold from analytics with a limit of 100
    return analytics.filter_threshold(data, 100)


# 5. Sanitizes, determines search type, and returns location
def search_and_report(items):
    # First, sanitize using analytics
    clean_items = analytics.clean_text(items)

    target = input("Enter item to search for: ").strip().lower()

    # Check if list is in order to decide search method
    # Since analytics.py doesn't have a sorter, we check order manually
    is_sorted = clean_items == sorted(clean_items)

    if is_sorted:
        # Binary Search implementation
        low, high = 0, len(clean_items) - 1
        while low <= high:
            mid = (low + high) // 2
            if clean_items[mid] == target:
                return mid
            elif clean_items[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    else:
        # Linear Search implementation
        for i in range(len(clean_items)):
            if clean_items[i] == target:
                return i

    return -1  # Return -1 if not found