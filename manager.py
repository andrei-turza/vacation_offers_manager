from domain import create_offer, validate_offer

def delete_offer(manager, offer_index):
    """
    Delete the offer with the given index, saving state for undo.
    :param manager: dictionary containing offers and undo_list
    :param offer_index: int, index of the offer to delete
    :return: None
    """
    offers = get_offers(manager)
    if 0 <= offer_index < len(offers):
        save_state_for_undo(manager)
        offers.pop(offer_index)
    else:
        raise ValueError("Invalid offer index.")

def add_offer(manager, destination, start_date, end_date, price):
    """Add offer to the list"""
    offer = create_offer(destination, start_date, end_date, price)
    validate_offer(offer)

    save_state_for_undo(manager)
    get_offers(manager).append(offer)

def undo(manager):
    """Restores the transaction list to its previous state"""
    undo_list = get_undo_list(manager)
    if len(undo_list) == 0:
        raise ValueError("There is no operation to undo")

    previous_state = undo_list.pop()
    set_offers(manager, previous_state)

def save_state_for_undo(manager):
    """save the state of the list before the last modification"""
    current_state = get_offers(manager)
    state_copy = copy_list_of_lists(current_state)
    get_undo_list(manager).append(state_copy)


def copy_list_of_lists(list_offers):
    """Creates a copy of a list of lists"""
    new_list = []
    for offer in list_offers:
        new_offer = []
        for value in offer:
            new_offer.append(value)
        new_list.append(new_offer)
    return new_list

def create_offer_manager():
    """
    Create a manager with offers list and the history
    for undo operation
    :return: a dictionary with 2 keys
        offers: the current list of offers
        undo_list: copies of previous list states
    """
    return {
        "offers": [],
        "undo_list": []
    }

def get_offers(manager):
    """return the current offers list"""
    return manager["offers"]

def get_undo_list(manager):
    """return the undo list"""
    return manager["undo_list"]

def set_offers(manager, offers):
    """
    Set the current list of offers
    :param manager: dictionary
    :param offers: new list of offers
    :return: None
    """
    manager["offers"] = offers