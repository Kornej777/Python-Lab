from bs4 import BeautifulSoup
import requests

class LoadRegions:

    def __init__(self, url):
        self.url = url
        self.region_map = {}

    def load(self):

        if not self.region_map:

            try:
                response = requests.get(self.url)
                soup = BeautifulSoup(response.text, "lxml")

                target_header = soup.find(
                    lambda tag: tag.name in ["h1"] 
                    and "Автомобильные коды регионов России" in tag.text
                )
                
                if not target_header:
                    return {}

                table = target_header.find_next("table")
                
                if not table:
                    return {}

                rows = table.find_all("tr")[1:]

                for row in rows:
                    cells = row.find_all("td")
                    if len(cells) >= 2:
                        codes_str = cells[0].get_text(strip=True)
                        region = cells[1].get_text(strip=True)
                        
                        codes_split = codes_str.split(", ")
                        
                        for code in codes_split:
                            code_clean = code.strip()
                            if code_clean:
                                self.region_map[code_clean] = region

            except:
                self.region_map = {}

            return self.region_map
