import csv
import requests

# function to generate api result
def gettax(address, city, zip):
      # !! spaces in the address or city need to be separated by '+' symbol
      address = address.replace(" ", "+")
      city = city.replace(" ", "+")
      apiaddress = "https://services.maps.cdtfa.ca.gov/api/taxrate/GetRateByAddress?address={}&city={}&zip={}".format(address, city, zip)
      x = requests.get(apiaddress)
      xjson = x.json() # this turns a json
      try:
            return xjson["taxRateInfo"][0]["rate"]
      except Exception:
            return "ERROR"


file = open(r"C:\Users\Annika - Accounting\PROJECTS\ca-taxes\shipping-addresses.csv", "r")
newfile = open(r"C:\Users\Annika - Accounting\PROJECTS\ca-taxes\ca-taxes.csv", "w", newline = "") # newline = ""

csvreader = csv.reader(file)

row_count = len(file.readlines())
file.seek(3)
next(csvreader)

csvwriter = csv.writer(newfile)
csvwriter.writerow(["Address", "City", "Zip", "Tax"])
counter = 0
for row in csvreader:
      address = row[0]
      city = row[1]
      zip = row[2]
      tax = str(gettax(address, city, zip))
      rowlist = [address, city, zip, tax]
      csvwriter.writerow(rowlist)
      counter += 1
      print(str(counter) + "/" + str(row_count))

file.close()
newfile.close()
    
print("Complete")