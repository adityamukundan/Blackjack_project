m = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
def display_board(position,value):                    # method to display the board
    n = {}
    list1 = [1,2,3,4,5,6,7,8,9]
    for x in list1:
        if position == x:
            n[x] = value
    m.update(n)
   # print(n)
    print('\t|   \t|   \t')
    print('  {}\t|   {}  \t|    {} \t'.format(m[1],m[2],m[3]))
    print('\t|   \t|   \t')
    print('---------------------------')
    print('\t|   \t|   \t')
    print('  {}\t|   {}  \t|    {}  \t'.format(m[4],m[5],m[6]))
    print('\t|   \t|   \t')
    print('---------------------------')
    print('\t|   \t|   \t')
    print('  {}\t|   {}  \t|    {}  \t'.format(m[7],m[8],m[9]))
    print('\t|   \t|   \t')
def game_logic_1():                       # logic for diagonal positions 1,5,9
    win_count_x = 0
    win_count_0 = 0
    for x in range(1,10,4):
        if m[x] == 'x' and m[x] != '0':
            win_count_x += 1
        if m[x] == '0' and m[x] != 'x':
            win_count_0  += 1
    if win_count_x == 3:
        return win_count_x
    elif win_count_0==3:
        return win_count_0
def game_logic_2():                    #logic for diagonal positions 3,5,7
    win_count_1_x = 0
    win_count_1_0 = 0
    for z in range(3,10,3):
        if m[z] == 'x':
            win_count_1_x += 1
        if m[z] == '0':
            win_count_1_0 += 1
    if win_count_1_x == 3:
        return win_count_1_x
    elif win_count_1_0 == 3:
        return win_count_1_0
def game_logic_3():                    #logic for vertical postions 3,6,9
    win_count_3_x = 0
    win_count_3_0 = 0
    for f in range(3,8,2):
        if m[f] == 'x':
            win_count_3_x += 1
        if m[f] == '0':
            win_count_3_0 += 1
    if win_count_3_x == 3:
        return win_count_3_x
    elif win_count_3_0 == 3:
        return win_count_3_0
def game_logic_4():                    #logic for vertical positions 2,4,6
    win_count_4_x = 0
    win_count_4_0 = 0
    for z in range(2,10,3):
        if m[z] == 'x':
            win_count_4_x += 1
        if m[z] == '0':
            win_count_4_0 += 1
    if win_count_4_x == 3:
        return win_count_4_x
    elif win_count_4_0 == 3:
        return win_count_4_0
def game_logic_5():                    #logic for vertical positions 1,4,7
    win_count_5_x = 0
    win_count_5_0 = 0
    for z1 in range(1,10,3):
        if m[z1] == 'x':
            win_count_5_x += 1
        if m[z1] == '0':
            win_count_5_0 += 1
    if win_count_5_x == 3:
        return win_count_5_x
    elif win_count_5_0 == 3:
        return win_count_5_0
def game_logic_6():
    win_count_6_x = 0
    win_count_6_0 = 0
    for y1 in range(1,4):             #logic for horizontal rows 1,2,3
        if m[y1] == 'x':
            win_count_6_x += 1
        if m[y1] == '0':
            win_count_6_0 += 1
    if win_count_6_x == 3:
        return win_count_6_x
    elif win_count_6_0 == 3:
        return win_count_6_0
def game_logic_7():
    win_count_7_x = 0
    win_count_7_0 = 0
    for y1 in range(4,7):             #logic for horizontal rows 4,5,6
        if m[y1] == 'x':
            win_count_7_x += 1
        if m[y1] == '0':
            win_count_7_0 += 1
    if win_count_7_x == 3:
        return win_count_7_x
    elif win_count_7_0 == 3:
        return win_count_7_0
def game_logic_8():
    win_count_8_x = 0
    win_count_8_0 = 0
    for y1 in range(7,10):             #logic for horizontal rows 7,8,9
        if m[y1] == 'x':
            win_count_8_x += 1
        if m[y1] == '0':
            win_count_8_0 += 1
    if win_count_8_x == 3:
        return win_count_8_x
    elif win_count_8_0 == 3:
        return win_count_8_0
def player_input_1():
    count = 0
    reset_list_1 = [1,2,3,4,5,6,7,8,9]
    reset_1 = 0
    i=1
    v2 = None
    v1 = input('Player1 do you want to be x or 0:')
    if v1 == 'x':
        v2 = '0'
    else:
        v2 = 'x'
        v1 = '0'
        print('Player1 is: %s and player2 is:  %s' %(v1,v2))
    while(i < 10):
        try:
            p1 = int(input('player1 please input the player position'))     #try block to make remove null entry on positions
        except ValueError:
            print('Input a number !')
            continue
        if m[p1] == v2:                                             # for  preventing re entry on  already entered positons
            print('Slot already taken ,chose another slot')
            continue
 #       v1 = input('Please input the marker')
        display_board(p1,v1)                                    # showing display board after the player enters the value
 #       if v1 == '':
 #           print('enter a marker !!')
 #           continue
        count += 1
        if count == 9:
 #           print('all positions are occupied ')
            break
        win  = game_logic_1()
        win1 = game_logic_2()
        win3 = game_logic_3()
        win4 = game_logic_4()
        win5 = game_logic_5()
        win6 = game_logic_6()
        win7 = game_logic_7()
        win8 = game_logic_8()
 #       print(win)
        if win or win1 or win3 or win4 or win5 or win6 or win7 or win8 == 3: # calling game logic and declaring winner
            print('player1 is the winner')
            for reset_1 in reset_list_1: # loop to reset the dictionary to null values for player to continue the game
                m[reset_1] = ''
            break
#        print(m)
        try:
             p2 = int(input('Player2 please input the player position')    #try block to make remove null entry on positions
        except ValueError:
            print('Input a number !')
            continue
        if m[p2] == v1:                  # for  preventing re entry on  already entered positons
            print('Slot already taken ,chose another slot')
            continue
 #       v1 = input('Please input the marker')
        display_board(p2,v2)                   # showing display board after the player enters the value
 #       if v1 == '':
 #           print('enter a marker !!')
 #           continue
        count += 1
        if count == 9:
 #           print('all positions are occupied ')
            break
 #       print(count)
        win  = game_logic_1()
        win1 = game_logic_2()
        win3 = game_logic_3()
        win4 = game_logic_4()
        win5 = game_logic_5()
        win6 = game_logic_6()
        win7 = game_logic_7()
        win8 = game_logic_8()
 #       print(win)
        if win or win1 or win3 or win4 or win5 or win6 or win7 or win8 == 3:    # calling game logic and declaring winner
            print('player2 is the winner')
            for reset_1 in reset_list_1:    # loop to reset the dictionary to null values for player to continue the game
                m[reset_1] = ''
            break
#        print(m)