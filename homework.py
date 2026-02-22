def search_and_report(items):
    # Use analytics to clean the list
    clean_items = analytics.clean_text(items)

    target = input("Enter item to search for: ").strip().lower()

    # Check if the list is already sorted manually
    is_ordered = True
    for i in range(len(clean_items) - 1):
        if clean_items[i] > clean_items[i + 1]:
            is_ordered = False
            break

    if is_ordered:
        # Binary Search
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
        # Linear Search
        for i in range(len(clean_items)):
            if clean_items[i] == target:
                return i

    return -1
