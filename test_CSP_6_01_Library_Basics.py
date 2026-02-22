from homework import *

def run_tests():
    print("--- 1. Testing process_expenses ---")
    # 100 + 15% = 115.0
    print(f"Prices [100, 200]: {process_expenses([100, 200])}")

    print("\n--- 3. Testing sanitize_usernames ---")
    names = ["  Admin", " guest ", "User123  "]
    print(f"Cleaned: {sanitize_usernames(names)}")

    print("\n--- 4. Testing identify_outliers ---")
    nums = [50, 101, 20, 500, 99]
    print(f"Outliers (>100): {identify_outliers(nums)}")

    print("\n--- 5. Testing search_and_report (Unsorted) ---")
    # This will prompt you for an input. Try 'apple'
    fruit = ["  Apple", "Banana ", "  CHERRY  ", " date "]
    print(f"Search Result Index: {search_and_report(fruit)}")

    print("\n--- 2. Testing analyze_scores ---")
    # This will prompt you for 3 scores
    high, avg = analyze_scores(3)
    print(f"Highest: {high}, Average: {avg}")

if __name__ == "__main__":
    run_tests()