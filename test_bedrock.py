from bedrock_client import call_bedrock
from prompts import faq_prompt


if __name__ == "__main__":
    question = "How do I access my company email?"
    filled_prompt = faq_prompt.format(faq_data="1. Use Outlook with your company login.", question=question)
    
    print("LLM Response:")
    print(call_bedrock(filled_prompt))

