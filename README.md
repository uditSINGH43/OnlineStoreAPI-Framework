# OnlineStoreAPI-Framework

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![pytest](https://img.shields.io/badge/Tested_with-pytest-green?logo=pytest)
![Allure](https://img.shields.io/badge/Reports-Allure-orange?logo=allure)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen)

## Overview

The **OnlineStoreAPI-Framework** is a Python-based **automated testing framework** tailored for validating the **REST APIs of an online store application**.  
It is designed to ensure that critical backend services like **user management, authentication, product catalog, cart, and order workflows** are reliable and functioning correctly.  

This framework is not just a collection of test cases — it follows **industry best practices**, making it **scalable, maintainable, and CI/CD ready**.  
It can be easily extended to new APIs and integrated into pipelines for continuous testing.

---

## Why This Framework?  

Modern e-commerce systems rely heavily on APIs. A small bug in login, checkout, or payment APIs can break the customer experience.  
This project ensures:  

- **Reliability:** Every API is tested for success and failure cases.  
- **Maintainability:** Clear structure with modular, reusable test cases.  
- **Scalability:** Add new endpoints without breaking existing ones.  
- **Professional Reporting:** Test results are available in **HTML** and **Allure interactive dashboards**.  

---

## Key Features & Benefits

- **Pytest-powered:** Test discovery, fixtures, and parallel execution support.  
- **End-to-End API Testing:** Covers login, user creation, product management, and order checkout.  
- **Reusable API Client:** Centralized utility to handle HTTP requests and responses.  
- **Data-driven:** JSON-based input for flexibility in running multiple scenarios.  
- **Assertions & Validations:** Built-in reusable assertions for response codes and payloads.  
- **Reporting:**  
  - **pytest-html** → Generates static HTML reports.  
  - **Allure** → Interactive dashboards with step-level logs and graphs.  

---
