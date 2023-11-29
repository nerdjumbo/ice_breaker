import requests
from bs4 import BeautifulSoup

# def scrape_linkedin_profile(linkedin_profile_url):
#     """
#     Scrape info  from linkedin profile
#     Args:
#         linkedin_profile_url (_type_): _description_
#     """
#     linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
#     data = requests.get(linkedin_profile_url).json()
#     data = {
#         k: v
#         for k, v in data.items()
#         if v not in ([], "", None, {})
#         and k not in ["people_also_viewed", "certifications"]
#     }

#     if data.get("groups"):
#         for group_dict in data.get("groups"):
#             group_dict.pop("profile_pic_url")

#     return data


def scrape_internet_profile(url_to_scrape: str):
    # Make an HTTP request to the webpage
    if url_to_scrape == "":
        return f"nothing found for this url {url_to_scrape}"
    response = requests.get(url_to_scrape)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract information from the webpage as needed
        page_title = soup.title.text
        return soup.find("body").text  # Adjust as per your needs
    else:
        return f"nothing found for this url {url_to_scrape}"
