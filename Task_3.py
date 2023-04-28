import requests
from bs4 import BeautifulSoup


def count_pages(html):
    soup = BeautifulSoup(html.text, "html.parser")
    line = soup.find("ul", class_="pagination").find_all("li")
    pages = []
    for j in line:
        pages.append(j.text[-1])
    global max_page
    max_page = (max(pages))
    get_page_data(max_page)


def get_page_data(max_page):
    url = "https://ru.proxy-tools.com/proxy/socks5?page="
    for i in range(1, int(max_page) + 1):
        page = requests.get(url + str(i))
        soup = BeautifulSoup(page.text, "html.parser")
        line = (soup.find("table",
                          class_="table table-sm table-responsive-md table-hover").find(
            "tbody").find_all("tr"))
        for j in line:
            td = j.find_all("td")
            j = td[4]
            countries.append((j.text).strip())
    print("\n".join(set(countries)), "\n")
    current_country()


def current_country():
    country = input("Выберите страну: ")
    with open(f"proxy_{country}", "w") as file_input:
        for i in range(1, int(max_page) + 1):
            page = requests.get(url + str(i))
            soup = BeautifulSoup(page.text, "html.parser")
            line = (soup.find("table",
                              class_="table table-sm table-responsive-md table-hover").find(
                "tbody").find_all("tr"))
            for i in line:
                td = i.find_all("td")
                i = td[0]
                if (td[4].text).strip() == country:
                    print(i.text)
                    file_input.write(i.text + "\n")


if __name__ == "__main__":
    max_pages = 100
    countries = []
    url = "https://ru.proxy-tools.com/proxy/socks5?page="
    page = requests.get(url)
    count_pages(page)
