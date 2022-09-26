import requests
import json
from columbia_student_resource import ColumbiaStudentResource


def t1():

    health_url = "http://127.0.0.1:5011/api/health"

    try:
        h_message = requests.get(health_url)
        if h_message.status_code == 200:
            print("\n\n Congratulations. Your end-to-end test worked. \n\n")
            print("Application health message = \n")
            data = h_message.json()
            print(json.dumps(data, indent=2))
            print("\n")
        else:
            print("\n\n Epic Fail. Status code = ", h_message.status_code, "\n\n")
            print("\n")
    except Exception as e:
        print("\n\n Epic, Epic, Epic Fail. Exception = ", e, "\n\n")
        print("\n")


def t2():
    res = ColumbiaStudentResource.get_by_key('bf64cb39-a13a-4905-9cd9-df77348e2bb2')
    print(json.dumps(res, indent=2, default=str))


def t3():
    query_url = "http://127.0.0.1:5011/api/students/c7916b38-c44e-4185-b7bc-a15c628800f0"

    try:
        q_message = requests.get(query_url)
        if q_message.status_code == 200:
            print("\n\n Congratulations. Your querying database with url test worked. \n\n")
            print("Application health message = \n")
            data = q_message.json()
            print(json.dumps(data, indent=2))
            print("\n")
        else:
            print("\n\n Epic Fail. Status code = ", q_message.status_code, "\n\n")
            print("\n")
    except Exception as e:
        print("\n\n Epic, Epic, Epic Fail. Exception = ", e, "\n\n")
        print("\n")


if __name__ == "__main__":
    t1()
    print("testing database querying")
    t2()
    print("\n")
    print("testing database querying using URL")
    t3()

