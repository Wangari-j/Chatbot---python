print("Welcome to Safaricom shop!")

userName = input("Kindly let us know your name: ")
print("Hello " + userName + ". Kindly respond with a number to select any options below:")

while True:
    options = ["Products", "Services", "Subscriptions", "EXit"]


    for (i, option) in enumerate(options, start=1):
        print(f"{i}. {option}")

    products_InStock = [
        "Mobile phones",
        "Laptops",
        "Accessories",
    ]

    product_info = [
        "Stay connected, stay stylish! Find the latest collection of our mobile phones. Available brands are: Samsung, Tecno, Huawei and iPhone. To buy from our websites use this link: www.safaricomphones.co.ke",
        "Whether You're a Gamer, Professional or Student, Find Your Perfect Companion Here!Top brands available now are: Dell, HP,Lenovo, Asus and many more. Visit www.safaricomshop.co.ke to purchase the latest.",
        "Get yourself the latest essential accessories to compliment your devices. From headsets, smartwatches, power banks, tripods, phone cases and many more. Buy from our website here: www.safaricomshop.co.ke"
    ]

    services = [
        "Airtime",
        "Data bundles",
        "SMS bundles",
    ]

    purchase_services = [
        "To purchase airtime, dial *144#",
        "To purchase data bundles, dial *544#",
        "To purchase SMS bundles, dial *188#",
    ]

    subscriptions = [
        "Music subscription: To subscribe to our monthly music subsriptions, dial *500*2# use code 'Muziki'",
        "Messages subscription: To subscribe to inspiration and motivation messages by dialling *500*4# and use 'Ujumbe' as your code.",
        "Games subscription: To subscribe to games, dial *500*6# and use 'Michezo' as your code."
    ]

    choice = int(input("Enter a number: "))

    if choice == 1:
        print("We have a wide range of products to choose from at the best rates. Such as:")
        for (i, info) in enumerate(products_InStock, start=1):
            print(f"{i}. {info}")

        example_of_products = int(input("Enter a number: "))
        if 1 <= example_of_products <= len(product_info):
            print(product_info[example_of_products - 1])
        else:
            print("Invalid product number.")

    elif choice == 2:
        print("Enter the service that you would like to purchase:")
        for (i, service) in enumerate(services, start=1):
            print(f"{i}. {service}")
        service_choice = int(input("Enter a number: "))
        if 1 <= service_choice <= len(purchase_services):
            print(purchase_services[service_choice - 1])
        else:
            print("Invalid service number.")

    elif choice == 3:
        print("Subscriptions available:")
        for subscription in subscriptions:
            print(subscription)

    elif choice == 4:
        print("Have a great one " + userName + " and if you need more help you're always welcome right here.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
