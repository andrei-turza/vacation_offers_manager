from tests import run_all_tests
from manager import create_offer_manager, get_offers
from list_offers import populate_with_dummy_data
from user_interface import start_ui


def main():
    run_all_tests()
    manager = create_offer_manager()
    populate_with_dummy_data(get_offers(manager))
    start_ui(manager)


if __name__ == "__main__":
    main()