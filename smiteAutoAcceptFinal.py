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
    roleList =['mid', 'Mid', 'solo', 'Solo', 'jungle', 'Jungle', 'jng', 'support',
               'Support', 'supp', 'adc', 'hunter',' Hunter']
    print('Please input the name of the god you wish to play.')
    print('Without spelling mistakes.')
    print('In all lower case.')
    godChoice = input()
    if godChoice in smiteGods:
        print('Your god will be chosen.')
        print('Please input the role you wish to call.')
        roleChoice = input()
        if roleChoice in roleList:
            print('Your role will be called.')

        else:
            print('Please re-enter you god and then enter a valid role.')
            autoGod()

    else:
        print('Please re-enter the god name with correct spelling.')
        autoGod()

    print('Press Ctrl-C to quit once your god has been chosen.')
    while True:
        try:
            while True:
                acceptX, acceptY = pyautogui.locateCenterOnScreen('accept.png')
                pyautogui.click(acceptX, acceptY)
                pyautogui.click(x=277, y=1044, button='left', clicks=1)
                pyautogui.typewrite(roleChoice)
                pyautogui.click(x=736, y=219, button='left', clicks=1, interval=5)
                pyautogui.typewrite(godChoice) 
                pyautogui.click(x=507, y=292, button='left', clicks=1, interval=5)
                lockInX, lockInY = pyautogui.locateCenterOnScreen('lock_in.png')
                pyautogui.click(lockInX, lockInY)
        except TypeError:
            pass

def autoAccept():
    print('Press Ctrl-C to quit once your game has been accepted.')
    acceptX = 2001
    acceptY = 2001
    while True:        
        try:
            acceptX, acceptY = pyautogui.locateCenterOnScreen('accept.png')
            pyautogui.click(acceptX, acceptY)

        except TypeError:
            autoAccept()

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

