import pyautogui, time

def autoGod():
    smiteGods = ['agni', 'ah muzen cab', 'ah puch', 'amaterasu', 'anhur', 'anubis',
             'ao kuang', 'aphrodite', 'apollo', 'arachne', 'ares', 'artemis',
             'artio', 'athena', 'awilix', 'bacchus', 'bakasura', 'bastet',
             'bellona', 'cabrakan', 'camazotz', 'cerberus', 'cernunnos',
             'chaac', "chang'e", 'chiron', 'chronos', 'cu chulainn', 'cupid',
             'da ji', 'discordia', 'erlang shen', 'fafnir', 'fenrir', 'freya',
             'ganesha', 'geb', 'guan yu', 'hachiman', 'hades', 'he bo', 'hel',
             'hercules', 'hou yi', 'hun batz', 'isis', 'izanami', 'janus',
             'jing wei', 'kali', 'khepri', 'kukulkan', 'kumbhakarna', 'kuzenbo',
             'loki', 'medusa', 'mercury', 'ne zha', 'neith', 'nemesis', 'nike',
             'nox', 'nu wa', 'odin', 'osiris', 'poseidon', 'ra', 'raijin',
             'rama', 'rataoskr', 'ravana', 'scylla', 'serqet', 'skadi', 'sobek',
             'sol', 'sun wukong', 'susano', 'sylvanus', 'terra', 'thanatos',
             'the morrigan', 'thor', 'thoth', 'tyr', 'ullr', 'vamana', 'vulcan',
             'xbalanque', 'xing tian', 'ymir', 'zeus', 'zhong kui']
    
    roleList =['mid', 'solo', 'jungle', 'support', 'adc']
    
    print('Please input the name of the god you wish to play.')
    godChoice = input().lower()
    if godChoice in smiteGods:
        print('Your god will be chosen.')
        print('Please input the role you wish to call.')
        print('For the list of accepted roles please input 1')
        roleChoice = input().lower()
        if roleChoice in roleList:
            print('Your role will be called.')
            pass
        
        elif roleChoice == '1':
            print('\n')
            print(*roleList, sep=', ')
            print('\n')
            autoGod()

        else:
            print('Please re-enter your god and then enter a valid role.')
            print('\n')
            autoGod()

    else:
        print('Please re-enter the god name with correct spelling.')
        print('\n')
        autoGod()
    
    while True:
        if pyautogui.locateOnScreen('accept.png') is None:
            pass

        else:
            acceptButtonLocation = pyautogui.locateOnScreen('accept.png')
            acceptX, acceptY = pyautogui.center(acceptButtonLocation)
            time.sleep(22)
            pyautogui.click(acceptX, acceptY)
            time.sleep(2)
            pyautogui.click(x=277, y=1044, button='left', clicks=1)
            pyautogui.typewrite(roleChoice)
            pyautogui.press('enter')
            pyautogui.click(x=736, y=219, button='left', clicks=1)
            pyautogui.typewrite(godChoice)
            time.sleep(3)
            pyautogui.click(x=507, y=292, button='left', clicks=1, interval=5)
            pyautogui.click(x=1592, y=965, button='left', clicks=1, interval=5)


def autoAccept():
    while True:
        if pyautogui.locateOnScreen('accept.png') is None:
            autoAccept()

        else:
            acceptButtonLocation = pyautogui.locateOnScreen('accept.png')
            acceptX, acceptY = pyautogui.center(acceptButtonLocation)
            pyautogui.click(acceptX, acceptY)
        
        # pyautogui.click(x=943, y=666, button='left', clicks=1)
        # time.sleep(10)

def start():
    choice = input()
    if choice == '1':
        autoAccept()

    if choice == '2':
        autoGod()

    else:
        print('Please input either 1 or 2')
        start()

print('Welcome to Smite Helper')
print('To automatically accept a match for you please input 1')
print('To automatically accept a match, and choose a god for you please input 2')
start()
