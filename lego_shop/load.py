import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Back

class LinksForCategories:
    
    def __init__(self):
        self.links = []
        self.url = "https://lekub.ru"

    def load(self):
        if not self.links:
            response = requests.get(f"{self.url}/catalog.html")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            divs = soup.find_all('div', class_='col-6 col-xl-3')

            for div in divs:
                a_tag = div.find('a')
                if a_tag and 'href' in a_tag.attrs:
                    self.links.append(f"{self.url}{a_tag['href']}")
            
            del self.links[0]

        return self.links.copy()


class ProductParser:
    def __init__(self):
        self.category_links = LinksForCategories()
        self.products = {}

    def load(self):
        category_links = self.category_links.load()
        
        for link in category_links:
            response = requests.get(link)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            divs = soup.find_all('div', class_=lambda x: x and 
                                ('col-6 col-sm-6 col-xl-4 even' in x or 
                                'col-6 col-sm-6 col-xl-4 odd' in x))
            
            for div in divs:
                meta_tags = div.find_all('meta', attrs={'content': True})
                name = meta_tags[1]['content'] if len(meta_tags) > 1 else 'Нет названия'
                name = self.reformat_name(name)

                price_div = div.find('div', class_='price3 text-coral')
                price = price_div.get_text(strip=True) if price_div else 'Нет цены'
                price = self.reformat_price(price)
                
                if name != 'Нет названия' and price != 'Нет цены':
                    self.products[name] = price
                        
        return self.products
    
    def reformat_name(self, name):
        article_match = re.search(r'(?:^|\s)(\d{4,7}(?:-\d{1,4})?)(?:\s|$)', name)

        if not article_match:
            return name
        
        article = article_match.group(1)
        
        parts = re.split(r'(?:^|\s)' + re.escape(article) + r'(?:\s|$)', name, maxsplit=1)
        before = parts[0].strip() if parts[0] else ""
        after = parts[1].strip() if len(parts) > 1 else ""
        if 'Лего' in before:
                before = before.replace('Лего ', '')
        if 'Лего' in after:
                after = after.replace('Лего ', '')

        brand_match = re.search(r'\b([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*)\s+\b', before + " " + after)
        if brand_match:
            brand = brand_match.group(1)
   
            if brand in before:
                description = (before.replace(brand, "").strip() + " " + after).strip()
            else:
                description = (before + " " + after.replace(brand, "").strip()).strip()
            
            return f"{Fore.LIGHTBLACK_EX}{brand} {Fore.LIGHTWHITE_EX}{article}: {Fore.RESET}{description}"
        
        if before:
            return f"{Fore.LIGHTWHITE_EX}{article}: {Fore.RESET}{before} {after}".strip()
        
        return f"{Fore.LIGHTWHITE_EX}{article}: {Fore.RESET}{after}".strip()
    
    def reformat_price(self, price):
        try:
            reformat_price = price.replace(' ', '')
            reformat_price = reformat_price[:-1]
            if int(reformat_price) >= 5000:
                reformat_price = Fore.RED + reformat_price + Fore.RESET
            else:
                reformat_price = Fore.GREEN + reformat_price + Fore.RESET
            return reformat_price + ' рублей'
        except Exception:
            return price

products = ProductParser().load()
    
print(f"Найдено {len(products)} товаров:", end='\n')
for name, price in list(products.items()): 
    print(f"{name} — {price}")