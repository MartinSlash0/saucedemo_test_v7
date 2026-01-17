                                    ---===Selenium Pytest Automation Framework===---
                                                 made by MartinSlash0
           
                                      This project is a UI test automation framework
                                    I built with Python, Selenium and Pytest following
                                       the Page Object Model (POM) design pattern.

                                  The framework automates from start to finish tests for:
                                  - Login functionality
                                  - Shopping cart & checkout flow
                                  
                                                    TESTED WEBSITES:
                                  - https://www.saucedemo.com
                                  
                                                       TECH STACK:                  
                                  
                                  - Python 3.11               - Pytest-HTML
                                  - Selenium WebDriver        - Firefox (GeckoDriver)
                                  - Pytest                    - Page Object Model (POM)
                                  
                                                    PROJECT STRUCTURE:
                                  
                                                  saucedemo_test_v7/
                                                  │
                                                  ├── pages/
                                                  │ ├── base_page.py
                                                  │ ├── login_page.py
                                                  │ └── store_page.py
                                                  │
                                                  ├── tests/
                                                  │ ├── test_login.py
                                                  │ ├── test_checkout.py
                                                  │
                                                  ├── locators.py
                                                  ├── config.py
                                                  ├── conftest.py
                                                  ├── screenshots/
                                                  ├── reports/
                                                  │ └── report.html
                                                  └── README.md
                                  
                                                  HOW TO RUN TESTS:
                                  
                                  1) Clone my repository
                                  
                                  --> git clone https://github.com/your-username/your-repo-name.git
                                  cd your-repo-name
                                  
                                  2) Install dependencies
                                  
                                  --> pip install -r requirements.txt
                                  
                                  3) A. Run all tests       or   B. Run with HTML report
                                  
                                  A. --> pytest
                                  B. -->pytest --html=report.html --self-contained-html
                                  
                                                  TEST SCENARIOS COVERED:
                                  
                                  - Valid and Invalid login
                                  = Login verification using UI elements
                                  
                                  - Shopping and checkout
                                  = Add item to cart
                                  = Verify item in cart
                                  = Checkout flow
                                  = Order completion validation
                                  
                                                  SCREENSHOTS ON FAILURE:
                                  - Screenshots are automatically captured
                                  - Stored in the screenshots/ directory
                                  - Embedded directly into the HTML report
                                  
                                  ========================================================
                                     This project was built as part of my QA Automation
                                    learning path and an attempt to fulfill my dream of
                                   working in the field of QA Automation. I tried focusing
                                  on best practices and real-world test automation patterns.
                                  
                                   Thank you for giving me a bit of your time by looking at
                                       my little project and I hope I can bring a bit of
                                     inspiration to you guys to build something yourselfs.
