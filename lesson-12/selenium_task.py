from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start browser maximized
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Open Google
    driver.get("https://www.google.com")

    # Step 2: Find search bar and enter query
    search_box = driver.find_element(By.NAME, "q")  # Google's search bar name
    search_query = "latest news on artificial intelligence"
    search_box.send_keys(search_query, Keys.ENTER)

    # Step 3: Wait for results to load
    time.sleep(10)

    # Step 4: Click on the first search result
    first_result = driver.find_element(By.TAG_NAME, "h3")
    first_result.click()

    # Step 5: Wait for the article page to load
    time.sleep(10)

    # Step 6: Extract the article headline (usually inside <h1>)
    try:
        headline = driver.find_element(By.TAG_NAME, "h1").text
    except:
        headline = "Headline not found"

    # Step 7: Get the current URL
    article_url = driver.current_url

    # Step 8: Take a screenshot
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved as '{screenshot_path}'")

    # Step 9: Save headline & URL to a text file
    with open("article_info.txt", "w", encoding="utf-8") as file:
        file.write(f"Search Query: {search_query}\n")
        file.write(f"Article Headline: {headline}\n")
        file.write(f"Article URL: {article_url}\n")

    print("Article information saved to 'article_info.txt'")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)
    driver.quit()
