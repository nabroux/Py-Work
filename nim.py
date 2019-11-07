import random
desk={'A':'3','B':'5','C':'7'}
# ~ print(desk)
bad_str = '100 500 220 330 140 260 370 540 144 224 246 334 347 111 115 155 356 136 235 257 123 127'.split()
pattern = 'O '
bad = [{'0':2,'1':1},{'0':2,'5':1},{'0':1,'2':2},{'0':1,'3':2},{'1':1,'4':2},{'1':2,'5':1},{'1':1,'5':2},{'3':2,'4':1},\
    {'1':3},{'0':1,'1':1,'4':1},{'0':1,'2':1,'6':1},{'0':1,'3':1,'7':1},{'0':1,'4':1,'5':1},{'2':1,'4':1,'6':1},\
    {'3':1,'4':1,'7':1},{'3':1,'5':1,'6':1},{'1':1,'3':1,'6':1},{'2':1,'3':1,'5':1},{'2':1,'5':1,'7':1},{'1':1,'2':1,'3':1},{'1':1,'2':1,'7':1}]

def show_info():
    print()
    for d,dn in desk.items():
        if int(dn) >1:
            print('plate '+d+' has '+dn+' stones.')
        else:
            print('plate '+d+' has '+dn+' stone.')
        print((pattern+' ')*int(dn))
    print()

def AI_move():
    print()
    current_stn = list(desk.values())
    current_dict = {}
    possibles = []
    for stn in current_stn:
        if stn not in current_dict:
            n = current_stn.count(stn)
            current_dict[stn] = n
    
    for b in bad:
        count = 0
        b_left = b.copy()
        current_dict_left = current_dict.copy()
        for stn in current_dict:
            if stn in b:
                if current_dict[stn] == b[stn]:
                    count += b[stn]
                    b_left[stn] -= b[stn]
                    current_dict_left[stn] -= b[stn]
                else:
                    count += min(current_dict[stn],b[stn])
                    b_left[stn] -= min(current_dict[stn],b[stn])
                    current_dict_left[stn] -= min(current_dict[stn],b[stn])
                if b_left[stn] == 0:
                    del b_left[stn]
                if current_dict_left[stn] == 0:
                    del current_dict_left[stn]
            
        if count == 2:
            # ~ print(b,b_left,current_dict_left)
            b_new=dict([val,key] for key,val in b_left.items())
            current_dict_new=dict([val,key] for key,val in current_dict_left.items())
            b_new = b_new[1]
            current_dict_new = current_dict_new[1] 
            if int(current_dict_new)-3 <= int(b_new) < int(current_dict_new):
                # ~ print(current_dict_new,'->',b_new)
                possibles.append([current_dict_new,b_new])
    # ~ print(possibles)
    if len(possibles)!=0:
        move = random.choice(possibles)
    else:
        dn = list(desk.values())
        move = [max(dn),str(int(max(dn))-1)]
    
    for plate,stones in desk.items():
        if stones == move[0]:
            desk[plate] = move[1]
            print("-----------AI's TURN-------------!")
            print('AI took',int(move[0])-int(move[1]),'stones from plate',plate)
            show_info()
            break

print('0為太陽,1為愛心,2為太極,3為星星,4為骷髏,5為雪片,6為笑臉,7為音符,8為輻射,9為飛機')
p_index = int(input('請選擇石頭款式: '))
p_list = ['☀ ','♡ ','☯ ','★ ','☠ ','❄ ','☺ ','♫ ','☢ ','✈']
pattern = p_list[p_index]

show_info()
while True:
    #choose plate
    while True:
        print()
        plate = input('which plate? ')
        if plate in desk:
            if desk[plate] != '0':
                break
            else:
                print('there is no stone')
        else:
            print('please enter A or B or C')
    
    #choose number
    while True:
        print()
        take_num = int(input('how many? '))
        if 3>= take_num >=1:
            if int(desk[plate]) >= take_num:
                desk[plate] = str(int(desk[plate])-take_num)
                break
            else:
                print('wrong')
        else:
            print('please enter 1~3')
    
    current_sum = sum([int(i) for i in desk.values()])
    if current_sum != 0:
        print('-----------YOUR TURN-------------!')
        print('You took',take_num,'stones from plate',plate)
        show_info()
        AI_move()
        current_sum = sum([int(i) for i in desk.values()])
        if current_sum == 0:
            print('-----------YOU WIN-------------!')
            break
    else:
        print('-----------YOU LOSE-------------!')
        break
