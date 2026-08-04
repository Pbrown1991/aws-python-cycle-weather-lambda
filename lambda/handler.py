import urllib.request
import json
from urllib.error import URLError, HTTPError

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast?latitude=53.41&longitude=-2.16&hourly=temperature_2m,precipitation_probability,precipitation,weather_code,wind_speed_10m&timezone=Europe/London&forecast_days=2"

def handler(event, context):
    try:
        req = urllib.request.Request(OPEN_METEO_URL)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())

    except HTTPError as e:
        print(f"HTTP error {e.code}: {e.reason}")
        return {"statusCode": e.code, "body": f"Weather API error: {e.reason}"}
    except URLError as e:
        print(f"URL error: {e.reason}")
        return {"statusCode": 500, "body": f"Network error: {e.reason}"}

    print(data)
    return {"statusCode": 200, "body": "OK"}

if __name__ == "__main__":
      import pprint
      result = handler({}, None)
      pprint.pprint(result)