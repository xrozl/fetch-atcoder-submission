import asyncio
import json
import os

from tqdm import tqdm

from atcoder import fetch_all_submissions, fetch_submission_code


def get_extension(language):
    for v in extensions:
        if language.startswith(v):
            return f".{extensions[v]}"
    return ""


def read_json(path):
    with open(path, mode="r", encoding="UTF-8") as f:
        return json.load(f)


def write_code(submission, code):
    language = submission["language"]
    contest_id = submission["contest_id"]
    problem_id = submission["problem_id"]
    extension = get_extension(language)

    dir_path = f"./dist/{language}/{contest_id}/"
    file_path = f"{dir_path}{problem_id}{extension}" if extension != "" else f"{dir_path}{problem_id}"

    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, mode="w", encoding="UTF-8", newline="") as f:
        f.write(code)

    return


def filter_ac_and_latest(submissions):
    _submissions = sorted(submissions, key=lambda x: x["epoch_second"], reverse=True)
    history = set()
    result = []

    for submission in _submissions:
        if submission["result"] == "AC":
            pair = (submission["language"], submission["problem_id"])
            if pair not in history:
                history.add(pair)
                result.append(submission)

    return result


async def main():
    all_submission = fetch_all_submissions(USER_ID)
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

    for submission in tqdm(filter_ac_and_latest(all_submission)):
        await asyncio.sleep(1.5)
        code = fetch_submission_code(submission["contest_id"], submission["id"])
        loop.run_in_executor(None, write_code, submission, code)

    print("All latest AC codes have been fetched.")
    return


if __name__ == "__main__":
    USER_ID = input("Please input your atcoder id:")
    extensions = read_json("./src/extensions.json")
    asyncio.run(main())
