import requests
from bs4 import BeautifulSoup


def fetch_all_submissions(user):
    url = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions"
    payload = {"user": user, "from_second": 0}
    response = requests.get(url, params=payload)
    return response.json()


def fetch_submission_code(contest_id, submission_id):
    url = f"https://atcoder.jp/contests/{contest_id}/submissions/{submission_id}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    code = soup.select_one("pre#submission-code").text
    return code
