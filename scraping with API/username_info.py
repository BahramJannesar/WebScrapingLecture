from instagram_private_api import Client, ClientCompatPatch
from login import login
import time
import json

user_name = 'moradidataclass'
password = '123qweasd'


def save_object( file_name  , saved_object , writing_method):

    saved_object = json.dumps(saved_object, indent=3 , ensure_ascii= False)
    with open(file_name, writing_method) as handler:
        handler.writelines(saved_object)



def main():

    api = login(user_name, password)

    user_info = api.username_info('GoodiBoodi')

    save_object('user_info.json' , user_info  , 'w')



if __name__ == "__main__":

    main()