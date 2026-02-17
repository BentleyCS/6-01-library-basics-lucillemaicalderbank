#Please modify the below functions so they fulfill the described process.
#You must use a function from analytics.py in each question to receive credit.
#There is no provided test file. You must make and submit one yourself. (check older test files for reference)

def process_expenses(rawPrices):
    updated_prices = []
    for price in rawPrices:
        updated_prices.append(price * 1.15)
    return updated_prices


# Modify the below function such that it asks the user for n scores
# and then returns the highest score and the average score of the list.
def analyze_scores(n):
    scores = []
    for i in range(n):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    highest = max(scores)
    average = sum(scores) / len(scores)

    return highest, average


# Modify the below function such that it takes in a list of strings
# and returns that list with all spaces removed and all letters lower case.
def sanitize_usernames(usernames):
    cleaned = []
    for name in usernames:
        cleaned.append(name.replace(" ", "").lower())
    return cleaned


# Modify the list such that it takes in a list as an argument
# and returns a version of the list with all values over 100.
def identify_outliers(values):
    return [value for value in values if value > 100]


# Modify the below function such that it takes in a list of items
# and asks the user for an item to search for.
# Sanitize the list to only be lower case words with no extra spaces
# Then return the location of the word using binary search if the list is in order
# and linear search if it is not.
def search_and_report(items):
    # Sanitize list
    cleaned = [item.strip().lower() for item in items]

    search_item = input("Enter item to search for: ").strip().lower()

    # Check if list is sorted
    if cleaned == sorted(cleaned):
        # Binary Search
        left = 0
        right = len(cleaned) - 1

        while left <= right:
            mid = (left + right) // 2
            if cleaned[mid] == search_item:
                return mid
            elif cleaned[mid] < search_item:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    else:
        # Linear Search
        for index, item in enumerate(cleaned):
            if item == search_item:
                return index
        return -1