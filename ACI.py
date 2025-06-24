# Advanced Compound Interest Calculator
# Formula: A = P * (1 + r/(100*n)) ** (n*t)

def compound_interest():
    try:
        principal = float(input("Enter principal amount (P): "))
        rate = float(input("Enter annual interest rate (r in %): "))
        time = float(input("Enter time in years (t): "))
        
        print("\nCompounding frequency:")
        print("1. Annually")
        print("2. Semi-Annually")
        print("3. Quarterly")
        print("4. Monthly")
        print("5. Daily")

        choice = int(input("Choose option (1–5): "))
        frequency_map = {1: 1, 2: 2, 3: 4, 4: 12, 5: 365}
        n = frequency_map.get(choice, 1)

        if choice not in frequency_map:
            print("Invalid choice! Defaulting to annual compounding.")

        amount = principal * (1 + rate / (100 * n)) ** (n * time)
        print(f"\nCompound amount after {time} years: {amount:.2f}")

    except ValueError:
        print("\nInvalid input! Please enter valid numbers.")

if __name__ == "__main__":
    compound_interest()