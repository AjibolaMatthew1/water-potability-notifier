import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# Get your Slack token from environment variables or directly
#SLACK_TOKEN = str(os.getenv("SLACK_TOKEN"))
#client = WebClient(token=SLACK_TOKEN)

def log_to_slack(message, channel='#water-potability-notifier'):
    try:
        response = client.chat_postMessage(
            channel=channel,
            text=message
        )
    except SlackApiError as e:
        # Optionally handle Slack API errors here
        print(f"Failed to send message to Slack: {e.response['error']}")


if __name__ == "__main__":
    error_message = "TUYA Error: Water sensor failed to report data"
    response = log_to_slack(error_message, "#water-potability-notifier")
    if response:
        print("Message posted successfully")
    else:
        print("Failed to post message")
