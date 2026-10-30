from datetime import datetime
from domain import (
    create_offer,
    get_offer_destination,
    get_offer_start_date,
    get_offer_end_date,
    get_offer_price,
    set_offer_price,
    validate_offer
)


def compute_offers_in_time_interval(list_offers, start_date, end_date):
    """
    The function creates a list with all the offers that are included in a given time interval
    :param list_offers: List of offer entities
    :type list_offers: list
    :param start_date: Starting date of vacation

    :type start_date: str
    :param end_date: Ending date of vacation
    :type end_date: str
    :return: offers_in_time_interval
    :rtype: list
    """
    offers_in_time_interval = []
    interval_start = datetime.strptime(start_date, "%d.%m.%Y")
    interval_end = datetime.strptime(end_date, "%d.%m.%Y")

    for offer in list_offers:
        offer_start = datetime.strptime(get_offer_start_date(offer), "%d.%m.%Y")
        offer_end = datetime.strptime(get_offer_end_date(offer), "%d.%m.%Y")
        if offer_start >= interval_start and offer_end <= interval_end:
            offers_in_time_interval.append(offer)
    return offers_in_time_interval


def compute_offers_for_destination(list_offers):
    """
    The function returns a dictionary with the frequency of every destination
    :param list_offers: List with offers
    :type list_offers: list
    :return: destination_counts
    :rtype: dict
    """
    destination_counts = {}
    for offer in list_offers:
        dest = get_offer_destination(offer)
        if dest in destination_counts:
            destination_counts[dest] += 1
        else:
            destination_counts[dest] = 1
    return destination_counts


def compute_offer_enddate(list_offers, end_date):
    """
    The function creates a list with all the vacation offers which have
    the end date equal with the given end date
    :param list_offers: List of offer entities
    :type list_offers: list
    :param end_date: end date of vacation
    :type end_date: str
    :return: offers_by_end_date
    :rtype: list
    """
    offers_by_end_date = []
    for offer in list_offers:
        if get_offer_end_date(offer) == end_date:
            offers_by_end_date.append(offer)
    return offers_by_end_date


def compute_offers_cheaper(list_offers, destination, price):
    """
    The function creates a list with all the offers that have the destination equal with
    the given destination and with the price less than the given price
    :param list_offers: List of offer entities
    :type list_offers: list
    :param destination: target destination
    :type destination: str
    :param price: maximum price threshold
    :type price: float
    :return: offers_cheaper
    :rtype: list
    """
    offers_cheaper = []
    for offer in list_offers:
        if get_offer_destination(offer) == destination and get_offer_price(offer) < price:
            offers_cheaper.append(offer)
    return offers_cheaper


def average_price_for_destination(list_offers, destination):
    """
    Compute the average price for all offers which have a specific destination
    :param list_offers: List of offers
    :type list_offers: list
    :param destination: destination given by user
    :type destination: str
    :return: total_price/count_offers or -1 if no offers found
    :rtype: float
    """
    count_offers = 0
    total_price = 0
    for offer in list_offers:
        if get_offer_destination(offer) == destination:
            count_offers += 1
            total_price += get_offer_price(offer)
    if count_offers != 0:
        return total_price / count_offers
    else:
        return -1


def chose_2_best_offers_in_an_interval(list_offers, start_date, end_date):
    """
    Choose the 2 cheapest offers in an interval of time
    :param list_offers: List of offers
    :type list_offers: list
    :param start_date: The start date of vacation
    :type start_date: str (format DD.MM.YYYY)
    :param end_date: The end date of vacation
    :type end_date: str (format DD.MM.YYYY)
    :return: List of offers
    :rtype: list
    """
    offers_in_interval = compute_offers_in_time_interval(list_offers, start_date, end_date)
    offers_in_interval.sort(key=lambda offer1: get_offer_price(offer1))
    return offers_in_interval[:2]


def sort_list_by_destination(list_offers, substring):
    """
    Sort the list by destination for offers containing the given substring
    :param list_offers: List of offers
    :type list_offers: list
    :param substring: A substring given by user
    :type substring: str
    :return: A sorted list filtered by destination given by user
    :rtype: list
    """
    filtered_offers = []
    for offer in list_offers:
        if substring in get_offer_destination(offer):
            filtered_offers.append(offer)
    filtered_offers.sort(key=lambda offer1: get_offer_destination(offer1))
    return filtered_offers


def add_an_offer(list_offers, destination, start_date, end_date, price):
    """
    Create, validate, and add a new vacation offer in current list
    :param list_offers: List that contains the vacation offers
    :type list_offers: list
    :param destination: string, destination of vacation
    :type destination: str
    :param start_date: string (format DD.MM.YYYY)
    :type start_date: str
    :param end_date: string (format DD.MM.YYYY)
    :type end_date: str
    :param price: float, vacation price
    :type price: float
    :return: None (modifies the list in place)
    """
    vacation_offer = create_offer(destination, start_date, end_date, price)
    validate_offer(vacation_offer)
    list_offers.append(vacation_offer)


def modify_offer_price(list_offers, offer_index, offer_new_price):
    """
    Modify the price of an existing offer by index
    :param list_offers: List that contains the vacation offers
    :type list_offers: list
    :param offer_index: The index of offer that we want to modify
    :type offer_index: int
    :param offer_new_price: the new price for the offer
    :type offer_new_price: float
    :return: None (modifies the list in place)
    """
    if 0 <= offer_index < len(list_offers):
        if offer_new_price <= 0:
            raise ValueError("Price must be a positive number.")
        set_offer_price(list_offers[offer_index], offer_new_price)


def delete_all_offers_for_a_destination(list_offers, destination):
    """
    Delete from the list all the offers that have a certain destination
    :param list_offers: List that contains the offers of vacation
    :type list_offers: list
    :param destination: The destination for which the offers are deleted
    :type destination: str
    :return: None (modifies the list in place)
    """
    for i in range(len(list_offers) - 1, -1, -1):
        if get_offer_destination(list_offers[i]) == destination:
            list_offers.pop(i)


def remove_offers_with_shorter_duration_than_a_given_nr_of_days(list_offers, nr_of_days):
    """
    Erase from the list all the offers for which the duration is less than a given number of
    days. The duration is computed inclusive with the start and end date.
    :param list_offers: List that contains the offers
    :type list_offers: list
    :param nr_of_days: the minimum number of days accepted
    :type nr_of_days: int
    :return: None
    """
    for i in range(len(list_offers) - 1, -1, -1):
        start_date_str = get_offer_start_date(list_offers[i])
        end_date_str = get_offer_end_date(list_offers[i])
        start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
        end_date = datetime.strptime(end_date_str, "%d.%m.%Y")
        if (end_date - start_date).days + 1 < nr_of_days:
            list_offers.pop(i)


def remove_all_offers_for_which_the_price_is_greater_than_a_given_price(list_offers, last_price):
    """
    Erase from the list all the offers that have a price greater than a given price
    :param list_offers: List that contains the vacation offers
    :type list_offers: list
    :param last_price: The maximum price admitted
    :type last_price: float
    :return: None (modifies the list in place)
    """
    for i in range(len(list_offers) - 1, -1, -1):
        if get_offer_price(list_offers[i]) > last_price:
            list_offers.pop(i)


def populate_with_dummy_data(list_offers):
    """
    Populate the list with test data to verify the menu
    :param list_offers: The empty list, where we will put the data
    :type list_offers: list
    :return: None
    """
    add_an_offer(list_offers, "Paris", "10.08.2026", "15.08.2026", 1000.0)
    add_an_offer(list_offers, "Roma", "12.08.2026", "17.08.2026", 800.0)
    add_an_offer(list_offers, "Sophia", "19.08.2026", "20.08.2026", 500.0)
    add_an_offer(list_offers, "Paris", "01.09.2026", "10.09.2026", 1200.0)
    add_an_offer(list_offers, "Madrid", "11.08.2026", "20.08.2026", 4435.25)