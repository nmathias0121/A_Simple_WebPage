# A_Simple_WebPage
A Basic webpage developed in HTML and JavaScript, tested using Python Selenium

# Files
- web-page
  - parent_page.html: introduction page contains a form to be filled
  - response_page.html: this page loads after form is filled and the submit button is clicked. If the secret field in the form is filled correctly, a new button will show that loads the secret page
  - secret_page.html: this page is loaded when the secret words are entered in the parent page.
- pytest
  - test_selenium.py: pytests for secret and non-secret scenarios
