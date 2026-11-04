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
    remove_all_offers_for_which_the_price_is_greater_than_a_given_price,
    eliminate_offers_price_nb_days,
    eliminate_offers_by_destinations_list
)
from domain import to_str_offer
from manager import get_offers, get_undo_list, undo, copy_list_of_lists


def _apply_with_undo(manager, list_offers, operation, *args):
    previous_state = copy_list_of_lists(list_offers)
    result = operation(list_offers, *args)
    if list_offers != previous_state:
        get_undo_list(manager).append(previous_state)
    return result


def undo_ui(manager):
    """
    User interface for undo operation
    :param manager: dictionary containing offers and undo_list
    :return: None
    """
    try:
        undo(manager)
        print("Last operation done successfully")
        print_list_of_offers(get_offers(manager))
    except ValueError as error:
        print(f"Error: {error}")
def read_price_and_number_of_days(list_offers, manager=None):
    giv_price = read_float("Enter the price: ")
    days = read_int("Enter the number of days for the offer: ")
    if manager is None:
        eliminate_offers_price_nb_days(list_offers, giv_price, days)
    else:
        _apply_with_undo(manager, list_offers, eliminate_offers_price_nb_days, giv_price, days)

def read_list_of_destinations(list_offers, manager=None):
    """
    Deal with the list of destinations which is input by the user
    :return: destinations
    :rtype: list
    """
    destinations = []
    print("Write the destinations you want to pass, when you finish pres enter for 2 times!")
    while True:
        dest = input("Destination: ").strip()
        if not dest:
            break
        destinations.append(dest)
    if manager is None:
        eliminate_offers_by_destinations_list(list_offers, destinations)
    else:
        _apply_with_undo(manager, list_offers, eliminate_offers_by_destinations_list, destinations)

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

def read_offer_details():
    """
    Read and return the details of the offer: destination, start_date, end_date, price.
    :return: (destination, start_date, end_date, price)
    :rtype: tuple
    """
    destination = input("Enter the destination address: ").strip()
    start_date = input("Enter the start date (DD.MM.YYYY): ").strip()
    end_date = input("Enter the end date (DD.MM.YYYY): ").strip()
    price = read_float("Enter the price: ")
    return destination, start_date, end_date, price


def add_offer_ui(list_offers, manager=None):
    """
    Read offer details from the user and add the validated offer to the list.
    """
    destination, start_date, end_date, price = read_offer_details()
    try:
        if manager is None:
            add_an_offer(list_offers, destination, start_date, end_date, price)
        else:
            _apply_with_undo(
                manager, list_offers, add_an_offer, destination, start_date, end_date, price
            )
        print("Offers added successfully")
        print_list_of_offers(list_offers)
    except ValueError as error:
        print(f"Error: {error}")


def read_given_destination_and_price(list_offers):
    destination = input("Enter the destination: ").strip()
    price = read_float("Enter the price you want: ")
    offers_cheaper = compute_offers_cheaper(list_offers, destination, price)

    if len(offers_cheaper) == 0:
        print("There are no offers that match the expectations!")
    else:
        print("Matching offers:")
        for offer in offers_cheaper:
            print(to_str_offer(offer))

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
    average_price = average_price_for_destination(list_offers, destination)
    if average_price == -1:
        print("You typed a destination for which there are no offers!")
    else:
        print(f"The average price for offers to {destination} is = {average_price}")

def print_the_number_of_offers_available_for_each_destination(list_offers):
    destination_counts = compute_offers_for_destination(list_offers)
    print("Number of offers available for each destination: ", destination_counts)

def read_given_substring(list_offers):
    substring = input("Enter the substring: ").strip()
    print_list_of_offers(sort_list_by_destination(list_offers, substring))


def read_given_interval(list_offers):
    start_date = input("Enter the start date (DD.MM.YYYY): ").strip()
    end_date = input("Enter the end date (DD.MM.YYYY): ").strip()
    try:
        print_list_of_offers(chose_2_best_offers_in_an_interval(list_offers, start_date, end_date))
    except ValueError:
        print("Error: Dates must be in the format DD.MM.YYYY (e.g. 18.08.2026)!")

def print_menu_5():
    print("\n")
    print("1. Eliminate offers that have as destination one of those you include.")
    print("2. Eliminate offers for which the price is greater than a given price, and the number of days the offer spans is smaller than a given number.")
    print("\n")

def handle_menu_5(list_offers, manager=None):
    x = read_int("Choose an option from above: ")
    if x == 1:
        read_list_of_destinations(list_offers, manager)
    elif x == 2:
        read_price_and_number_of_days(list_offers, manager)

def print_menu_4():
    print("\n")
    print("1. Display the average price of offers for a given destination")
    print("2. Display the number of offers available for each destination")
    print("3. Display the offers for which the destination string contains a given substring, sorted in alphabetic order based on destination.")
    print("4. Display the two best offers for a given interval (see 3.a. for example of interval) in terms of price.")
    print("\n")

def handle_menu_4(list_offers):
    x = read_int("Choose an option from above: ")
    if x == 1:
        read_given_destination(list_offers)
    elif x == 2:
        print_the_number_of_offers_available_for_each_destination(list_offers)
    elif x == 3:
        read_given_substring(list_offers)
    elif x == 4:
        read_given_interval(list_offers)

def print_menu_3():
    print("\n")
    print("1. Display all offers which take place in a given interval of time")
    print("2. Display all offers with a given destination and having a price smaller than a given price")
    print("3. Display all offers with a given end date")
    print("\n")

def handle_menu_3(list_offers):
    x = read_int("Choose an option from above: ")
    if x == 1:
        read_start_end_date_for_printing_offers_in_that_interval(list_offers)
    elif x == 2:
        read_given_destination_and_price(list_offers)
    elif x == 3:
        read_given_end_date(list_offers)


def print_list_of_offers(list_offers):
    """
    Print all the offers
    :param list_offers: list that contain the offers
    :return: None
    """
    for index, offer in enumerate(list_offers):
        print(f"{index}. {to_str_offer(offer)}")


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


def handle_menu_2(list_offers, manager=None):
    user_option_2 = read_int("Choose an option from above: ")
    if user_option_2 == 1:
        destination = input("Enter the destination address: ").strip()
        if manager is None:
            delete_all_offers_for_a_destination(list_offers, destination)
        else:
            _apply_with_undo(manager, list_offers, delete_all_offers_for_a_destination, destination)
    elif user_option_2 == 2:
        nr_of_days = read_int("Enter the number of days: ")
        if manager is None:
            remove_offers_with_shorter_duration_than_a_given_nr_of_days(list_offers, nr_of_days)
        else:
            _apply_with_undo(
                manager, list_offers, remove_offers_with_shorter_duration_than_a_given_nr_of_days,
                nr_of_days
            )
    elif user_option_2 == 3:
        price = read_float("Enter the least acceptable price for the offer: ")
        if manager is None:
            remove_all_offers_for_which_the_price_is_greater_than_a_given_price(list_offers, price)
        else:
            _apply_with_undo(
                manager, list_offers,
                remove_all_offers_for_which_the_price_is_greater_than_a_given_price, price
            )


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


def handle_menu_1(list_offers, manager=None):
    user_option_2 = read_int("Choose an option from above: ")
    if user_option_2 == 1:
        add_offer_ui(list_offers, manager)
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
            if manager is None:
                modify_offer_price(list_offers, index, price)
            else:
                _apply_with_undo(manager, list_offers, modify_offer_price, index, price)
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
    7. Display the current offers
    8. Exit
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
        print_list_of_offers(offers)
    except ValueError:
        print("Error: Dates must be in the format DD.MM.YYYY (e.g. 27.10.2026)!")


def read_start_end_date_for_printing_offers_in_that_interval(list_offers):
    start_date = input("Enter the start date for printing offers (e.g. 27.10.2026): ").strip()
    end_date = input("Enter the end date for printing offers (e.g. 27.10.2026): ").strip()
    print_all_offers_which_take_place_in_a_given_interval_of_time(list_offers, start_date, end_date)


def start_ui(manager):
    while True:
        list_offers = get_offers(manager)
        print_menu_0_main()
        user_option = read_int("Choose an option from above: ")
        if user_option == 1:
            print_menu_1()
            handle_menu_1(list_offers, manager)
        elif user_option == 2:
            print_menu_2()
            handle_menu_2(list_offers, manager)
        elif user_option == 3:
            print_menu_3()
            handle_menu_3(list_offers)
        elif user_option == 4:
            print_menu_4()
            handle_menu_4(list_offers)
        elif user_option == 5:
            print_menu_5()
            handle_menu_5(list_offers, manager)
        elif user_option == 6:
            undo_ui(manager)
        elif user_option == 7:
            print_list_of_offers(list_offers)
        elif user_option == 8:
            print("Exiting application...")
            break