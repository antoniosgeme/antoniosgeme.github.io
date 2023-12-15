from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# URL of your Google Scholar profile
profile_url = 'https://scholar.google.com/citations?user=tQpJjzwAAAAJ&hl=en&authuser=1'

driver = webdriver.Chrome()
# Navigate to your Google Scholar profile
driver.get(profile_url)

# Wait for the page to load (adjust the sleep duration as needed)
time.sleep(5)

show_more_clicked = True

# Continue scrolling down to load more publications until "Show more" is not clicked in an iteration
while show_more_clicked:
    # Scroll down to the bottom of the page
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)

    # Wait for a short duration to allow new publications to load (adjust as needed)
    time.sleep(2)

    # Check if the "Show more" button is displayed
    show_more_button = driver.find_element(By.XPATH, '//button[contains(text(), "Show more")]')
    
    if show_more_button.is_displayed():
        # Click "Show more" and set the flag to True
        show_more_button.click()
        show_more_clicked = True
    else:
        # If "Show more" is not displayed, set the flag to False to exit the loop
        show_more_clicked = False

# Find all publication entries on the page
publication_entries = driver.find_elements(By.CSS_SELECTOR, '.gs_ri')

# Iterate through each publication entry
for entry in publication_entries:
    # Extract the title and click on it to view citation
    title_element = entry.find_element(By.TAG_NAME, 'h3')
    title = title_element.text
    title_element.click()

    # Wait for the citation section to load (adjust the sleep duration as needed)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'gs_citt')))

    # Find the LaTeX citation
    latex_citation = driver.find_element(By.ID, 'gs_citt').text

    # Print the LaTeX citation
    print(latex_citation)

    # Close the citation overlay
    close_button = driver.find_element(By.XPATH, '//div[@id="gs_citd"]//button[@aria-label="Close"]')
    close_button.click()

# Close the browser
driver.quit()