import boto3
import os
import re
import sys
import json
from dotenv import load_dotenv

load_dotenv()

bedrock_client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION"))
model_id = os.getenv("MODEL_ID")
max_tokens = int(os.getenv("MAX_TOKENS"))
assistant_role = os.getenv("ASSISTANT_ROLE")


def analyze_file_contents(file_contents):
    """
    Uses Amazon Bedrock's Claude 3 Haiku model to analyze the contents of a file.
    Removes any comments from the file contents, splits messages into smaller chunks of at most max_tokens,
    calls the Bedrock API to analyze each chunk, and returns the response.

    Args:
    - file_contents (str): The contents of the file to analyze.

    Returns:
    - The response from the Claude model, or None if an error occurs.
    """

    # Strip comments from the file contents
    file_contents = re.sub(
        r'^\s*"""[\s\S]*?"""\s*$', "", file_contents, flags=re.MULTILINE
    )
    file_contents = re.sub(r"^\s*#[\s\S]*?\s*$", "", file_contents, flags=re.MULTILINE)
    file_contents = re.sub(r"^\s*//[\s\S]*?\s*$", "", file_contents, flags=re.MULTILINE)

    print("Splitting messages into smaller chunks of at most max_tokens")

    # Split the message into smaller chunks of at most max_tokens
    message_chunks = [
        file_contents[i : i + max_tokens]
        for i in range(0, len(file_contents), max_tokens)
    ]

    response = None
    try:
        for i, chunk in enumerate(message_chunks, 1):
            # Create payload for Bedrock API
            payload = {
                "modelId": model_id,
                "contentType": "application/json",
                "accept": "application/json",
                "body": json.dumps(
                    {
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": max_tokens,
                        "messages": [
                            {
                                "role": "assistant",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": assistant_role
                                    }
                                ],
                            },
                            {"role": "user", "content": chunk},
                        ],
                    }
                ),
            }

            # Call the Bedrock API
            response = bedrock_client.invoke_model(**payload)
            response_body = json.loads(response["body"].read())

            return response_body

    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return None
    except KeyboardInterrupt:
        print("KeyboardInterrupt caught. Exiting...")
        sys.exit()

    return response
