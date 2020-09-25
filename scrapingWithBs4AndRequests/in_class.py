import json
import requests
from bs4 import BeautifulSoup
import time


def save_object( file_name  , saved_object , writing_method):

    saved_object = json.dumps(saved_object, indent=3 , ensure_ascii=False)
    with open(file_name, writing_method) as handler:
        handler.writelines(saved_object + ',')



def main():

    print('Hello Guys!')




if __name__ == "__main__":
    main()