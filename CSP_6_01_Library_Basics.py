# main_functions.py
import analytics

# 1. Add 15% markup to each price in the list
def process_expenses(rawPrices):
    return [analytics.apply_markup(price, 0.15) for price in rawPrices]


# 2. Ask user for n scores, return highest and average
def analyze_scores(n):
    scores = []
    for i in range(n):
        while True:
            try:
                score = float(input(f"Enter score {i+1}: "))
                scores.append(score)
                break
            except ValueError:
                print("Please enter a valid number.")
    highest = analytics.get_highest(scores)
    average = analytics.get_average(scores)
    return highest, average


# 3. Sanitize a list of usernames: lowercase and no spaces
def sanitize_usernames(usernames):
    return analytics.clean_text(usernames)


# 4. Return list of numbers over 100
def identify_outliers(numbers):
    return analytics.filter_threshold(numbers, 100)


# 5. Search for an item in a list
def search_and_report(items):
    items = analytics.clean_text(items)
    search_item = input("Enter the item to search for: ").strip().lower()

    # Check if list is sorted
    is_sorted = all(items[i] <= items[i+1] for i in range(len(items)-1))

    # Binary search if sorted
    if is_sorted:
        left, right = 0, len(items)-1
        while left <= right:
            mid = (left + right) // 2
            if items[mid] == search_item:
                return mid
            elif items[mid] < search_item:
                left = mid + 1
            else:
                right = mid - 1
        return -1  # Not found

    # Linear search if not sorted
    for idx, item in enumerate(items):
        if item == search_item:
            return idx
    return -1  # Not found