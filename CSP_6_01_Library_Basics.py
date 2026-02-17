import analytics


def process_expenses(rawPrices):
    return [analytics.apply_markup(price, 0.15) for price in rawPrices]


def analyze_scores(n):
    scores = []
    for i in range(n):
        score = float(input(f"Enter score {i+1}: "))
        scores.append(score)
    highest = analytics.get_highest(scores)
    average = analytics.get_average(scores)
    return highest, average


def sanitize_usernames(usernames):
    return analytics.clean_text(usernames)


def identify_outliers(numbers):
    return analytics.filter_threshold(numbers, 100)


def search_and_report(items):
    items_clean = analytics.clean_text(items)
    search_word = input("Enter word to search: ").strip().lower()
    if items_clean == sorted(items_clean):
        low, high = 0, len(items_clean) - 1
        while low <= high:
            mid = (low + high) // 2
            if items_clean[mid] == search_word:
                return mid
            elif items_clean[mid] < search_word:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    else:
        for i, item in enumerate(items_clean):
            if item == search_word:
                return i
        return -1