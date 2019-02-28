import json
import psycopg2
import requests
import time


conn = psycopg2.connect(database="tweeter_db", user="tweeteruser", host="localhost", port="26257")
conn.set_session(autocommit=True)
curr = conn.cursor()

url =  "https://github.com/zalamgir/tweeter-go-tester/blob/master/shakespeare-tweets.json"
after = {"after": "null"}

for n in range(300000):
    req = requests.get(url, params=after, headers={"User-Agent": "Python"})

    resp = req.json()
    after = {"after": str(resp['tweets']['after'])}

    tweets = json.dumps(resp)

    cur.execute("""INSERT INTO tweeter_db.tweeter_table (posts)
            SELECT json_arry_elements(%s->'tweets')""", (tweets,))

    time.sleep(2)

cur.close()
conn.close()
