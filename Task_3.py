# Создайте программу для игры с конфетами
from random import randint

def candy (candy_ost, candy_take):
    print ('Кто последний заберет конфеты, тот -  выиграл!\n')
    count = 0 
    curr_player_turn = 0
    flag = True
    flag1 = 0
    
   
    print (f"Кол конфет в кучке: {candy_ost}, можно взять от 1 до {candy_take} конф.\n")
    while True:
        count += 1
        if candy_ost <= candy_take:
            print (f"Ход №{count} от БОТА: взял {candy_ost} конф., БОТ ПОБЕДИЛ!!!\n")
            break

        if count == 1 :                                                             
            turn = randint(1, candy_take)
            flag = False
            candy_ost -= turn
            print (f"Ход №{count} от БОТА: взял {turn} конф. В кучке {candy_ost} конф.")    

        else:
            if candy_ost % (candy_take + 1) != 0:
                flag = True   
                if flag1 == 0:                                                               
                    print ("---ВЫ ОШИБЛИСЬ! БОТ МЕНЯЕТ СТРАТЕГИЮ, НАЧИНАЕТ ВЫИГРЫВАТЬ----\n")
                    flag1 += 1
            turn = candy_ost % (candy_take + 1) if flag == True else randint(1, candy_take)
            candy_ost -= turn
            flag1 = False
            print (f"Ход №{count} от БОТА: взял {turn} конф. В кучке {candy_ost} конф.")
        
        count += 1
        if (flag == True):
            print (f"Введите количество конф. ")
        else:
            print (f"Введите количество конф. Чтобы выиграть надо взять: {candy_ost % (candy_take + 1)} конф.")
        curr_player_turn = int (input())
        
        while curr_player_turn < 1 or  curr_player_turn > candy_take:
            print (f'Количество конфет должно быть от 1 до {candy_take}  повторите ввод: ')
            curr_player_turn = int (input())
            
        candy_ost -= curr_player_turn

        if candy_ost == 0:
            print ("ВЫ ПОБЕДИЛИ!")
            break
        else:
            print (f" Ход №{count} от игрока: берет {curr_player_turn}  конф. В кучке {candy_ost} конф. \n")
           
candy (int (input ('введите исходное кол конфет: ')), int (input ('введите макс кол конфет, которое можно взять: ')))