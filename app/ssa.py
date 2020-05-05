from bs4 import BeautifulSoup
import requests

#def ssa_scrape(name, sex): #https://stackoverflow.com/questions/52835681/how-can-i-run-a-python-script-from-within-flask
#    request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
#    params = {"name": name, "sex": sex}
#    response = requests.post(request_url, params)
#    #print(response.status_code)
#    soup = BeautifulSoup(response.text, "html.parser")
#    return soup

def ssa_scrape(name, sex): 
    while True:
        request_url = "https://www.ssa.gov/cgi-bin/babyname.cgi"
        params = {"name": name, "sex": sex}
        response = requests.post(request_url, params)
        soup = BeautifulSoup(response.text, "html.parser")
        if not "Please enter another name." in soup.text:
            facts = soup.body.find("ul")
            return facts.text
        else:
            return "Heg is not in the top 1000 names for any year of birth beginning with 2000. Please enter another name."

if __name__ == "__main__":

    sexes = ["M", "F"]

    name = input("Please enter your baby's first name: ")

    while True:
        sex = input("Please enter your baby's sex as either 'M' or 'F': ")    
        if sex in sexes:
            break      
        else: 
            print ("Hey, please enter your baby's sex as either 'M' or 'F. Please try again!")

    ssa_scrape(name, sex)