from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize the Firefox driver
driver = webdriver.Firefox()
# Navigate to the web page
driver.get("https://abm--cpq.sandbox.my.salesforce.com/")

# Maximize the window
driver.maximize_window()

# Define a function to find an element using a self-healing locator
def find_element_self_healing(driver, locator):
    # Wait for up to 10 seconds before throwing a TimeoutException
    wait = WebDriverWait(driver, 10)

    # Try to find the element using the provided locator
    try:
        element = wait.until(EC.presence_of_element_located(locator))
        return element
    except:
        pass

    # If the element was not found, try to find it using a heuristic approach
    elements = driver.find_elements_by_xpath("//*[contains(@id,'" + locator[1] + "')]")

    # If multiple elements were found, return the first one
    if len(elements) > 0:
        return elements[0]

    # If no elements were found, raise an exception
    raise Exception("Could not find element with locator: " + str(locator))

# # Use the self-healing locator to find and click the Login button
# locator = (By.XPATH, "//input[contains(@id,'Login')]")
# find_element_self_healing(driver, locator).click()

# Use the self-healing locator to find and send keys to the username field
locator = (By.XPATH, "//input[contains(@id,'username')]")
find_element_self_healing(driver, locator).send_keys("deepanshu.arora@abm.com.cpq")

# Use the self-healing locator to find and send keys to the password field
locator = (By.XPATH, "//input[contains(@id,'password')]")
find_element_self_healing(driver, locator).send_keys("D4deepanshu@123")

# Use the self-healing locator to find and click the Login button
locator = (By.XPATH, "//input[contains(@id,'Login')]")
find_element_self_healing(driver, locator).click()

# Print the title of the page
print(driver.title)

# Close the driver
driver.quit()
