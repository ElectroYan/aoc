from datetime import datetime
import os
import requests as r
from dotenv import load_dotenv
import importlib.util
import json
import re
import time

def get_test_data() -> str:
    test_data = ""
    while True:
        try:
            line = input()
        except EOFError:
            break
        test_data += line + "\n"
    return test_data.rstrip("\n")

def days_per_year(year: str) -> int:
    if int(year) < 2025:
        return 25
    else:
        return 12 # :(

def get_data(session: str, year: str, day: str) -> str:
    day_int = int(day)
    url = f"https://adventofcode.com/{year}/day/{day_int}/input"
    cookies = {"session": session}
    response = r.get(url, cookies=cookies)
    response.raise_for_status()
    return response.text

def generate_days(year: str):
    os.makedirs(f"y{year}", exist_ok=True)
    for i in range(1, days_per_year(year) + 1):
        with open(f"y{year}/d{i:02}.py", "w") as f:
            f.write(
                f"""import day\n\nclass Day(day.Day):\n    def p1(self):\n        pass\n\n    def p2(self):\n        pass\n"""
            )

def submit_answer(session: str, year: str, day: str, level: int, answer: str):
    day_int = int(day)
    url = f"https://adventofcode.com/{year}/day/{day_int}/answer"
    cookies = {"session": session}
    data = {"level": level, "answer": answer}
    ua = os.getenv("USER_AGENT", "aoc-automation-script (no AI)")
    headers = {"User-Agent": ua}
    response = r.post(url, cookies=cookies, data=data, headers=headers)
    response.raise_for_status()
    match = re.search(r'<main>(.*?)</main>', response.text, re.DOTALL)
    if match:
        content = match.group(1).strip()
        clean = re.sub('<[^<]+?>', '', content)
        return clean


def main():
    load_dotenv()
    aoc_session = os.getenv("SESSION")
    if not aoc_session:
        raise ValueError("SESSION not set in environment variables")

    os.makedirs("output", exist_ok=True)
    os.makedirs("input", exist_ok=True)

    config = {}
    if not os.path.exists("config.json"):
        config = {"year": str(datetime.now().year), "day": str(1)}
    else:
        with open("config.json") as f:
            config = json.load(f)

    year = input(f"Year [{config.get("year", datetime.now().year)}]: ") or config.get("year", datetime.now().year)
    if not year.isdigit():
        raise ValueError("Year must be a number")
    if int(year) < 2015 or int(year) > datetime.now().year:
        raise ValueError("Year must be between 2015 and the current year")
    day = input(f"Day [{config.get("day", datetime.now().day)}]: ") or config.get("day", datetime.now().day)
    if not day.isdigit():
        raise ValueError("Day must be a number")
    day = f"{int(day):02}"
    if int(day) < 1 or int(day) > days_per_year(year):
        raise ValueError(f"Day must be between 1 and {days_per_year(year)} for year {year}")

    config["year"] = year
    config["day"] = day
    with open("config.json", "w") as f:
        f.write(json.dumps(config, indent=4))

    if not os.path.exists(f"y{year}"):
        yn = input("Generate? (Y/n): ").lower() != "n"
        if yn:
            generate_days(year)


    use_test_data = input("Test? (y/N/r): ").lower() or "n"

    input_file_path = f"input/{year}-{day}{"-test" if use_test_data != "n" else ""}.txt"

    input_data = ""

    if os.path.exists(input_file_path) and use_test_data != "r":
        with open(input_file_path) as f:
            input_data = f.read()
    else:
        if use_test_data != "n":
            input_data = get_test_data()
            with open(input_file_path, "w") as f:
                f.write(input_data)
        else:
            input_data = get_data(aoc_session, str(year), str(day))
            with open(input_file_path, "w") as f:
                f.write(input_data)

    input_data = input_data.rstrip("\n")

    class_path = f"y{year}/d{int(day):02}.py"
    spec = importlib.util.spec_from_file_location(f"y{year}.d{int(day):02}", class_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    day_instance = module.Day(input_data)

    if use_test_data != "n":
        print("Level 1 (test):", day_instance.p1())
        print("Level 2 (test):", day_instance.p2())
    else:
        try:
            start_time = time.time()
            ans1 = day_instance.p1()
            end_time = time.time()
            print(f"Level 1 [{((end_time - start_time) * 1000):.05f}ms]:", ans1)
            start_time = time.time()
            ans2 = day_instance.p2()
            end_time = time.time()
            if ans1 and not ans2:
                sub1 = input("Submit? (y/N): ").lower() == "y"
                if sub1:
                    res = submit_answer(aoc_session, str(year), str(day), 1, str(ans1))
                    print(res)
                    with open(f"output/{year}-{day}-1.txt", "a+") as f:
                        f.write(f"{ans1}: {res}\n\n")

            print(f"Level 2 [{((end_time - start_time) * 1000):.05f}ms]:", ans2)
            if ans2:
                sub2 = input("Submit? (y/N): ").lower() == "y"
                if sub2:
                    res = submit_answer(aoc_session, str(year), str(day), 2, str(ans2))
                    print(res)
                    with open(f"output/{year}-{day}-2.txt", "a+") as f:
                        f.write(f"{ans2}: {res}\n\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()