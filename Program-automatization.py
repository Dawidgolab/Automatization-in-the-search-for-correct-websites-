import requests

Bossfile = "test.txt"

with open(Bossfile,'r',encoding="UTF-8") as file:
    readFile = file.readlines()
    for page in readFile:
        try:
            respond = requests.get(page.strip())
            encodingPage = respond.status_code
            if encodingPage == 200:
                with open("GoodPage.txt",'a+',encoding="UTF-8") as good_file:
                    GoodPage = good_file.write(page)
        except (requests.exceptions.RequestException,requests.exceptions.MissingSchema,
                requests.exceptions.ConnectionError):
            print(f"ERROR!!! That page is wrong : {page}(code-404)")
        except FileNotFoundError:
            print("ERROR!!! The file 'test.txt' does not exist or cannot be found.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")