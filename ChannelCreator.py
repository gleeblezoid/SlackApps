import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)

# Listen to incoming command
@app.command("/channel")
def command_channel(ack, say, command):
    ack()
    say(
        {
            "blocks": [
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Private Channel Name",
                        "emoji": True,
                    },
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Private Channel Disclaimer",
                        "emoji": True,
                    },
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Click Me",
                                "emoji": True,
                            },
                            "value": "Create Channel",
                            "action_id": "actionId-0",
                        }
                    ],
                },
            ]
        }
    )


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
