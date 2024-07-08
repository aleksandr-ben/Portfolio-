import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ngware.fr/mf2/revisef2.html")

with open("table.csv", "w", newline = "\n", encoding="utf-8") as file:
	answerwriter = csv.writer(file, delimiter = ";")
	answerwriter.writerow(["Field", "Theme", "Data", "City", "Points", "Question", "Answer"])
	for link in driver.find_elements(By.TAG_NAME, "a"):
		link.click()
	for elem in driver.find_elements(By.ID, "sujet"):
		titlerow = elem.find_elements(By.CLASS_NAME, "gris")[1]
		question = elem.find_element(By.CLASS_NAME, "danlebleu")
		title = [t.strip() for t in titlerow.text.split("/")]
		title[4] = title[4].split()[0].strip()
		ansdiv = title[-1]
		row = title[:-2]
		row += [question.text.strip()]
		answer = elem.find_element(By.ID, ansdiv)
		row += [answer.text.strip()]
		print(row)
		answerwriter.writerow(row)

driver.close()