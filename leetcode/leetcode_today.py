import os
import requests
import json
import datetime

DIR = os.path.dirname(__file__)

def leetcode_today():
    print(datetime.datetime.now().isoformat())
    url = "https://leetcode.com/graphql"

    query = """
    query {
        activeDailyCodingChallengeQuestion {
            link, 
            question {
                questionId,
                title,
                titleSlug,
                difficulty,
                content,
                exampleTestcases,
                categoryTitle,
                topicTags {
                    name
                },
                codeSnippets {
                    lang,
                    code
                }
            }
        }
    }
    """

    payload = {
        "query": query,
        "variables": {}
    }
    payload = json.dumps(payload)
    headers = {
      'Content-Type': 'application/json',
    }

    res = requests.request("POST", url, headers=headers, data=payload).json()

    res = res["data"]["activeDailyCodingChallengeQuestion"]

    q = res["question"]
    with open(os.path.join(DIR, f'{q["questionId"]}. {q["title"]}.md'), "w", encoding="utf8") as f:
        f.write(q["content"])

    for x in q["codeSnippets"]:
        if x["lang"] == "Python3":
            with open(os.path.join(DIR, f'{q["questionId"]}.py'), "w", encoding="utf8") as f:
                f.write(x["code"])
            break
    print(q["questionId"])
    print(q["title"])
    print(q["difficulty"])
    print("https://leetcode.com" + res["link"])
    
    # !git add "{q["questionId"]}.*"
    # !git commit -m "Leetcode {q["questionId"]}"
    # !git push

if __name__ == "__main__":
    leetcode_today()