import requests
from bs4 import BeautifulSoup

def get_cgpa(url, roll_number):
    # Send GET request with roll number as parameter
    params = {'rollno': roll_number}  # Change 'rollno' to match the actual input name
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Failed to fetch page.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.prettify())

    print("       ")
	
    # Step 1: Get 2nd table
    tables = soup.find_all('table')
    if len(tables) < 2:
        print("Less than 2 tables found.")
        return
    second_table = tables[1]

    # Print raw HTML inside second_table
    #print(second_table.prettify())

    # Step 2: Get tbody of 2nd table
    tbody = second_table.find('tbody')
    if not tbody:
        print("tbody not found in 2nd table.")
        return

    # Step 3: Get 2nd <tr>
    trs = tbody.find_all('tr')
    if len(trs) < 2:
        print("Less than 2 <tr> found.")
        return
    second_tr = trs[1]

    # Step 4: Get 1st <td> of 2nd <tr>
    tds = second_tr.find_all('td')
    if not tds:
        print("No <td> in 2nd <tr>.")
        return
    first_td = tds[0]

    # Step 5: Get <span> inside 1st <td>
    span = first_td.find('span')
    if not span:
        print("No <span> found in <td>.")
        return

    # Step 6: Get all inner tables in the span
    inner_tables = span.find_all('table')
    if len(inner_tables) < 2:
        print("Less than 2 inner tables in span.")
        return
    target_table = inner_tables[1]

    # Step 7: Extract required <td>
    inner_tbody = target_table.find('tbody')
    if not inner_tbody:
        print("No tbody in inner table.")
        return
    inner_trs = inner_tbody.find_all('tr')
    if not inner_trs:
        print("No tr in inner tbody.")
        return
    target_tds = inner_trs[0].find_all('td')
    if len(target_tds) < 2:
        print("Expected <td> not found.")
        return

    cgpa = target_tds[1].get_text(strip=True).replace('\xa0', '')
    print("Extracted CGPA:", cgpa)

# Example usage
url = "http://202.63.117.72/result_2024_VIISEM/index.php"   # 🔁 Replace with actual URL
roll_number = "100521733006"      # 🔁 Replace with actual roll number
get_cgpa(url, roll_number)
