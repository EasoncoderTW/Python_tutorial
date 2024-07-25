import requests
from bs4 import BeautifulSoup

class TyphoonDays:
    def __init__(self, url = "https://www.dgpa.gov.tw/typh/daily/nds.html") -> None:
        self.url = url


    def __call__(self, search_city = []):
        response = requests.get(self.url) # Download
        content = response.content.decode("utf-8") # Decode
        
        # string find
        front = content.find("<TR><TD headers='city_Name'")
        # truncated the string ahead of front
        content = content[front:] 
        tear = content.find("<!-- 備註 #a5a1c2-->") # find the tear
        content = content[:tear]
        
        # Use bs4 to parse the HTML format string
        soup = BeautifulSoup(content, "html.parser")
        
        # parse city
        result = soup.find_all("tr")
        
        # parse text
        result_dict = dict() # create a empty dictionary
        for r in result:
            city_info = r.find_all("td")
            city_name = city_info[0].getText()
            city_status = city_info[1].getText()
            result_dict[city_name] = city_status # append a element into dictionary
            #print(city_name,city_status)
        
        result_str = ""    
        if len(search_city) == 0: # user want to get all info
            result_str += "----- 停止上班 -----\n"
            for name,status in result_dict.items():
                if "停止上班" in status:
                    result_str += name
                    result_str += " "
            result_str += "\n----- 停止上課-----\n"
            for name,status in result_dict.items():
                if "停止上課" in status:
                    result_str += name
                    result_str += " "
            result_str += "\n"
        else: # has specific city
            for name in search_city:
                result_str += ("[" +name + "] ")
                result_str += result_dict[name] # use dictionary to find the status
                result_str += "\n"

        return result_str