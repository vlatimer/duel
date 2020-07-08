import random
shield = 0
print('             Welcome to Duel')
print('             Input your age')
first_input = input()
tmp = 0
if first_input == 'cheat_shield':
    shield = 5
    age = 100
else:
    age = int(first_input)
print('             Enter your and computer lives')
lives_you = int(input())
if lives_you <= 0:
    tmp = -1
lives_computer = lives_you
while lives_you != 0 or lives_computer != 0:
    if lives_you == -123:
        break
    if age <= 5:
        print('           ---------------------------------')
        print('           |  Choose where will you shoot   |')
        print('           |             One or Two         |')
        print('           ---------------------------------')
        number = int(input())
        answer = random.randint(1,2)
        if number == answer:
            print('--------------------------------------------')
            print('             YOU HIT TNE ENEMY')
            lives_computer -= 1
            print('             lives computer =',lives_computer)
            print('--------------------------------------------')
            if lives_computer == 0:
                break
        elif number >= 3:
            break
        else:
            print('--------------------------------------------')
            print('             You Miss')
            print('             lives computer =',lives_computer)
            print('--------------------------------------------')
        print(' ')
        print('           ---------------------------------')
        print('           |  Choose where will you Hide    |')
        print('           |         One or Two             |')
        print('           ---------------------------------')
        Hide = int(input())
        shoot = random.randint(1,2)
        if Hide == shoot:
            print('--------------------------------------------')
            print('             THE COMPUTER HIT YOU')
            lives_you -= 1
            print('             Your lives =',lives_you)
            print('--------------------------------------------')
            print('')
            if lives_you == 0:
                break
        elif Hide >= 3:
            break
        else:
            print('--------------------------------------------')
            print('             The computer did not hit you')
            print('--------------------------------------------')
            print(' ')
    elif age <= 15 and age >= 6:
        print('        ----------------------------------')
        print('        |    Choose where will you shoot  |')
        print('        |        One or Two or Tree       |')
        print('        ----------------------------------')
        number = int(input())
        answer = random.randint(1,3)
        if number == answer:
            print(' ')
            print('------------------------------------------')
            print('             YOU HIT TNE ENEMY')
            lives_computer -= 1
            print('             lives computer =',lives_computer)
            print('------------------------------------------')
            if lives_computer == 0:
                break
        elif number >= 4:
            break
        else:
            print('------------------------------------------')
            print('             You Miss')
            print('             lives computer =',lives_computer)
            print('------------------------------------------')
        print(' ')
        print('        ----------------------------------')
        print('        |    Choose where will you Hide   |')
        print('        |        One or Two or Tree       |')
        print('        ----------------------------------')
        Hide = int(input())
        shoot = random.randint(1,3)
        if Hide == shoot:
            lives_you -= 1
            print('------------------------------------------')
            print('             THE COMPUTER HIT YOU')
            print('             Your lives =',lives_you)
            print('------------------------------------------')
            print('')
            if lives_you == 0:
                break
        elif Hide >= 4:
            break
        else:
            print('------------------------------------------')
            print('             The computer did not hit you')
            print('------------------------------------------')
            print(' ')
    else:        
        print('        -------------------------------------')
        print('        |     Choose where will you shoot    |')
        print('        | One or Two or Tree or Four or Five |')
        print('        -------------------------------------')
        number = int(input())
        answer = random.randint(1,5)
        if number == answer:
            print(' ')
            print('------------------------------------------')
            print('             YOU HIT TNE ENEMY')
            lives_computer -= 1
            print('             lives computer =',lives_computer)
            print('------------------------------------------')
            if lives_computer == 0:
                break
        elif number >= 6:
            break
        else:
            print('------------------------------------------')
            print('             You Miss')
            print('             lives computer =',lives_computer)
            print('------------------------------------------')
        print(' ')
        print('        -------------------------------------')
        print('        |     Choose where will you Hide     |')
        print('        | One or Two or Tree or Four or Five |')
        print('        -------------------------------------')
        Hide = int(input())
        shoot = random.randint(1,5)
        if Hide == shoot:
            if shield != 0:
                shield -= 1
                print('------------------------------------------')
                print('             THE COMPUTER HIT YOU')
                print('             Your shields =',shield)
                print('             Your lives =',lives_you)
                print('------------------------------------------')
                print('')
            else:
                lives_you -= 1
                print('------------------------------------------')
                print('             THE COMPUTER HIT YOU')
                print('             Your lives =',lives_you)
                print('------------------------------------------')
                print('')
                if lives_you == 0:
                    break
        elif Hide >= 6:
            break
        else:
            print('------------------------------------------')
            print('             The computer did not hit you')
            print('------------------------------------------')
            print(' ')
if lives_computer == 0 and tmp == 0:
    print(' ')
    print('        ++++++++++++++++++++++++++++++++')
    print('         !!!!! You win the Game !!!!!')
    print('        ++++++++++++++++++++++++++++++++')
elif lives_you == 0 and tmp == 0:
    print(' ')
    print('             You Lost')
else:
    print('ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR')
    print('-----------------------------------------------------------------------------------')
    print(' ')
    print('the game is over, you wanted to cheat, it is not according to the rules of the game')
    print(' ')
    print('-----------------------------------------------------------------------------------')
    print('ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR')