wallet = 0
seats_alloted = 120
seat_price = 20

def book_seats(seats_alloted, seats_chosen):
    if seats_chosen <= 0:
        print("Not a valid selection of seats.")
        return seats_alloted, False
    if seats_chosen <= seats_alloted:
        print(f'You have selected {seats_chosen} seat(s).')
        seats_alloted -= seats_chosen
        return seats_alloted, True
    else:
        print('Not enough seats available.')
        return seats_alloted, False

def calculate_total_price(seats_chosen, tax_rate=0.18):
    base_price = seat_price * seats_chosen
    if base_price < 500:
        tax_rate = 0.12
    elif 500 < base_price:
        tax_rate = 0.18

    tax_payable = tax_rate * base_price
    total_price = base_price + tax_payable
    print('--------------------------------------------------------------------')
    print(f'\nSubtotal        : ₹{base_price:.2f}')
    print(f'Tax @{tax_rate*100:.0f}%     : ₹{tax_payable:.2f}')
    print(f'Total to Pay    : ₹{total_price:.2f}\n')
    print('--------------------------------------------------------------------')
    return total_price

def payment_interface(wallet, total_price):
    while wallet < total_price:

        print(f'❌ Not enough money in wallet. Balance: ₹{wallet:.2f}, Required: ₹{total_price:.2f}')
        print("1. Add money")
        print("2. Show wallet balance")
        print("3. Cancel booking")
        print('\n================================================================\n')

        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                amount = float(input("Enter amount to add: ₹"))
                if amount > 0:
                    wallet += amount
                    print(f"✅ ₹{amount:.2f} added to wallet. New balance: ₹{wallet:.2f}")
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            print(f"💰 Wallet balance: ₹{wallet:.2f}")
        elif choice == '3':
            print("❌ Booking cancelled.")
            return wallet, False
        else:
            print("Invalid choice.")
    wallet -= total_price
    print(f"✅ Payment of ₹{total_price:.2f} successful. Remaining wallet balance: ₹{wallet:.2f}")
    return wallet, True

# Main program loop
is_running = True

while is_running:
    try:
        print('==================================================================')
        print(f"\n        🪑 Seats Available: {seats_alloted}                    ")
        print(f"         💰 Wallet Balance: ₹{wallet:.2f}                        ")
        print("\n===================================================================")
        seats_chosen = int(input("Enter number of seats to book (or 0 to quit):   "))

        if seats_chosen == 0:
            print('================================================================')
            print("               👋 Exiting the program.                          ")
            print('                    Thank You                                    ')
            break

        seats_alloted, booking_successful = book_seats(seats_alloted, seats_chosen)

        if booking_successful:
            confirm = input("To confirm the selection, press (y) or press (q) to quit: ").lower()
            if confirm == 'y':
                total_price = calculate_total_price(seats_chosen)
                wallet, payment_successful = payment_interface(wallet, total_price)
                if payment_successful:
                    print("🎟️ Booking confirmed!")
                else:
                    # Refund seats
                    seats_alloted += seats_chosen
            elif confirm == 'q':
                print("👋 Exiting the program.")
                is_running = False
        else:
            continue

    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
