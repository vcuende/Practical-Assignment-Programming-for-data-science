import pandas as pd
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

all_links = {
    'stocks': 'https://www.investing.com/funds/amundi-msci-wrld-ae-c',
    'corporate bonds': 'https://www.investing.com/etfs/ishares-global-corporate-bond-$',
    'public bonds': 'https://www.investing.com/etfs/db-x-trackers-ii-global-sovereign-5',
    'gold': 'https://www.investing.com/etfs/spdr-gold-trust',
    'cash': 'https://www.investing.com/indices/usdollar'

}

topic = 'cash'
link = all_links[topic]

# Change this variable path and write your local path where the "geckodriver" file is found
path = "/Users/victor/Documents/GitHub/Practical-Assignment-Programming-for-data-science/geckodriver"

# Create a new Firefox session
driver = webdriver.Firefox(executable_path=path)

driver.get(link)

driver.implicitly_wait(30)

# Wait for the alert to show up and then change to the alert control
accept_button = driver.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]')
accept_button.click()
print('Cookies popup clicked!')

iframe = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//iframe[@title='Cuadro de diálogo Iniciar sesión con Google']"))
)

driver.switch_to.frame(iframe)

print('Accessed to Google Account iframe')

google_signup = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.ID, 'close'))
)
google_signup.click()
print('Google popup clicked!')

# For going back to the previous web controller context:
driver.switch_to.default_content()
print('Returned to the main iframe')
# Wait till all the elements are loaded

historical_button = driver.find_element('link text', 'Historical Data')
historical_button.click()
print("Historical button clicked")

date_picker = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div/div[2]/main/div/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div')
date_picker.click()

start_date = "2020-01-01"
end_date = "2021-01-01"

dates = [start_date, end_date]

date_inputs = driver.find_elements('xpath', "//input[@type='date']")
for i, date_input in enumerate(date_inputs):
    date_input.send_keys(dates[i])
    
print(f"Start date {start_date} selected as input")
print(f"End date {end_date} selected as input")

date_picker = driver.find_element('css selector', '.inv-button.HistoryDatePicker_apply-button__fPr_G')
date_picker.click()
print("Pushed 'Apply' button")

table = driver.find_elements('css selector', ".datatable_body__cs8vJ")
rows = table[1].find_elements("xpath", ".//tr")


# Only date and price attributes are needed
date_list = []
prices_list = []

for row in rows:
    # Find all cells in the row
    cells = row.find_elements("xpath", ".//td[position() <= 2]")

    # Iterate each cell in the row
    for i, cell in enumerate(cells):
        content = cell.text

        if i == 0: #date
            date_list.append(content)
        elif i == 1: #price
            prices_list.append(content)

driver.close()
dict_df = {
    "date": date_list,
    "price": prices_list
}

filename = "usdollar"
df = pd.DataFrame(dict_df)
df.set_index('date', inplace=True)
df.to_csv(f"./files/{topic}/{filename}.csv")
