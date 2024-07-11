import requests, os
from bs4 import BeautifulSoup as bs

def flatten_list (lol) :
    flattened_list = ""
    for row in lol:
        flattened_list += ",".join(row) + "\n"
    return flattened_list
    

base_url = "https://datalemur.com"
response = requests.get(base_url + "/questions?category=SQL")
soup = bs(response.content)
# print(soup.prettify())
table = soup.find('table')
# print(table)


data=[]
for i,row in enumerate(table.find_all('tr')[1:]):
    # print(row)

    # print(i+1,end=".\t")
    question_metadata = row.find_all("a",{"class":"TableLink_link__hjAob"})
    company = question_metadata[0].getText().strip()
    difficulty = question_metadata[-1].getText().strip()
    question_name = question_metadata[1].getText().strip()
    link = row.find("a")['href'].strip()
    # print(*[
    #     company
    #     ,difficulty
    #     ,question_name
    #     ], sep="\t")
    data.append([str(i+1), company, difficulty, question_name, base_url + link])

    folder = f"{i+1} - {question_name} [{company} SQL Interview Question]/"
    if not os.path.exists(folder):
        os.mkdir(folder)
        with open(folder + f"{i+1} - problem.md", 'w') as file: 
            file.write(f"""# {question_name} [{company} SQL Interview Question]

> Problem info:
> Difficulty: `{difficulty}`
> Company: `{company}`

""")
        with open(folder + f"{i+1} - solution.sql", 'w') as file: file.write("-- Solved on: PostgreSQL 14")

csv_string = flatten_list(data)
with open("questions.csv", 'w+') as file:
    file.write(csv_string)