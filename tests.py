from domain import (
    create_offer,
    get_offer_destination,
    get_offer_start_date,
    get_offer_end_date,
    get_offer_price,
    set_offer_destination,
    set_offer_start_date,
    set_offer_end_date,
    set_offer_price,
    validate_offer
)

from list_offers import (
    add_an_offer,
    modify_offer_price,
    delete_all_offers_for_a_destination,
    remove_offers_with_shorter_duration_than_a_given_nr_of_days,
    remove_all_offers_for_which_the_price_is_greater_than_a_given_price,
    compute_offers_in_time_interval,
    compute_offers_for_destination,
    compute_offer_enddate,
    compute_offers_cheaper,
    average_price_for_destination,
    chose_2_best_offers_in_an_interval,
    sort_list_by_destination,
    eliminate_offers_by_destinations_list,
    eliminate_offers_price_nb_days,
    populate_with_dummy_data
)
from manager import (
    create_offer_manager,
    set_offers,
    copy_list_of_lists,
    add_offer,
    get_offers,
    undo,
    get_undo_list
)


def test_undo_after_add():
    manager = create_offer_manager()
    initial_offers = []
    populate_with_dummy_data(initial_offers)
    set_offers(manager, initial_offers)
    expected_offers = copy_list_of_lists(initial_offers)

    add_offer(manager, "USA", "10.10.2026", "12.10.2026", "4000")
    assert len(get_offers(manager)) == 6

    undo(manager)

    assert get_offers(manager) == expected_offers
    assert get_undo_list(manager) == []

def test_eliminate_offers_price_nb_days():
    list_offers = []
    populate_with_dummy_data(list_offers)
    giv_price = 700
    days = 7
    eliminate_offers_price_nb_days(list_offers, giv_price, days)
    assert len(list_offers) == 3
    assert get_offer_destination(list_offers[0]) == "Sophia"
    assert get_offer_price(list_offers[1]) == 1200.0

def test_eliminate_offers_by_destinations_list():
    destinations = ["Paris", "Roma"]
    list_offers = []
    populate_with_dummy_data(list_offers)
    eliminate_offers_by_destinations_list(list_offers, destinations)
    assert len(list_offers) == 2
    assert get_offer_destination(list_offers[0]) == "Sophia"
    assert get_offer_price(list_offers[0]) == 500.00


def test_create_and_getters_setters_offer():
    offer = create_offer("Paris", "20.10.2026", "23.10.2026", 1500)
    assert get_offer_destination(offer) == "Paris"
    assert get_offer_start_date(offer) == "20.10.2026"
    assert get_offer_end_date(offer) == "23.10.2026"
    assert get_offer_price(offer) == 1500.0

    set_offer_destination(offer, "Roma")
    assert get_offer_destination(offer) == "Roma"

    set_offer_start_date(offer, "21.10.2026")
    assert get_offer_start_date(offer) == "21.10.2026"

    set_offer_end_date(offer, "25.10.2026")
    assert get_offer_end_date(offer) == "25.10.2026"

    set_offer_price(offer, 1800)
    assert get_offer_price(offer) == 1800.0


def test_validate_valid_offer():
    offer = create_offer("Paris", "10.08.2026", "15.08.2026", 1000)
    validate_offer(offer)


def test_validate_invalid_offer():
    invalid_offer = create_offer("", "31.02.2026", "15/08/2026", -100)
    try:
        validate_offer(invalid_offer)
        assert False, "Expected ValueError for an invalid offer"
    except ValueError as error:
        message = str(error)
        assert "Destination must not be empty." in message
        assert "Start date must be a valid date" in message
        assert "End date must be a valid date" in message
        assert "Price must be a positive number." in message


def test_add_an_offer():
    test_list_offers = []
    populate_with_dummy_data(test_list_offers)
    assert len(test_list_offers) == 5
    add_an_offer(test_list_offers, "France", "11.11.2026", "16.11.2026", 500)
    assert len(test_list_offers) == 6
    assert get_offer_destination(test_list_offers[5]) == "France"


def test_modify_offer_price():
    test_list_offers = []
    populate_with_dummy_data(test_list_offers)

    modify_offer_price(test_list_offers, 0, 1250)
    assert len(test_list_offers) == 5
    assert get_offer_price(test_list_offers[0]) == 1250.0
    assert get_offer_destination(test_list_offers[0]) == "Paris"
    assert get_offer_price(test_list_offers[1]) == 800.0


def test_delete_all_offers_for_a_destination():
    test_list_offers = []
    populate_with_dummy_data(test_list_offers)

    delete_all_offers_for_a_destination(test_list_offers, "Paris")
    assert len(test_list_offers) == 3
    assert get_offer_destination(test_list_offers[0]) == "Roma"


def test_remove_offers_with_shorter_duration_than_a_given_nr_of_days():
    test_list_offers = []
    populate_with_dummy_data(test_list_offers)

    remove_offers_with_shorter_duration_than_a_given_nr_of_days(test_list_offers, 2)
    assert len(test_list_offers) == 5

    remove_offers_with_shorter_duration_than_a_given_nr_of_days(test_list_offers, 6)
    assert len(test_list_offers) == 4
    assert get_offer_destination(test_list_offers[0]) == "Paris"
    assert get_offer_destination(test_list_offers[1]) == "Roma"


def test_remove_all_offers_for_which_the_price_is_greater_than_a_given_price():
    test_list_offers = []
    populate_with_dummy_data(test_list_offers)

    remove_all_offers_for_which_the_price_is_greater_than_a_given_price(test_list_offers, 700)
    assert len(test_list_offers) == 1
    assert get_offer_destination(test_list_offers[0]) == "Sophia"


def test_queries_and_reports():
    test_list_offers = []
    populate_with_dummy_data(test_list_offers)

    in_interval = compute_offers_in_time_interval(test_list_offers, "10.08.2026", "16.08.2026")
    assert len(in_interval) == 1
    assert get_offer_destination(in_interval[0]) == "Paris"

    counts = compute_offers_for_destination(test_list_offers)
    assert counts["Paris"] == 2
    assert counts["Roma"] == 1

    by_end = compute_offer_enddate(test_list_offers, "20.08.2026")
    assert len(by_end) == 2

    cheaper = compute_offers_cheaper(test_list_offers, "Paris", 1005)
    assert len(cheaper) == 1
    assert get_offer_price(cheaper[0]) == 1000.0

    assert average_price_for_destination(test_list_offers, "Paris") == 1100.0
    assert average_price_for_destination(test_list_offers, "Madrid") == 4435.25
    assert average_price_for_destination(test_list_offers, "Mongolia") == -1

    best_2 = chose_2_best_offers_in_an_interval(test_list_offers, "01.08.2026", "30.08.2026")
    assert len(best_2) == 2
    assert get_offer_price(best_2[0]) == 500.0
    assert get_offer_price(best_2[1]) == 800.0

    sorted_offers = sort_list_by_destination(test_list_offers, "a")
    assert len(sorted_offers) == 5
    assert get_offer_destination(sorted_offers[0]) == "Madrid"
    assert get_offer_destination(sorted_offers[2]) == "Paris"


def run_all_tests():
    test_undo_after_add()
    test_create_and_getters_setters_offer()
    test_validate_valid_offer()
    test_validate_invalid_offer()
    test_add_an_offer()
    test_modify_offer_price()
    test_delete_all_offers_for_a_destination()
    test_remove_offers_with_shorter_duration_than_a_given_nr_of_days()
    test_remove_all_offers_for_which_the_price_is_greater_than_a_given_price()
    test_queries_and_reports()
    test_eliminate_offers_by_destinations_list()
    test_eliminate_offers_price_nb_days()
    print("All tests passed")