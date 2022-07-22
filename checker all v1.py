# by : @t.9j_

import time
from colorama import Fore
import requests, random,webbrowser, os
if ImportError:
    os.system('pip install requests')
    os.system('pip install random')
    os.system('pip install colorama')
    os.system('pip install time')
    os.system('pip install webbrowser')

qw12 = int(input('[1] download Libirary  >> \n[2] skip >> \n'))

if qw12 == 1:
    os.system('pip install requests')
    os.system('pip install random')
    os.system('pip install colorama')
    os.system('pip install time')
    os.system('pip install webbrowser')
elif qw12 == 2:
    pass





print("""



   ██╗ss██╗ ██╗sssss██████╗s
   ██║ss██║ ██║sssss╚════██╗
   ███████║ ██║ssssss█████╔╝
   ██╔══██║ ██║ssssss╚═══██╗
   ██║ss██║ ███████╗██████╔╝
    ╚═╝ss╚═╝ ╚══════╝╚═════╝s
   
 by : @t.9j_



""")
webbrowser.open('https://t.me/mytools111')



print(f"""
    {Fore.LIGHTRED_EX}#{Fore.LIGHTWHITE_EX}-------------{Fore.LIGHTGREEN_EX}cheacker{Fore.LIGHTWHITE_EX}-------------{Fore.LIGHTRED_EX}#{Fore.LIGHTWHITE_EX}
	|  [01] Checker Tellonym           |
	|  [02] Checker Instagram          |
	|  [03] Checker Telegram           |
	|  [04] Checker Snapchat           |
	{Fore.LIGHTRED_EX}#{Fore.LIGHTWHITE_EX}----------------------------------{Fore.LIGHTRED_EX}#{Fore.LIGHTWHITE_EX}""" '\n')


me = int(input('choose >> '))
#__________________________________________________________________________________________________________________________________________
#Tellonym
if me == int('1' or '01'):
    print("""




        """ * 100)

    print(Fore.LIGHTWHITE_EX + """


      _____      _  _                                 
     |_   _|___ | || |  ___   _ __   _   _  _ __ ___  
       | | / _ \| || | / _ \ | '_ \ | | | || '_ ` _ \ 
       | ||  __/| || || (_) || | | || |_| || | | | | |
       |_| \___||_||_| \___/ |_| |_| \__, ||_| |_| |_|
                                     |___/            

    by: @t.9j_

    """ + Fore.LIGHTWHITE_EX)



    choose = input('[1] send to telegram >>  \n[2] save in file >> ''\n')

    if choose == '2':
        type = int(input('Enter type of user >> '))
        sleep = input('Enter sleep >> ')
        while True:
            user = (''.join(random.choice('abcde_fghijklm_nopq_rstu_vwyz1234567890_') for i in range(type)))
            time.sleep(int(sleep))

            url = (f'https://tellonym.me/{user}')

            headers = {
                'authority': 'api.tellonym.me',
                'method': 'GET',
                'path': '/accounts/check?username=l.9v&limit=25',
                'scheme': 'https',
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/json;charset=utf-8',
                'if-none-match': 'W/"bc-GKNZ+AmmeV1xB5jt46lj6LM4WAs',
                'origin': 'https://tellonym.me',
                'sec-ch-ua': '.Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Windows",
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'tellonym-client': 'web:3.24.11',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

            }

            data = {

                'username': user
            }
            req = requests.get(url, headers=headers, data=data).status_code

            if req == 200:
                print(Fore.LIGHTWHITE_EX + 'not good ' + Fore.LIGHTRED_EX + user + Fore.LIGHTWHITE_EX)

            if req == 404 and choose == '1':
                print(Fore.LIGHTWHITE_EX + 'good' + ' ' + Fore.LIGHTGREEN_EX + user + Fore.LIGHTWHITE_EX)



            elif req == 404:
                print(Fore.LIGHTWHITE_EX + 'good' + ' ' + Fore.LIGHTGREEN_EX + user + Fore.LIGHTWHITE_EX)
                co = (user + '\n')
                with open('Available Tellonym.txt', 'a') as x:
                    tl = '[] NEW USER -->  '
                    x.write(tl + user + '\n' + 'by : @t.9j_')

    if choose == '1':
        pass
    type = int(input('Enter type of user >> '))
    ID = input('Enter id bot >> ')
    token = input('Enter token bot >> ')
    sleep = input('Enter sleep >> ')
    while True:
        user = (''.join(random.choice('abcdefghijklmnopqrstuvwyz1234567890') for i in range(type)))
        time.sleep(int(sleep))

        url = (f'https://tellonym.me/{user}')

        headers = {
            'authority': 'api.tellonym.me',
            'method': 'GET',
            'path': '/accounts/check?username=l.9v&limit=25',
            'scheme': 'https',
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json;charset=utf-8',
            'if-none-match': 'W/"bc-GKNZ+AmmeV1xB5jt46lj6LM4WAs',
            'origin': 'https://tellonym.me',
            'sec-ch-ua': '.Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'tellonym-client': 'web:3.24.11',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

        }

        data = {

            'username': user
        }
        req = requests.get(url, headers=headers, data=data).status_code

        if req == 200:
            print(Fore.LIGHTWHITE_EX + 'not good ' + Fore.LIGHTRED_EX + user + Fore.LIGHTWHITE_EX)

        if req == 404 and choose == '1':
            print(Fore.LIGHTWHITE_EX + 'good' + ' ' + Fore.LIGHTGREEN_EX + user + Fore.LIGHTWHITE_EX)
            tlg = (
                f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= Done hunt : {user} \n \n  by : @t.9j_ ''')
            i = requests.post(tlg)
#__________________________________________________________________________________________________________________________________
#Instagram
elif me == int('2' or '02'):


    print("""
    
    
    
    
    """ * 100)
    print("""
    
██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗         ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║        ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║        ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║        ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║        ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                          
    
    
    
    """)
    choose1 = int(input('[1] send to telegram >>  \n[2] save in file >> ''\n'))



    if choose1 == int('2' or '[2]'):

        print('\n')
        type1 = int(input('Enter type of user >> '))
        sleep1 = int(input('Enter sleep >> '))



        while True:
            user1 = (''.join(random.choice('abcdefghijklmnopqrstuvwyz1234567890') for i in range(type1)))
            url1 = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user1}'

            headers1 = {
                'authority': 'i.instagram.com',
                'method': 'GET',
                'path': f'/api/v1/users/web_profile_info/?username={user1}',
                'scheme': 'https',
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': 'ig_nrcb=1; mid=Yr2K-AALAAEDINeNBtGFxQCiGxs2; ig_did=22093F93-78CA-40AF-A467-B1499333DE30; csrftoken=38aNRM0rkyEB5ELVuevxX6s9XWE3lCVG; ds_user_id=53444607930; sessionid=53444607930%3A4dqp5jE5ijeGli%3A27%3AAYf5uvMNguqYsv3pastqcpPSsAx-ZeyiFlkwEsp7Iw; datr=P9u-Ytm770H67yOEgerRU13I; shbid="4010\05453444607930\0541689683970:01f7f2607fb140485d6b2ea8f96874b203a7e5bc73c501fe672f2ff20205dcde581f1e8e"; shbts="1658147970\05453444607930\0541689683970:01f73ee971a61c1bcb981002e29c5b8d785dcd236e42653890cee65149a5ae0d68cca4e9"; rur="ODN\05453444607930\0541689687710:01f78c4970b8d1c8f5e8862f042fed0c5f24f900284a4e00a9460f3601645baa558b1f2a"',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': "Windows",
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                'x-asbd-id': '198387',
                'x-csrftoken': '38aNRM0rkyEB5ELVuevxX6s9XWE3lCVG',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0unRbwbH2A1_b4uO9N4K76B5gnlYv0vPp1xsOZiIfG1wXi'

            }
            data1 = {
                'username': user1
            }
            req1 = requests.get(url1, headers=headers1, data=data1).status_code
            time.sleep(sleep1)
            if req1 == 200:
                print(f' not Available  {Fore.LIGHTRED_EX}[{user1}]{Fore.LIGHTWHITE_EX}')
            if not req1 == 200:
                print(f'Available or banned  {Fore.LIGHTGREEN_EX} [{user1}]{Fore.LIGHTWHITE_EX}')
                with open('Available Instagram.txt', 'a') as x:
                    tl = '[] NEW USER -->  '
                    x.write(tl + user1 + '\n' + 'by : @t.9j_')


    if choose1 == int('1' or '[1]'):
        pass
    type1 = int(input('Enter type of user >> '))
    sleep1 = int(input('Enter sleep >> '))
    ID = input('Enter id of bot >> ')
    token  = input('Enter token bot >> ')
    while True:
        user1 = (''.join(random.choice('abcdefghijklmnopqrstuvwyz1234567890') for i in range(type1)))
        url1 = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user1}'

        headers1 = {
            'authority': 'i.instagram.com',
            'method': 'GET',
            'path': f'/api/v1/users/web_profile_info/?username={user1}',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'ig_nrcb=1; mid=Yr2K-AALAAEDINeNBtGFxQCiGxs2; ig_did=22093F93-78CA-40AF-A467-B1499333DE30; csrftoken=38aNRM0rkyEB5ELVuevxX6s9XWE3lCVG; ds_user_id=53444607930; sessionid=53444607930%3A4dqp5jE5ijeGli%3A27%3AAYf5uvMNguqYsv3pastqcpPSsAx-ZeyiFlkwEsp7Iw; datr=P9u-Ytm770H67yOEgerRU13I; shbid="4010\05453444607930\0541689683970:01f7f2607fb140485d6b2ea8f96874b203a7e5bc73c501fe672f2ff20205dcde581f1e8e"; shbts="1658147970\05453444607930\0541689683970:01f73ee971a61c1bcb981002e29c5b8d785dcd236e42653890cee65149a5ae0d68cca4e9"; rur="ODN\05453444607930\0541689687710:01f78c4970b8d1c8f5e8862f042fed0c5f24f900284a4e00a9460f3601645baa558b1f2a"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-asbd-id': '198387',
            'x-csrftoken': '38aNRM0rkyEB5ELVuevxX6s9XWE3lCVG',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0unRbwbH2A1_b4uO9N4K76B5gnlYv0vPp1xsOZiIfG1wXi'

        }
        data1 = {
            'username': user1
        }
        req1 = requests.get(url1, headers=headers1, data=data1).status_code
        time.sleep(sleep1)
        if req1 == 200:
            print(f' not Available  {Fore.LIGHTRED_EX}[{user1}]{Fore.LIGHTWHITE_EX}')
        else:
            print(f'Available or banned  {Fore.LIGHTGREEN_EX} [{user1}]{Fore.LIGHTWHITE_EX}')
            tlg = (
                f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= Done hunt : {user1} \n \n  by : @t.9j_ ''')
            i = requests.post(tlg)

#______________________________________________________________________________________________________________
#Telegram
elif me == int('3' or '03'):
    print("""




        """ * 100)

    print("""
    
    
    
    
████████╗███████╗██╗     ███████╗ ██████╗ ██████╗  █████╗ ███╗   ███╗             ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝ ██╔══██╗██╔══██╗████╗ ████║            ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   █████╗  ██║     █████╗  ██║  ███╗██████╔╝███████║██╔████╔██║            ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══╝  ██║     ██╔══╝  ██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║            ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ███████╗███████╗███████╗╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║            ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝             ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                       
    
    
    """)

    choose12 = int(input('[1] send to telegram >>  \n[2] save in file >> ''\n'))


    if choose12 == int('2' or '[2]'):
        tybe3 = int(input('Enter type of user here >> '))
        sl = input('Enter sleep >> ')


        while True:

            user3 = (''.join(random.choice('abcdefghijklmnopqrstuvwyz1234567890') for i in range(tybe3)))
            url3 = (f'https://t.me/{user3}')

            req = requests.get(url3)
            time.sleep(int(sl))
            if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 3:
                print('Available' + Fore.LIGHTGREEN_EX + f' [{user3}]' + Fore.LIGHTWHITE_EX)
                co3 = (user3 + '\n')
                with open('Available Telegram.txt', 'a') as x:
                    tl = '[] NEW USER -->  '
                    x.write(tl + user3 + '\n' + 'by : @t.9j_')
            else:
                print('not Available' + Fore.LIGHTRED_EX + f' [{user3}]' + Fore.LIGHTWHITE_EX)


    if choose12 == int('1' or '[1]'):
        tybe3 = int(input('Enter type of user here >> '))
        sl3 = input('Enter sleep >> ')
        ID = input('Enter id of bot >> ')
        token = input('Enter token bot >> ')
        while True:

            user3 = (''.join(random.choice('abcdefghijklmnopqrstuvwyz1234567890') for i in range(tybe3)))
            url3 = (f'https://t.me/{user3}')

            req = requests.get(url3)
            time.sleep(int(sl3))
            if req.text.find(
                    'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 3:
                print('Available' + Fore.LIGHTGREEN_EX + f' [{user3}]' + Fore.LIGHTWHITE_EX)
                tlg = (
                    f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= Done hunt : {user3} \n \n  by : @t.9j_ ''')
                i = requests.post(tlg)
            else:
                print('not Available' + Fore.LIGHTRED_EX + f' [{user3}]' + Fore.LIGHTWHITE_EX)
    else:
        exit(0)


#__________________________________________________________________________________________________________________________
#Snapchat

if me == int('4' or '04'):
    print("""




        """ * 100)

    print("""
    
███████╗███╗   ██╗ █████╗ ██████╗  ██████╗██╗  ██╗ █████╗ ████████╗             ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗╚══██╔══╝            ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████╗██╔██╗ ██║███████║██████╔╝██║     ███████║███████║   ██║               ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
╚════██║██║╚██╗██║██╔══██║██╔═══╝ ██║     ██╔══██║██╔══██║   ██║               ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║██║ ╚████║██║  ██║██║     ╚██████╗██║  ██║██║  ██║   ██║               ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                       
    

    """)

    choose13 = int(input('[1] send to telegram >>  \n[2] save in file >> ''\n'))

    if choose13 == int('1' or '[1]'):
        type4 = int(input('Enter type of user  >> '))
        sl6 = input('Enter sleep >> ')
        ID = input('Enter id of bot >> ')
        token = input('Enter token of bot >> ')
        while True:
            count = int(0)
            user7 = (''.join(random.choice('abcdefghijklmnopqrstuvwyz1234567890_') for i in range(type4)))
            url6 = 'https://accounts.snapchat.com/accounts/get_username_suggestions'
            headers7 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '57',
                'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
                'origin': 'https://accounts.snapchat.com',
                'referer': 'https://accounts.snapchat.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'same-origin',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
            }
            data7 = {
                'requested_username': user7,
                'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
            req_checker = requests.post(url6, data=data7, headers=headers7).text
            time.sleep(int(sl6))
            if '"status_code":"OK"' in req_checker:
                count += 1
                print(f'[{count}]' + Fore.LIGHTWHITE_EX + ' 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 ==> :' + Fore.LIGHTGREEN_EX + f'{user7}' + Fore.LIGHTWHITE_EX)
                tlg = (
                    f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= Done hunt : {user7} \n \n  by : @t.9j_ ''')
                i = requests.post(tlg)


            elif '"status_code":"TAKEN"' in req_checker:
                print(
                    f'{count}'' 𝐍𝐎𝐓 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 ==> :' + Fore.LIGHTGREEN_EX + f'{user7}' + Fore.LIGHTWHITE_EX)
            elif '"status_code":"INVALID_BEGIN"' in req_checker:
                print(f'[❌] bad begin ==> : {user7}')
            elif '"status_code":"INVALID_END"' in req_checker:
                print(f'[❌] bad end ==> : {user7}')
            elif '"status_code":"DELETED"' in req_checker:
                print(f'[❌] DELETED [ban] user ==> : {user7}')
            elif '"status_code":"INVALID_SEPARATED"' in req_checker:
                print(Fore.LIGHTYELLOW_EX + f'[❌] you got blocked wait ==> : {user7}' + Fore.LIGHTWHITE_EX)
            else:
                print(f'[❌] unknown error ==> : {user7}', req_checker)
    if choose13 == int('2' or '[2]'):
        type4 = int(input('Enter user type >> '))
        sl6 = input('Enter sleep >> ')
        while True:
            count = int(0)
            user7 = (''.join(random.choice('abcdefghijklmnopqrstuvwyz1234567890_') for i in range(type4)))
            url6 = 'https://accounts.snapchat.com/accounts/get_username_suggestions'
            headers7 = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '57',
                'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
                'origin': 'https://accounts.snapchat.com',
                'referer': 'https://accounts.snapchat.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'same-origin',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
            }
            data7 = {
                'requested_username': user7,
                'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
            req_checker = requests.post(url6, data=data7, headers=headers7).text
            time.sleep(int(sl6))
            if '"status_code":"OK"' in req_checker:
                count += 1
                print(f'[{count}]' + Fore.LIGHTGREEN_EX + ' 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 ==> :' f'{user7}' + Fore.LIGHTWHITE_EX)
                with open('Available snapchat.txt', 'a') as x:
                    tl = '[] NEW USER -->  '
                    x.write(tl + user7 + '\n' + 'by : @t.9j_')
            elif '"status_code":"TAKEN"' in req_checker:
                print(f'{count}'+Fore.LIGHTWHITE_EX+' 𝐍𝐎𝐓 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 ==> :' + Fore.LIGHTRED_EX + f'{user7}' + Fore.LIGHTWHITE_EX)
            elif '"status_code":"INVALID_BEGIN"' in req_checker:
                print(f'[❌] bad begin ==> : {user7}')
            elif '"status_code":"INVALID_END"' in req_checker:
                print(f'[❌] bad end ==> : {user7}')
            elif '"status_code":"DELETED"' in req_checker:
                print(f'[❌] DELETED [ban] user ==> : {user7}')
            elif '"status_code":"INVALID_SEPARATED"' in req_checker:
                print(Fore.LIGHTYELLOW_EX + f'[❌] you got blocked wait ==> : {user7}')
            else:
                print(f'[❌] unknown error ==> : {user7}', req_checker)

    else:
        exit(0)



#Instagram_____________________________________________________________________________________________________________
#500 سطر ههههههههههههههههههههه