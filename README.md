# OnlineStoreAPI-Framework

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![pytest](https://img.shields.io/badge/Tested_with-pytest-green?logo=pytest)
![Allure](https://img.shields.io/badge/Reports-Allure-orange?logo=allure)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)


## Overview

This repository contains a **Python-based API testing framework** designed for validating store-related functionalities. The framework is built with **pytest** and integrates with **Allure reporting** for clear test results. It focuses on REST API testing around user management, authentication, product handling, and order workflows.

## Key Features & Benefits

*   **Pytest-based Framework:** Modular and scalable test execution.
*   **REST API Testing:** Covers core store APIs including login, user, and product endpoints.
*   **Data-driven Testing:** Test data is separated and reusable.
*   **Allure Reports:** Generates rich, interactive HTML reports.
*   **Custom Utilities:** Includes reusable methods for requests, assertions, and setup/teardown.
*   **CI/CD Friendly:** Can be integrated with GitHub Actions or Jenkins for automated runs.

## Prerequisites & Dependencies

Before you begin, ensure you have the following installed:

*   **Python:** Python 3.8 or higher is recommended.
*   **pip:** Python package installer.
*   **pytest:** Install using `pip install pytest`.
*   **requests:** Install using `pip install requests`.
*   **pytest-html / Allure-pytest:** For report generation.  
    ```bash
    pip install pytest-html allure-pytest
    ```

Optional:
*   **Allure Commandline:** Download and add to system PATH for advanced reporting.

## Installation & Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/uditSINGH43/OnlineStoreAPI-Framework.git
    cd OnlineStoreAPI-Framework
    ```

2. **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    # source venv/bin/activate  # On Linux/macOS
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment (Optional):**  
   Update any environment variables or test data in `config/` or `data/` files as needed.

## Usage Examples & API Documentation

1. **Running Tests:**
    ```bash
    pytest -v -s
    ```

    Generate an HTML report:
    ```bash
    pytest --html=report.html
    ```

    Generate an Allure report:
    ```bash
    pytest --alluredir=reports/allure-results
    allure serve reports/allure-results
    ```

2. **Example Test Structure:**
   * `testCases/test_user_tests.py`: Covers user login and registration APIs.
   * `testCases/test_product_tests.py`: Validates product endpoints.
   * `utils/common.py`: Helper functions for requests and data handling.

   A typical test:
   ```python
   def test_login_valid_user(api_client):
       response = api_client.post("/login", json={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert "token" in response.json()
