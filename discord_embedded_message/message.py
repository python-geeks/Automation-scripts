import datetime
import json
import requests


def send_message(
    webhook_url: str,
    content_msg="",
    title="",
    title_url="",
    color=00000000,
    timestamp=datetime.datetime.now().isoformat(),
    footer_icon="",
    footer="",
    thumbnail_url="",
    author="",
    author_url="",
    author_icon_url="",
    text_name="",
    text="",
):
    payload = {
        "content": content_msg,
        "embeds": [
            {
                "title": title,
                "url": title_url,
                "color": color,
                "timestamp": timestamp,
                "footer": {
                    "icon_url": footer_icon,
                    "text": footer,
                },
                "thumbnail": {"url": thumbnail_url},
                "author": {
                    "name": author,
                    "url": author_url,
                    "icon_url": author_icon_url,
                },
                "fields": [
                    {
                        "name": text_name,
                        "value": text,
                    }
                ],
            }
        ],
    }
    print(">> Sending To WebHook...")
    payload = json.dumps(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, headers=headers, data=payload)
    return response


def example_calling():
    webhook_url = "your_webhook_url"
    response = send_message(
        webhook_url,
        content_msg="Some random text",
        title="Discord Embed example",
        title_url="https://discordjs.guide/popular-topics/embeds.html#embed-preview",
        color=15335679,
        footer_icon="https://github.githubassets.com/favicons/favicon-dark.png",
        footer="May the Force be with you",
        thumbnail_url="https://avatars.githubusercontent.com/u/55619686",
        author="OjusWiZard",
        author_url="https://github.com/OjusWiZard/",
        author_icon_url="https://avatars.githubusercontent.com/u/55619686",
        text_name=":point_down: :point_down: :point_down:",
        text="This is a test message",
    )
    print("Status: ", response.status_code)


if __name__ == "__main__":
    example_calling()
