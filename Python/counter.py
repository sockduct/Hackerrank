# Input:
# * First Line:  # of shoes
# * Second Line:  list of all shoe sizes
# * Third Line:  # of customers
# * Subsequent Lines:  shoe_size, price_of_shoe

def main():
    shoes: int = 0
    shoe_size: int = 0
    shoe_sizes: list[int] = []
    customers: int = 0
    price: int = 0  # Could be float
    revenue: int = 0  # Could be float

    shoes = int(input())
    shoe_sizes = [int(shoe_size) for shoe_size in input().split()]
    customers = int(input())

    for customer in range(customers):
        shoe_size, price = [int(item) for item in input().split()]

        if shoe_size in shoe_sizes:
            revenue += price
            shoe_sizes.remove(shoe_size)

    print(revenue)

if __name__ == '__main__':
    main()
