from tests import run_all_tests
from list_offers import populate_with_dummy_data
from user_interface import start_ui


def main():
    run_all_tests()
    list_offers = []
    populate_with_dummy_data(list_offers)
    start_ui(list_offers)


if __name__ == "__main__":
    main()