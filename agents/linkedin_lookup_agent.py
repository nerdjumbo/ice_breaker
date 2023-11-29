from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

# from tools.tools import get_profile_url_using_serp
from langchain.tools.brave_search.tool import BraveSearch
import json


def lookup(name):
    llm_model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    FIND_PERSON_PROMPT_STR = """
        given the search string for person's name and unique search criteria, {person_name} I want you to get me 
        
        1- a link to their LinkedIN Profile Page. 
        2- a link to their facebook page.
        
        Your answer should be in the JSON format with the fields [linkedin_url, facebook_url]
        if any field is empty still add key with empty string as value
    """

    tools_for_agent = [
        # Tool(
        #     name="Crawl Google for Linkedin profile page",
        #     func=get_profile_url,
        #     description="useful for when you need get the Linkedin Page URL",
        # )
        BraveSearch.from_api_key(
            api_key="BSA8KTQWE4oa2DPQyY2LR2jXs34Jln5", search_kwargs={"count": 5}
        )
    ]
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm_model,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_error=True,
    )
    prompt_template = PromptTemplate(
        template=FIND_PERSON_PROMPT_STR, input_variables=["person_name"]
    )
    agent_output = agent.run(prompt_template.format_prompt(person_name=name))
    print(agent_output)
    print(type(agent_output))

    return json.loads(agent_output)
