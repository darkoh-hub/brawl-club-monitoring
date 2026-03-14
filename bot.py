import requests
import time

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM5OWFmYWViLTk2NGUtNGExNi04Zjc5LWYzNWQ5ZGEyOGVlNSIsImlhdCI6MTc3MzUyNzg3Nywic3ViIjoiZGV2ZWxvcGVyLzRiMWMwNTAxLWRkYWItMTlmOC0wOTQ1LWU0YzM3ZGZiNTAzNSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiODAuMjE1LjE0OS4xOTciXSwidHlwZSI6ImNsaWVudCJ9XX0.L3VIHggpUifXXPMOfZ41glCQWTGCb-e4GPq6tVKkLe2-uDoo8CyGFhLfUuB33KnqHafi3jvAS2MMtEekZgYgYQ"
BOT_TOKEN = "8254681433:AAGO7XUPg-zk4Aiw2tck3_xGXWFyefdJrzM"

CHANNEL_ID = "-1003707137096"
CLUB_TAG = "%232VYPJ2PLU"

url = f"https://api.brawlstars.com/v1/clubs/{CLUB_TAG}"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

players = []

def send(msg):
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHANNEL_ID,
            "text": msg
        }
    )

while True:
    r = requests.get(url, headers=headers)
    data = r.json()

    current_players = [p["name"] for p in data["members"]]

    for p in players:
        if p not in current_players:
            send(f"🚫 BAN ALERT\n\nГравець {p} більше не в клубі")

    players = current_players

    time.sleep(60)
