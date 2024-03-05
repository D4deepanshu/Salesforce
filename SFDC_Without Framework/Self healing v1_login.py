from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element_self_healing(driver, locator, timeout=20):
    """
    Find an element using a self-healing locator strategy.
    If the element is not found using the traditional locator,
    it will try to find the element using a heuristic approach.
    """
    try:
        # Try to find the element using the traditional locator
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except Exception:
        # If the element is not found, try to find it using the heuristic approach
        try:
            # Find all elements that contain the desired substring in their ID attribute
            elements = driver.find_elements_by_xpath(f"//*[contains(@id,'{locator[1]}')]")

            # If only one element is found, return it
            if len(elements) == 1:
                return elements[0]

            # If multiple elements are found, raise an exception
            raise Exception(f"Found {len(elements)} elements using the heuristic approach. Please refine your locator.")
        except Exception as e:
            # If the heuristic approach fails, raise an exception
            raise Exception(f"Failed to find element using locator {locator}. Reason: {str(e)}")


# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the Salesforce CPQ login page
driver.get("https://login.salesforce.com/")

# Find and interact with the username field
username_locator = (By.XPATH, "//input[contains(@id,'username')]")
find_element_self_healing(driver, username_locator).send_keys("deepanshu.arora@abm.com.cpq")

# Find and interact with the password field
password_locator = (By.XPATH, "//input[contains(@id,'password')]")
find_element_self_healing(driver, password_locator).send_keys("D4deepanshu@123")

# Find and click the Login button
login_button_locator = (By.XPATH, "//input[contains(@id,'Login')]")
find_element_self_healing(driver, login_button_locator).click()

# Print the title of the page
print(driver.title)

# Close the driver
driver.quit()