import boto3
import json

# Initialize Bedrock client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2"  # Change if you're using a different region
)

# Function to call Bedrock LLM
def call_bedrock(prompt):
    try:
        response = bedrock.invoke_model(
            modelId="anthropic.claude-v2",  # Replace with your approved model ID
            contentType="application/json",
            body=json.dumps({
                "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
                "max_tokens_to_sample": 300
            })
        )
        result = json.loads(response['body'].read().decode())
        return result.get("completion", "[No output received]")
    except Exception as e:
        return f"Error calling Bedrock: {str(e)}"
