def convert_currency(amount, from_currency, to_currency, rates):
    # Check if the currencies are valid
    if from_currency not in rates or to_currency not in rates:
        return "Invalid currency code."
    
    # Convert amount to base currency (USD in this case)
    base_amount = amount / rates[from_currency]
    
    # Convert amount from base currency to the target currency
    converted_amount = base_amount * rates[to_currency]
    
    return converted_amount

def main():
    # Static exchange rates for demonstration (base currency is USD)
    rates = {
        'USD': 1.00,        # US Dollar
        'EUR': 0.93,        # Euro
        'GBP': 0.82,        # British Pound
        'JPY': 137.89,      # Japanese Yen
        'AUD': 1.47,        # Australian Dollar
        'CAD': 1.36         # Canadian Dollar
    }
    
    print("Welcome to the Currency Converter")
    print("Available currencies: USD, EUR, GBP, JPY, AUD, CAD")
    
    while True:
        from_currency = input("Enter the currency code to convert from (e.g., USD): ").upper()
        to_currency = input("Enter the currency code to convert to (e.g., EUR): ").upper()
        
        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue
        
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        if isinstance(converted_amount, str):
            print(converted_amount)
        else:
            print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            print("Thank you for using the Currency Converter. Goodbye!")
            break

if __name__ == "__main__":
    main()
