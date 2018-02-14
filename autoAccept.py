import pyautogui

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
    print('Please input the name of the god you wish to play.')
    print('Without spelling mistakes.')
    print('In all lower case.')
    godChoice = input()
    if godChoice in smiteGods:
        print('Your god will be chosen.')

    else:
        print('Please re-enter the god name with correct spelling.')

    print('Press Ctrl-C to quit once your god has been chosen.')
    try:
        while True:
            acceptX, acceptY = pyautogui.locateCenterOnScreen('accept.png')
            pyautogui.click(acceptX, acceptY)
            pyautogui.click(button='left', clicks=1, interval=15)
            lockInX, lockInY = pyautogui.locateCenterOnScreen('lock_in.png')
            pyautogui.click(lockInX, lockInY)
    except KeyboardInterrupt:
        print('Program stopped.')

def autoAccept():
    print('Press Ctrl-C to quit once your game has been accepted.')
    try:
        while True:
            pyautogui.click(x=943, y=666, clicks=1, interval=10, button='left')
    except KeyboardInterrupt:
        print('Program stopped.')


        

print('Welcome to Smite Helper')
print('To launch the game for you please input 1')
print('To automatically accept a match for you please input 2')
print('To automatically accept a match, and choose a god for you please input 3')
choice = input()

if choice == '1':
    gameLaunch()

if choice == '2':
    autoAccept()

if choice == '3':
    autoGod()
