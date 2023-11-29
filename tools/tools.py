from langchain.serpapi import SerpAPIWrapper


def get_profile_url_using_serp(text):
    """Searches for Linkedin Profile Page"""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res


# def get_profile_url_using_brave(text):
#     """Searches for Linkedin Profile Page"""
#    pass
