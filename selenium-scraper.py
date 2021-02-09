from selenium import webdriver
import time
driver = webdriver.Firefox()

with open("vinod-khosla-videos.txt", "w") as file:
     
    driver.get(f"https://waitwho.is/vinod-khosla/videos")
    time.sleep(4)
    results = driver.find_elements_by_xpath("//iframe")
    for iframe in results:
        extra_part = len("https://www.youtube.com/embed/")
        video_id = iframe.get_attribute('src')[extra_part:]
        file.write(f"https://www.youtube.com/watch?v={video_id}\n")

    time.sleep(5)

print("EXIT")