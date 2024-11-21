import requests


class SiteManager:
    def __init__(self):
        self.sites = []

    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
            print(f"Сайт {url} добавлен.")
        else:
            print(f"Сайт {url} уже существует в списке.")

    def get_sites(self):
        return self.sites


class SiteParser:
    def fetch_content(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Ошибка при получении сайта {url}: {e}")
            return ""

    def search_content(self, content, query):
        return content.lower().count(query.lower())


class UserInterface:
    def display_results(self, results):
        if not results:
            print("Нет совпадений.")
            return

        print("Результаты поиска:")
        sorted_results = sorted(results.items(), key=self.sort_key, reverse=True)
        for site, count in sorted_results:
            if count > 0:
                print(f"На сайте {site} найдено {count} совпадений.")

    def sort_key(self, item):
        return item[1]


class SearchApp:
    def __init__(self):
        self.site_manager = SiteManager()
        self.parser = SiteParser()
        self.ui = UserInterface()

    def add_sites(self):
        url = input("Введите URL сайта: ").strip()
        if url:
            self.site_manager.add_site(url)
        else:
            print("URL не может быть пустым.")

    def search(self):
        query = input("Введите запрос для поиска: ")
        sites = self.site_manager.get_sites()
        if not sites:
            print("Список сайтов пуст. Добавьте сайты для начала.")
            return

        results = {}
        for site in sites:
            print(f"Поиск на сайте {site}...")
            content = self.parser.fetch_content(site)
            matches = self.parser.search_content(content, query)
            results[site] = matches

        self.ui.display_results(results)

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Добавить сайт")
            print("2. Искать информацию на всех сайтах")
            print("3. Выход")
            choice = input("Выберите действие: ")

            if choice == "1":
                self.add_sites()
            elif choice == "2":
                self.search()
            elif choice == "3":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    app = SearchApp()
    app.run()