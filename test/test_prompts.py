from prompts.faq_prompt import faq_prompt
from bedrock.call_model import call_bedrock

# Sample test data
faq_data = """
1. You can access your email through Outlook at outlook.office.com.
2. Sign in using your company credentials.
"""
question = "How do I access my email?"

# Fill the template
filled_prompt = faq_prompt.format(faq_data=faq_data, question=question)

# Call the Bedrock model
print("🤖 LLM Response:")
response = call_bedrock(filled_prompt)
print(response)