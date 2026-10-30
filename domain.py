from datetime import datetime


def create_offer(destination: str, start_date: str, end_date: str, price: float | int):
    """
    Create a vacation offer entity.
    :param destination: destination of vacation
    :type destination: str
    :param start_date: starting date of vacation (format DD.MM.YYYY)
    :type start_date: str
    :param end_date: ending date of vacation (format DD.MM.YYYY)
    :type end_date: str
    :param price: vacation price
    :type price: float
    :return: offer entity
    :rtype: dict
    """
    return [destination, start_date, end_date, float(price)]


def get_offer_destination(offer):
    """
    Return the destination of an offer.
    :param offer: an offer entity
    :return: the offer destination
    :rtype: str
    """
    return offer[0]


def get_offer_start_date(offer):
    """
    Return the start date of an offer.
    :param offer: an offer entity
    :return: the offer start date (format DD.MM.YYYY)
    :rtype: str
    """
    return offer[1]


def get_offer_end_date(offer):
    """
    Return the end date of an offer.
    :param offer: an offer entity
    :return: the offer end date (format DD.MM.YYYY)
    :rtype: str
    """
    return offer[2]


def get_offer_price(offer):
    """
    Return the price of an offer.
    :param offer: an offer entity
    :return: the offer price
    :rtype: float
    """
    return offer[3]


def set_offer_destination(offer, destination: str):
    """
    Change the destination of an offer.
    :param offer: an offer entity
    :param destination: the new destination
    :type destination: str
    :return: None
    """
    offer[0] = destination


def set_offer_start_date(offer, start_date: str):
    """
    Change the start date of an offer.
    :param offer: an offer entity
    :param start_date: the new start date (format DD.MM.YYYY)
    :type start_date: str
    :return: None
    """
    offer[1] = start_date


def set_offer_end_date(offer, end_date: str):
    """
    Change the end date of an offer.
    :param offer: an offer entity
    :param end_date: the new end date (format DD.MM.YYYY)
    :type end_date: str
    :return: None
    """
    offer[2] = end_date


def set_offer_price(offer, price: float | int):
    """
    Change the price of an offer.
    :param offer: an offer entity
    :param price: the new price
    :type price: float
    :return: None
    """
    offer[3] = float(price)


def validate_offer(offer):
    """
    Validate the fields of an offer using the entity interface.
    :param offer: offer entity to validate
    :return: None
    :raises ValueError: if a field contains an invalid value
    """
    errors = ""
    destination = get_offer_destination(offer)
    start_date = get_offer_start_date(offer)
    end_date = get_offer_end_date(offer)
    price = get_offer_price(offer)

    if not isinstance(destination, str) or destination.strip() == "":
        errors += "Destination must not be empty. "

    valid_start = None
    valid_end = None
    try:
        valid_start = datetime.strptime(start_date, "%d.%m.%Y")
    except (TypeError, ValueError):
        errors += "Start date must be a valid date in the format 'DD.MM.YYYY'. "

    try:
        valid_end = datetime.strptime(end_date, "%d.%m.%Y")
    except (TypeError, ValueError):
        errors += "End date must be a valid date in the format 'DD.MM.YYYY'. "

    if valid_start is not None and valid_end is not None and valid_start > valid_end:
        errors += "Start date must be before or equal to end date. "

    if not isinstance(price, (int, float)) or price <= 0:
        errors += "Price must be a positive number."

    if errors:
        raise ValueError(errors.strip())