# Vacation Offers Manager

A modular Python CLI application designed for managing, filtering, and analyzing holiday offers. The project follows a layered architecture with custom domain validation, state management with multi-step Undo support, and an automated unit test suite.

> **Note:** This project is actively being developed. A web interface built with Streamlit is currently in the testing phase and will be released in a future update.

## Features

- **Offer Management:** Add new vacation offers and modify existing prices with full input validation.
- **Deletion & Filtering:**
  - Remove offers by destination, maximum price threshold, or minimum duration (in days).
  - Filter out offers matching a custom list of destinations or specific price-to-duration criteria.
- **Search & Queries:**
  - Find offers within a specific date interval (`DD.MM.YYYY`).
  - Search offers by destination below a target price or by exact end date.
- **Reports & Statistics:**
  - Calculate the average price for a specific destination.
  - View the total number of available offers per destination.
  - Filter offers by destination substring, sorted alphabetically.
  - Retrieve the top 2 cheapest offers within a given time interval.
- **Undo Mechanism:** Revert previous state-modifying operations (additions, price updates, deletions, and filters).
- **Automated Testing:** Built-in assertion test suite executed automatically at startup.

## Tech Stack

- **Language:** Python 3.10+
- **Standard Libraries:** `datetime`
- **Testing:** Custom assertion-based unit tests

## Project Structure

```text
vacation_offers_manager/
│
├── main.py             # Application entry point
├── domain.py           # Offer entity definition, getters, setters, and validation
├── list_offers.py      # Business logic, filtering, reports, and dummy data
├── manager.py          # State management and Undo history stack
├── user_interface.py   # Interactive CLI menus and user input handling
├── tests.py            # Automated unit test suite
├── LICENSE             # MIT License
└── README.md           # Project documentation
