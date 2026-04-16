#Task 7: Mini project - Export discount prices
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

with open("discount_report.txt", "w") as f:
    total = 0
    count = 0

    for product, price in prices.items():
        discounted_price = price - (price * discount / 100)

        f.write(product + " | " + str(price) + " | " + str(discounted_price) + "\n")

        total += discounted_price
        count += 1

    # Optional summary
    avg = total / count
    f.write("\nTotal Items: " + str(count))
    f.write("\nAverage Discounted Price: " + str(avg))


# Read and print file
with open("discount_report.txt", "r") as f:
    for line in f:
        print(line.strip())