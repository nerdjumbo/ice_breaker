from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_internet_profile
from output_parsers import person_intel_parser, PersonIntel
from typing import Tuple


def ice_break(name) -> Tuple[PersonIntel, str]:
    linkedin_profile_url = lookup(name=name)
    print(linkedin_profile_url)

    summary_template = """
    given the Linkedin information {information} about a persom from I want you to create:
    1. a short summary
    2. two interesting facts about them
    3. Topics that may interest the person
    4. Create two creative ice breakers to open a conversation with the person
    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0.0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print("value of linkedin url is " + linkedin_profile_url["linkedin_url"])
    print("value of facebook url is " + str(linkedin_profile_url["facebook_url"]))

    linkedin_data = scrape_internet_profile(linkedin_profile_url["linkedin_url"])
    facebook_data = scrape_internet_profile(linkedin_profile_url["facebook_url"])
    chain_output = chain.run(information=linkedin_data + facebook_data)

    print(chain_output)
    return (
        person_intel_parser.parse(text=chain_output),
        "https://media.licdn.com/dms/image/C5603AQHy3NzIerdrSQ/profile-displayphoto-shrink_100_100/0/1630772345656?e=1706140800&v=beta&t=glXim89yqqTKy-mBCidz_4e8MICo9uvZbZE_peBrowM",
    )


if __name__ == "__main__":
    name = "Narender Modi"
    result = ice_break(name)
