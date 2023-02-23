#libraries
import requests
from bs4 import BeautifulSoup
import csv


#request name e.g.  Aarbo Kirsten,  Abdelmalek Bassam,  Akins Stacie , 
# vet_clinic_name e.g. Big Rock Animal Clinic , Chaparral Veterinary Clinic  and Marda Loop Animal Hospital
# vet_clinic_type e.g. General Practice Registered Veterinarian, Time Limited Registered Veterinarian, Unsupervised Limited Practice Registered Veterinarian
# def get_data(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     return soup

# def parse_data(soup):
#     table = soup.find('table', attrs={'class': 'table table-striped'})
#     rows = table.find_all('tr')
#     for row in rows:
#         cols = row.find_all('td')
#         cols = [ele.text.strip() for ele in cols]
#         data.append([ele for ele in cols if ele]) # Get rid of empty values
#     return data
# #write to csv with column names: name, vet_clinic_name, vet_clinic_type
# def write_csv(data):
#     with open('abvma.csv', 'w') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['name', 'vet_clinic_name', 'vet_clinic_type'])
#         for name in data:
#             writer.writerow(name)
# #main
# if __name__ == "__main__":
#     url = 'https://www.abvma.ca/client/roster/clientRosterView.html?clientRosterId=168'
#     soup = get_data(url)
#     data = parse_data(soup)
#     write_csv(data)
#end



# ####From C******
# Python script that uses the Beautiful Soup library to scrape the information you requested from the URL you provided, and saves the output to a CSV file:


import requests
from bs4 import BeautifulSoup
import csv

url = "https://abvma.ca/company/roster/companyRosterView.html?companyRosterId=23"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

data = []

# Extracting the data
Physical_Location = soup.find("div", {"class":"col-md-4"}).find("p").get_text(strip=True)
Phone = soup.find("div", {"class":"col-md-4"}).find_all("p")[1].get_text(strip=True)
Fax = soup.find("div", {"class":"col-md-4"}).find_all("p")[2].get_text(strip=True)
Email = soup.find("div", {"class":"col-md-4"}).find_all("p")[3].get_text(strip=True)
Website = soup.find("div", {"class":"col-md-4"}).find_all("p")[4].get_text(strip=True)
Veterinarians = soup.find("div", {"class":"col-md-4"}).find_all("p")[5].get_text(strip=True)
RVT = soup.find("div", {"class":"col-md-4"}).find_all("p")[6].get_text(strip=True)
Services_provided = soup.find("div", {"class":"col-md-4"}).find_all("p")[7].get_text(strip=True)
Practice_Name = soup.find("h3").get_text(strip=True)
Responsible_Vet = soup.find("p", {"class":"text-muted"}).get_text(strip=True)
Species = soup.find("div", {"class":"col-md-8"}).find_all("p")[1].get_text(strip=True)
City = soup.find("div", {"class":"col-md-8"}).find_all("p")[2].get_text(strip=True)
Province = soup.find("div", {"class":"col-md-8"}).find_all("p")[3].get_text(strip=True)

data.append({"Practice Name":Practice_Name, "Physical Location":Physical_Location, "Phone":Phone, "Fax":Fax, "Email":Email, "Website":Website, "Veterinarians":Veterinarians, "RVT":RVT, "Services provided":Services_provided, "Responsible Vet":Responsible_Vet, "Species":Species, "City":City, "Province":Province})

# Saving the data to a CSV file
with open("output.csv", "w", newline="") as f:
    fieldnames = ["Practice Name", "Physical Location", "Phone", "Fax", "Email", "Website", "Veterinarians", "RVT", "Services provided", "Responsible Vet", "Species", "City", "Province"]
    writer = csv.D



###From Copilot
#Use Beautiful soup in python to write me a code that scrapes or extracts data of Physical Location:, Phone:, Fax:, Email:, Website:, Veterinarians:, RVT's: , 
# Services provided for the following species :, Practice Name, Responsible Vet, Species, City, Province from: https://abvma.ca/company/roster/companyRosterView.html?companyRosterId=23
#Save the output in a CSV file.

# import requests
# from bs4 import BeautifulSoup
# import csv
