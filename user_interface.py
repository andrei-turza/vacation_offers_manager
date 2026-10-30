from domain import get_offer_destination
from list_offers import (
    add_an_offer,
    modify_offer_price,
    sort_list_by_destination,
    chose_2_best_offers_in_an_interval,
    average_price_for_destination,
    compute_offers_cheaper,
    compute_offer_enddate,
    compute_offers_for_destination,
    compute_offers_in_time_interval,
    delete_all_offers_for_a_destination,
    remove_offers_with_shorter_duration_than_a_given_nr_of_days,
    remove_all_offers_for_which_the_price_is_greater_than_a_given_price
)


def read_int(prompt):
    """
    Read an integer from the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer, (e.g. 12)!")


def read_float(prompt):
    """
    Read a float from the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Price must be a number.")


def read_user_option():
    x = read_int("Enter the option you want: ")
    return x


def read_offer_details():
    """
    Read and return the details of the offer: destination, start_date, end_date, price.
    :return: (destination, start_date, end_date, price)
    :rtype: tuple
    """
    destination = input("Enter the destination address: ").strip()
    start_date = input("Enter the start date (DD.MM.YYYY): ").strip()
    end_date = input("Enter the end date (DD.MM.YYYY): ").strip()
    while True:
        try:
            price = float(input("Enter the price: "))
            break
        except ValueError:
            print("Price must be a number.")
    return destination, start_date, end_date, price


def add_offer_ui(list_offers):
    """
    Read offer details from the user and add the validated offer to the list.
    """
    destination, start_date, end_date, price = read_offer_details()
    try:
        add_an_offer(list_offers, destination, start_date, end_date, price)
        print("Offers added successfully")
        print_list_of_offers(list_offers)
    except ValueError as error:
        print(f"Error: {error}")


def read_given_destination_and_price(list_offers):
    destination = input("Enter the destination: ").strip()
    price = read_float("Enter the price you want: ")
    offers_cheaper = compute_offers_cheaper(list_offers, destination, price)
    for offer in offers_cheaper:
        print(offer)
    if len(offers_cheaper) == 0:
        print("There are no offers that match the expectations!")


def read_given_end_date(list_offers):
    end_date = input("Enter the end date for display offer (DD.MM.YYYY): ").strip()
    offers_by_end_date = compute_offer_enddate(list_offers, end_date)
    if len(offers_by_end_date) != 0:
        print(f"The offers with end date {end_date} are:")
        for offer in offers_by_end_date:
            print(offer)
    else:
        print("There are no offers that match the expectation!")


def read_given_destination(list_offers):
    destination = input("Enter the destination: ").strip()
    while destination not in (get_offer_destination(offer) for offer in list_offers):
        print("There is no such destination!")
        destination = input("Enter the destination: ").strip()
    average_price = average_price_for_destination(list_offers, destination)
    if average_price == -1:
        print("You typed a destination for which are no offers")
    else:
        print(f"The average price for offers to {destination} is =", average_price)


def print_the_number_of_offers_available_for_each_destination(list_offers):
    destination_counts = compute_offers_for_destination(list_offers)
    print("Number of offers available for each destination: ", destination_counts)

def read_given_substring(list_offers):
    substring = input("Enter the substring: ").strip()
    print(sort_list_by_destination(list_offers, substring))


def read_given_interval(list_offers):
    start_date = input("Enter the start date (DD.MM.YYYY): ").strip()
    end_date = input("Enter the end date (DD.MM.YYYY): ").strip()
    try:
        print(chose_2_best_offers_in_an_interval(list_offers, start_date, end_date))
    except ValueError:
        print("Error: Dates must be in the format DD.MM.YYYY (e.g. 18.08.2026)!")


def print_menu_3():
    print("\n")
    print("1. Display all offers which take place in a given interval of time")
    print("2. Display all offers with a given destination and having a price smaller than a given price")
    print("3. Display all offers with a given end date")
    print("4. Display the average price of offers for a given destination")
    print("5. Display the number of offers available for each destination")
    print("6. Display the offers for which the destination string contains a given substring, sorted in alphabetic order based on destination.")
    print("7. Display the two best offers for a given interval (see 3.a. for example of interval) in terms of price.")
    print("\n")


def handle_menu_3(list_offers):
    x = read_int("Choose an option from above: ")
    if x == 1:
        read_start_end_date_for_printing_offers_in_that_interval(list_offers)
    elif x == 2:
        read_given_destination_and_price(list_offers)
    elif x == 3:
        read_given_end_date(list_offers)
    elif x == 4:
        read_given_destination(list_offers)
    elif x == 5:
        print_the_number_of_offers_available_for_each_destination(list_offers)
    elif x == 6:
        read_given_substring(list_offers)
    elif x == 7:
        read_given_interval(list_offers)


def print_list_of_offers(list_offers):
    """
    Print all the offers
    :param list_offers: list that contain the offers
    :return: None
    """
    index = 0
    for i in list_offers:
        print(index, i)
        index += 1


def print_menu_2():
    """
    Displays the menu after the user select option 2
    1. Delete all available offers for a given destination
    2. Remove all offers that have a shorter duration than a given number of days
    3. Remove all offers for which the price is greater than a given price
    :return: None
    """
    print("\n")
    print("1. Delete all available offers for a given destination")
    print("2. Remove all offers that have a shorter duration than a given number of days")
    print("3. Remove all offers for which the price is greater than a given price")
    print("\n")


def handle_menu_2(list_offers):
    user_option_2 = read_int("Choose an option from above: ")
    if user_option_2 == 1:
        destination = input("Enter the destination address: ").strip()
        delete_all_offers_for_a_destination(list_offers, destination)
    elif user_option_2 == 2:
        nr_of_days = read_int("Enter the number of days: ")
        remove_offers_with_shorter_duration_than_a_given_nr_of_days(list_offers, nr_of_days)
    elif user_option_2 == 3:
        price = read_float("Enter the least acceptable price for the offer: ")
        remove_all_offers_for_which_the_price_is_greater_than_a_given_price(list_offers, price)


def print_menu_1():
    """
    Displays the menu after the user select option 1
    1. Add an offer
    2. Modify an offer price
    :return: None
    """
    print("\n")
    print("1. Add an offer")
    print("2. Modify an offer price")
    print("\n")


def handle_menu_1(list_offers):
    user_option_2 = read_int("Choose an option from above: ")
    if user_option_2 == 1:
        add_offer_ui(list_offers)
    elif user_option_2 == 2:
        if len(list_offers) == 0:
            print("There are no offers in the list to modify!")
            return
        print_list_of_offers(list_offers)
        while True:
            index = read_int("Enter the index of the offer: ")
            if 0 <= index < len(list_offers):
                break
            print(f"Error: Invalid index! Please choose a number between 0 and {len(list_offers) - 1}.")
        price = read_float("Enter the new price for the offer: ")
        try:
            modify_offer_price(list_offers, index, price)
        except ValueError as error:
            print(f"Error: {error}")


def print_menu_0_main():
    """
    The function displays the menu for the user
    1. Add and modify an offer
    2. Remove offers
    3. Display offers with specific properties
    4. Reports
    5. Filtering
    6. Undo
    0. Exit
    :return: None
    """
    print("\n")
    print("1. Add and modify an offer")
    print("2. Remove offers")
    print("3. Display offers with specific properties")
    print("4. Reports")
    print("5. Filtering")
    print("6. Undo")
    print("7. Display the current offers")
    print("8. Exit")
    print("\n")


def print_all_offers_which_take_place_in_a_given_interval_of_time(list_offers, start_date, end_date):
    try:
        offers = compute_offers_in_time_interval(list_offers, start_date, end_date)
        print("Your destinations after filtering are:")
        print(offers)
    except ValueError:
        print("Error: Dates must be in the format DD.MM.YYYY (e.g. 27.10.2026)!")


def read_start_end_date_for_printing_offers_in_that_interval(list_offers):
    start_date = input("Enter the start date for printing offers (e.g. 27.10.2026): ").strip()
    end_date = input("Enter the end date for printing offers (e.g. 27.10.2026): ").strip()
    print_all_offers_which_take_place_in_a_given_interval_of_time(list_offers, start_date, end_date)


def start_ui(list_offers):
    image_poster()
    while True:
        print_menu_0_main()
        user_option = read_int("Choose an option from above: ")
        if user_option == 1:
            print_menu_1()
            handle_menu_1(list_offers)
        elif user_option == 2:
            print_menu_2()
            handle_menu_2(list_offers)
        elif user_option == 3:
            print_menu_3()
            handle_menu_3(list_offers)
        elif user_option == 7:
            print_list_of_offers(list_offers)
        elif user_option == 8:
            print("Exiting application...")
            break

def image_poster():
    t = '''
    [0;97;47m▓[0;94;47m▄▄[0;97;47m▓[0;37m   [0;97;47m▓[0;94;47m▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄▄[0;37m▄    ▄[0;94;47m▄▄▄▄▄▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄▄[0;37m▄  [0;97;47m▓[0;94;47m▄▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄▄[0;37m▄  [0;97;47m▓[0;94;47m▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;37m▄          [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄▄[0;37m▄  [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄▄▄[0;97;47m▓[0;37m [0;97;47m▓[0;94;47m▄▄▄▄▄▄▄[0;37m▄     ▄[0;94;47m▄▄▄▄▄▄▄▄[0;97;47m▓[0m
    [0;97;47m▒[0;94;47m▀▀[0;97;47m▒[0;37m   [0;97;47m▒[0;94m▓▓[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀▀▀▀▀[0;94m▓▓▓[0;97;47m▒[0;37m ▄[0;97;47m▒[0;94;47m▀▀▀▀▀▀▀▀[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀▀▀▀▀[0;94m▓▓▓[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀▀[0;97;47m▒[0;37m [0;97;47m▒[0;94m▓▓[0;94;47m▀▀▀▀▀[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀▀▀▀▀[0;94m▓▓▓[0;97;47m▓[0;37m [0;97;47m▒[0;94m▓▓[0;97;47m▒[0;37m [0;97;47m▒[0;94m▓[0;94;47m▄[0;37m▄        [0;97;47m▒[0;94;47m▀▀▀▀▀▀[0;94m▓▓▓[0;97;47m▓[0;37m [0;97;47m▒[0;94;47m▀▀▀▀▀▀▀▀▀[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀▀▀▀▀▀▀▀[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀▀▀▀▀▀▀▀[0;97;47m▒[0;37m [0;97;47m▒[0;94;47m▀▀▀▀▀[0;94m▓▓▓[0;94;47m▄[0;37m▄  [0;97;47m▒[0;94;47m▀▀▀▀▀▀▀▀▀[0;97;47m▒[0m
    [0;37m▄▄▄▄   [0;97;47m░[0;94m▒▒[0;97;47m░[0;37m ▄▄▄▄   [0;97;47m░[0;94m▒▒[0;97;47m░[0;37m ▄▄▄▄        ▄▄▄▄   [0;97;47m░[0;94m▒▒[0;97;47m░[0;37m       [0;97;47m░[0;94m▒▒[0;97;47m░[0;37m      ▄▄▄▄ ▄▄▄▄   [0;97;47m▒[0;94m▒▒[0;97;47m▒[0;37m [0;97;47m░[0;94m▒▒[0;97;47m░[0;37m ▀[0;94;47m▀[0;94m▒▒[0;94;47m▄[0;37m▄      ▄▄▄▄   [0;97;47m▒[0;94m▒▒[0;97;47m▒[0;37m ▄▄▄▄        ▄▄▄▄        ▄▄▄▄        ▄▄▄▄  ▀[0;94;47m▀[0;94m▒▒▒[0;97;47m░[0;37m ▄▄▄▄       [0m
    [0;97;47m░[0;94m░░[0;97;47m░[0;37m   █[0;94m░░[0;37m█ [0;97;47m░[0;94m░░[0;97;47m░[0;37m   █[0;94m░░[0;37m█ [0;97;47m░[0;94m░░[0;97;47m░[0;37m        [0;97;47m░[0;94m░░[0;97;47m░[0;37m   █[0;94m░░[0;37m█       █[0;94m░░[0;37m█      █[0;94m░░[0;37m█ [0;97;47m░[0;94m▓▓[0;97;47m░[0;37m   [0;97;47m░[0;94m░░[0;97;47m░[0;37m █[0;94m░░[0;37m█   [0;97;47m░[0;94m░░[0;97;47m░[0;37m      [0;97;47m░[0;94m▓▓[0;97;47m░[0;37m   [0;97;47m░[0;94m░░[0;97;47m░[0;37m █[0;94m░░[0;37m█ [0;97;47m░[0;94;47m▄▄[0;97;47m░[0;37m   █[0;94m░░[0;37m█ [0;97;47m░[0;94;47m▄▄[0;97;47m░[0;37m   █[0;94m▓▓[0;37m█ █[0;94;47m▄▄[0;37m█   [0;97;47m░[0;94m░░[0;97;47m░[0;37m   [0;97;47m░[0;94m░░[0;94;47m▀[0;37m▀ [0;97;47m░[0;94m▒▒[0;97;47m░[0;37m ▄▄▄▄▄ [0m
    [0;94;47m░[0;37m  [0;94;47m░[0;37m   [0;94;47m░[0;37m  [0;94;47m░[0;37m [0;94;47m▒[0;37m  [0;94;47m▒[0;37m ▄▄▀  [0;94;47m▒[0;37m [0;94;47m▒[0;37m  [0;94;47m▒[0;37m        [0;94;47m▒[0;37m  [0;94;47m▒[0;37m ▄▄▀  [0;94;47m▒[0;37m       [0;94;47m░[0;37m  [0;94;47m░[0;37m      [0;94;47m▒[0;37m  [0;94;47m▒[0;37m [0;94;47m▒[0;37m  [0;94;47m▒[0;37m   [0;94;47m▒[0;37m  [0;94;47m▒[0;37m [0;94;47m░[0;37m  [0;94;47m░[0;37m   [0;94;47m░[0;37m  [0;94;47m░[0;37m      [0;94;47m▒[0;37m  [0;94;47m▒[0;37m   [0;94;47m▒[0;37m  [0;94;47m▒[0;37m [0;94;47m▒[0;37m  [0;94;47m▒[0;37m █▄▄█   [0;94;47m▒[0;37m  [0;94;47m▒[0;37m █▄▄█   [0;94;47m▒[0;37m  [0;94;47m▒[0;37m [0;94;47m▒[0;37m▄▄[0;94;47m▒[0;37m   [0;94;47m░[0;37m  [0;94;47m░[0;37m ▄▀ ▄▀   ▀▄▄[0;94;47m▓[0;37m █▄▄  [0;94;47m▒[0m
    [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m   [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m [0;94m▀▀▄[0;34m░░[0;94;47m▓[0;37m [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m        [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m [0;94m▀▀▄[0;34m░░[0;94;47m▓[0;37m       [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m      [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m   [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m   [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m      [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m   [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m        [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m        [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m        [0;94;47m▓[0;34m░░[0;94;47m▓[0;37m ▀[0;94m▄[0;34m░░[0;94m▀▄[0;37m  [0;94m▄▄▄▄[0;37m [0;94m▀▀[0;94;47m▓[0;34m░░[0;94;47m▓[0m
    [0;94m█[0;34m▒▒[0;94;44m▀[0;94m▄[0;37m [0;94m▄[0;94;44m▀[0;34m▒▒[0;94m█[0;37m [0;94m█[0;34m▒▒[0;94m█[0;37m   [0;94m█[0;34m▒▒[0;94m█[0;37m [0;94m█[0;34m▒▒▒[0;94;44m▀[0;94m▄[0;37m      [0;94m█[0;34m▒▒[0;94m█[0;37m   [0;94m█[0;34m▒▒[0;94m█[0;37m       [0;94m█[0;34m▒▒[0;94m█[0;37m      [0;94m█[0;34m▒▒[0;94m█[0;37m [0;94m█[0;34m▒▒[0;94m█[0;37m   [0;94m█[0;34m▒▒[0;94m█[0;37m [0;94m█[0;34m▒▒[0;94m█[0;37m   [0;94m█[0;34m▒▒[0;94m█[0;37m      [0;94m█[0;34m▒▒[0;94m█[0;37m   [0;94m█[0;34m▒▒[0;94m█[0;37m [0;94m█[0;34m▒▒[0;94m█[0;37m        [0;94m█[0;34m▒▒[0;94m█[0;37m        [0;94m█[0;34m▒▒[0;94m█[0;37m        [0;94m█[0;34m▒▒[0;94m█[0;37m   [0;94m▀[0;94;44m▄[0;34m▒▒[0;94m█[0;37m [0;94m█[0;34m▒▒[0;94m█[0;37m   [0;94m█[0;34m▒▒[0;94m█[0m
    [0;94m▀[0;94;44m▄[0;34m▓▓▓[0;94;44m▀[0;34m▓▓▓[0;94;44m▄[0;94m▀[0;37m [0;94m█[0;34m▓▓[0;94m█[0;37m   [0;94m█[0;34m▓▓[0;94m█[0;37m  [0;94m▀[0;94;44m▄[0;34m▓▓▓[0;94;44m▀▀▀▀[0;94m█[0;37m [0;94m█[0;34m▓▓[0;94m█[0;37m   [0;94m█[0;34m▓▓[0;94m█[0;37m       [0;94m█[0;34m▓▓[0;94m█[0;37m      [0;94m█[0;34m▓▓[0;94m█[0;37m [0;94m█[0;34m▓▓▓[0;94;44m▀▀▀[0;34m▓▓▓[0;94m█[0;37m [0;94m█[0;34m▓▓[0;94m█[0;37m   [0;94m█[0;34m▓▓[0;94m█[0;37m      [0;94m█[0;34m▓▓▓[0;94;44m▀▀▀[0;34m▓▓▓[0;94m█[0;37m [0;94m█[0;34m▓▓[0;94m█[0;37m        [0;94m█[0;34m▓▓[0;94m█[0;37m        [0;94m█[0;34m▓▓[0;94;44m▀▀▀▀▀▀▀[0;94m█[0;37m [0;94m█[0;34m▓▓[0;94m█[0;37m    [0;94m█[0;34m▓▓[0;94m█[0;37m [0;94m█[0;34m▓▓[0;94;44m▀▀▀▀[0;34m▓▓▓[0;94m█[0m
    [0;37m  [0;90m▀[0;90;44m▄▄▄▄▄[0;90m▀[0;37m   [0;94m█[0;90;44m▄▄[0;94m█[0;37m   [0;94m█[0;90;44m▄▄[0;94m█[0;37m    [0;90m▀[0;90;44m▄▄▄▄▄▄[0;94m█[0;37m [0;94m█[0;90;44m▄▄[0;94m█[0;37m   [0;94m█[0;90;44m▄▄[0;94m█[0;37m       [0;94m█[0;90;44m▄▄[0;94m█[0;37m      [0;94m█[0;90;44m▄▄[0;94m█[0;37m  [0;90m▀[0;90;44m▄▄▄▄▄▄▄[0;90m▀[0;37m  [0;94m█[0;90;44m▄▄[0;94m█[0;37m   [0;94m█[0;90;44m▄▄[0;94m█[0;37m       [0;90m▀[0;90;44m▄▄▄▄▄▄▄[0;90m▀[0;37m  [0;94m█[0;90;44m▄▄[0;94m█[0;37m        [0;94m█[0;90;44m▄▄[0;94m█[0;37m        [0;94m█[0;90;44m▄▄▄▄▄▄▄▄▄[0;94m█[0;37m [0;94m█[0;90;44m▄▄[0;94m█[0;37m    [0;94m█[0;90;44m▄▄[0;94m█[0;37m  [0;90m▀[0;90;44m▄▄▄▄▄▄▄[0;90m▀[0;37m [0m
    '''
    print(t)
