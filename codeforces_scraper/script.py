import requests
import json
import bs4
import re

CLEANR = re.compile("<.*?>")


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, "", raw_html)
    return cleantext


def split_value_and_unit(soup):
    length = soup.split()
    return {"value": int(length[0]), "unit": length[1]}


def test_group(lst):
    return [{"input": _in, "output": _out} for _in, _out in pairwise(lst)]


def test_sample(souped_html):
    return test_group(get_tags_contents(souped_html, "pre"))


def get_tags_contents(souped_html, tag_name, class_name=None):
    return [
        concat_contents(tag.contents)
        for tag in souped_html.find_all(tag_name, class_name)
    ]


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def get_statement(soup):
    return concat_contents(soup.find("div", "header").next_sibling.contents)


def get_content(soup, _class=""):
    element = soup.find("div", _class)
    if not element:
        return None
    tags = element.contents
    tags.pop(0)
    return concat_contents(tags)


def concat_contents(ls):
    return "".join([str(i) for i in ls])


def scrap_wraper(problem_link):
    markup = requests.get(problem_link).text
    soup = bs4.BeautifulSoup(markup, "html.parser")
    problem = {
        "title": soup.find("div", "title").string,
        "timeLimit": split_value_and_unit(
            soup.find("div", "time-limit").contents[1].string
        ),
        "memoryLimit": split_value_and_unit(
            soup.find("div", "memory-limit").contents[1].string
        ),
        "statement": get_statement(soup),
        "inputSpecification": get_content(soup, "input-specification"),
        "outputSpecification": get_content(soup, "output-specification"),
        "samples": test_sample(soup),
        "note": get_content(soup, "note"),
    }
    return problem


def get_all_problems():
    url = "https://codeforces.com/api/problemset.problems"
    print(url)

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        print(json.dumps(data["result"]["problems"], sort_keys=True, indent=4))
    else:
        print("SORRY! SERVER ERROR EXISTS")


def get_all_problems_by_tag(tag):
    url = "https://codeforces.com/api/problemset.problems"

    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        list_of_all_problems = data["result"]["problems"]
        for index in list_of_all_problems:
            tags_of_problem = index["tags"]
            if tags_of_problem.count(tag):
                print(index)

    else:
        print("SORRY! SERVER ERROR EXISTS")


def get_problem_statement_by_id_and_index(id, index):
    url = "https://codeforces.com/problemset/problem/" + id + "/" + index
    data = scrap_wraper(url)
    print(cleanhtml(data["statement"]))
    print(cleanhtml(data["inputSpecification"]))
    print(cleanhtml(data["outputSpecification"]))


def main():
    ch = "YES"
    while ch == "YES":
        print("PLEASE SELECT ANY ONE OF THE BELOW :")
        print("\n1. GET ALL PROBLEMS")
        print("\n2. GET ALL PROBLEMS BY TAGS \n3. GET PROBLEM STATEMENT ")

        answer = int(input())

        if answer == 1:
            get_all_problems()

        elif answer == 2:
            print("\nPlease Enter Your Tag : ")
            tag = input()
            get_all_problems_by_tag(tag)

        elif answer == 3:
            print("\nPlease Enter Id and Index as Follows : \nId : ")
            id = input()
            print("\nIndex : ")
            index = input()
            get_problem_statement_by_id_and_index(id, index)

        ch = input("WOULD YOU LIKE TO CONTINUE : ")


if __name__ == "__main__":
    main()
