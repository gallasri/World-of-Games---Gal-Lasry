from selenium import webdriver

def test_scores_service(app_url):
    driver = webdriver.Chrome()
    driver.get(app_url)
    score_element = driver.find_element_by_id("score")
    score = int(score_element.text)
    driver.quit()
    return 1 <= score <= 1000

def main_function():
    app_url = "http://localhost:8777"
    if not test_scores_service(app_url):
        print("Test failed!")
        return -1
    print("Test passed!")
    return 0

if __name__ == "__main__":
    main_function()


