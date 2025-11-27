books = {
    "Book1": 5,
    "Book2": 6,
    "Book3": 10
}

book_name = input("Enter book name: ").strip()

while True:
    amount = input("Enter number of copies: ").strip()
    if amount.isdigit():
        amount = int(amount)
        break
    print("Invalid entry — please enter a number only.")

if book_name not in books:
    print("Unavailable")
else:
    available = books[book_name]
    if available >= amount:
        print("Available")
    elif 0 < available < amount:
        print("Partially Available")
    else:
        print("Unavailable")
