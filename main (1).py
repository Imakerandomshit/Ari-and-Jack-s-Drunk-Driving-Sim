import time
import random
import math
#Variable reset
start_time = time.time()
drunk_lvl = 0
money = 100000
turns = 0
hunger = 99
points = 0
aura = 50
net_worth = money
crimes_commited = 0
money_achievement = 0
continue_car_steal = False
user_car = 'old Toyota Corolla'
correct_gog = 0
lunchly_found = False
#All options
all_scenarios = ['A Bus of school kids is making an illegal turn across the highway.  What do you do?',
'There is a prison on the left side of the road. Fire is coming from the inside, and it looks like a major riot is taking place. What do you do?',
'The car in front of you honks at you and swerves in front of you, causing you to slam the brakes. What do you do?',
'There is a massive traffic jam extending for kilometres, and you’ll never make it to the front…normally. What do you do?',
'You are at a red light and the man in the car next to you rolls down his window and signals for a race. What do you do?',
'You stop at zebra crossing and a poor, disabled old lady falls out of her wheelchair right in front of your car. What do you do?',
'A homeless man begins to clean your windshield and holds up a piece of cardboard asking for money at a red light. All of a sudden, the light turns green and he doesn’t move. What do you do?',
'A giant spider drops down onto your car’s windshield. It looks angry, and out for blood. What do you do?',
'A bald man walks deliberately out in front of your car. He is an insurance scammer and wants to take your money. What do you do?',
'While driving, you see a woman and her two children with all of their luggage, and a broken-down car, holding up a sign saying ‘Help we’re stuck!’. What do you do?']
def stats():
  print()
  print("=-=-=-=-=-=-STATS=-=-=-=-=-=-=")
  if hunger >= 100:
    print(f"Hunger ------------------- 100% (Dead)")
  else:
    print(f"Hunger ------------------- {hunger}%")
  print(f"Drunk Level -------------- {drunk_lvl}")
  print(f"Money -------------------- ${money}.00")
  print(f'Net worth ---------------- ${net_worth}.00')
  print(f'Crimes commited ---------- {crimes_commited}')
  print(f"Aura --------------------- {aura}")
  elapsed_time = round(time.time() - start_time, 2)
  time_minutes = math.trunc(elapsed_time / 60)
  time_seconds = int(round(elapsed_time))
  seconds_minus_minutes = time_seconds - (time_minutes * 60)
  if time_seconds < 60:
    print(f"Time lasted -------------- {time_minutes} minutes and {time_seconds} seconds")
  else:
    print(f"Time lasted ------------- {time_minutes} minutes and {seconds_minus_minutes} seconds")

def aura_reset():
  global aura
  if aura < 0:
    time.sleep(1)
    print('You now have negative aura!!')
  elif aura > 100:
    aura = 100
  time.sleep(1)
  print(f'You now have {aura}% aura.')
  time.sleep(1)

def hunger_reset():
  global hunger
  if hunger < 0:
    hunger = 0
  time.sleep(1)
  print(f'Your hunger level is now {hunger}%.\n')
  time.sleep(1)

def hunger_end():
  global hunger
  if hunger >= 100:
    time.sleep(1)
    print('\nYou have reached 100% hunger...\n')
    time.sleep(3)
    print('You were too busy drinking, driving and possibly commiting crime.')
    time.sleep(3)
    print('You die a terrible, slow and hungry death...')
    time.sleep(5)
    print('\nThanks for playing!\n')
    time.sleep(3)
    stats()
    exit()
def money_reset():
  global money
  if money < 0:
    money = 0
  time.sleep(1)
  print(f'You now have ${money}.00')
  time.sleep(1)

def achievements():
  print("=-=-=-=-=-=-ACHIEVEMENTS=-=-=-=-=-=-=")
  if money_achievement == 1:
    print('1. Rags To Riches')
  else:
    print('1. ACHIEVEMENT LOCKED')
  confirm_achievement = int(input("What Achievement would you like to view? "))  
  if confirm_achievement == 1:
    print('Rags To Riches\nEarn your first 100 dollars.')
  elif confirm_achievement == 2:
    print('Grand Theft Auto\nSteal a car.')
print("Welcome to Ari and Jack's Drunk Driving Simulator!")
time.sleep(1)
print("You start at the gas station.")
time.sleep(1)
print("This is the main menu: ")
time.sleep(1)


while True:
  if money_achievement == 0:
    if money >= 100:
      money_achievement = 1
      print('You have earned a new achievement.\n')

  if turns % 5 == 0:
      print()
      print("=-=-=-=-=-=-MAIN MENU=-=-=-=-=-=-=")
      if drunk_lvl == 0:
        print('1. Drink')
      else:
        print(f'1. Drink (Drunk level: {drunk_lvl})')
      if hunger >= 80:
        print(f'2. EAT!! (HUNGER: {hunger}%!)')
      elif hunger == 0:
        print('2. Eat')
      else:
        print(f'2. Eat (Hunger: {hunger}%)')
      print("3. Commit 'Silly stuff'")
      print('4. Leave the station')
      print('5. Resist your urges and quit the game')
      print('6. Check your stats')
      print('7. Check your achievements')
      print()
      option = int(input("What would you like to do? "))
      print()

      if option == 1:
        if money >= 8:
          time. sleep(0.5)
          print("=-=-=-=-=-=-DRINK MENU=-=-=-=-=-=-=")
          print("1. Beer --------- $8.00")
          print("2. Cheap wine --- $12.00")
          print("3. Tequila ------ $15.00")
          print("4. Rum ---------- $20.00")
          print('5. Gin ---------- $25.00')
          print('6. 75% Vodka ---- $45.00')
          print('7. 95% VODKA ---- $120.00')
          print('8. GLASS OF GOLD  $2000.00')
          print('9. Exit')
          print()
          print(f'You have ${money}.00')
          drink_option = int(input("What drink would you like to purchase? "))
          if drink_option == 1:
            #Beer purchased?
            if money >= 8:
              money -= 8
              drunk_lvl += 10
              print('\nYou purchased a beer and increased your drunk level by 10!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}.')
              time.sleep(1)
            else:
              print('You are too poor.')
          elif drink_option == 2:
            #Cheap wine purchased?
            if money >= 15:
              money -= 15
              drunk_lvl += 20
              print('\nYou purchased cheap wine and increased your drunk level by 20!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}.')
              time.sleep(1)
            else:
              print('You are too poor.')
          elif drink_option == 3:
            #Tequila purchased?
            money -= 15
            drunk_lvl += 30
            print('\nYou purchased tequila and increased your drunk level by 30!')
            time.sleep(1)
            print(f'You now have ${money}.00')
            time.sleep(1)
            print(f'Your drunk level is now {drunk_lvl}.')
            time.sleep(1)
          elif drink_option == 4:
            #Rum purchased?
            if money >= 20:
              money -= 20
              drunk_lvl += 40
              print('\nYou purchased rum and increased your drunk level by 40!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}.')
              time.sleep(1)
            else:
              print('You are too poor.')
          elif drink_option == 5:
          #Gin purchased?
            if money >= 25:
              money -= 25
              drunk_lvl += 50
              print('\nYou purchased gin and increased your drunk level by 50!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}.')
              time.sleep(1)
            else: 
              print('You are too poor.')
          elif drink_option == 6:
          #75% vodka purchased?
            if money >= 45:
              money -= 45
              drunk_lvl += 75
              print('\nYou purchased 75% vodka and increased your drunk level by 75!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}.')
              time.sleep(1)
          elif drink_option == 7:
          #95% vodka purchased?
            if money >= 120:
              money -= 120
              drunk_lvl += 150
              print('\nYou purchased 95% vodka and increased your drunk level by 150!!!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}.')
              time.sleep(1)
            else:
              print('You are too poor.')
          elif drink_option == 8:
          #GLASS OF GOLD purchased?
            if money >= 2000:
              money -= 2000
              print('Y-y-you...')
              time.sleep(3)
              print('You did the unthinkable!!')
              time.sleep(3)
              print('\nYou purchased THE GLASS OF GOLD!!!')
              print()
              time.sleep(3)
              print('You slowly feel the effects taking over...')
              time.sleep(3)
              print('You stumble out of the gas station...')
              time.sleep(3)
              print('You can barely see straight, everything is a blur...')
              time.sleep(3)
              print("It's too much...")
              print()
              time.sleep(5)
              print('You fall onto the hard, unforgiving, concrete pavement')
              time.sleep(3)
              print()
              print("Intoxicated, tired, there's nothing you can do but lie there.")
              time.sleep(3)
              print('The last thing you see is the gloomy, cloudy sky. Your eyes close. Pernamently...')
              time.sleep(5)
              print()
              print('Thanks for playing!')
              time.sleep(3)
              stats()
              exit()
            else:
              print('You are too poor.')
          else: 
            print("That isn't an option. Pick again!")
        else: 
          print('You are too poor.') 
      elif option == 2:
        if money >= 2:
          print("=-=-=-=-=-=-FOOD MENU=-=-=-=-=-=-=")
          print("1. Mars bar ------------- $2.00")
          print("2. Chippy chips --------- $5.00")
          print("3. Bucket of cheese balls $10.00")
          print("4. Fish and chips ------- $15.00")
          print("5. Full english breakfast $25.00")
          print("6. Headache pills ------- $100.00")
          print("7. SLAB OF NUTRITION ---- $100.00")
          print("8. Exit")
          print(f'\nYou have ${money}.00')
          if hunger >= 50 and hunger < 80:
           print(f'Your hunger level is {hunger}%. You should eat.')
          elif hunger >= 80:
            print(f'YOUR HUNGER LEVEL IS {hunger}%!! EAT QUICK!!')
          elif hunger <= 10:
            print(f"Your hunger level is only {hunger}%. You don't need to eat.")
          else:
            print(f'Your hunger level is {hunger}%.')
          time.sleep(1)
          food_option = int(input('What food would you like to purchase? '))
          if food_option == 1:
            #Mars bar purchased?
            if money >= 2:
              money -= 2
              hunger -= 5
              print('\nYou purchased a Mars bar!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              hunger_reset()
          elif food_option == 2:
            #Chippy chips purchased?
            if money >= 5:
              money -= 5
              hunger -= 10
              print('\nYou purchased Chippy chips!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              hunger_reset()
          elif food_option == 3:
            #Bucket of cheese balls purchased?
            if money >= 10:
              money -= 10
              hunger -= 15
              print('\nYou purchased a bucket of cheese balls!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              hunger_reset()
          elif food_option == 4:
            #Fish and chips purchased?
            if money >= 15:
              money -= 15
              hunger -= 20
              print('\nYou purchased fish and chips!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              hunger_reset()
          elif food_option == 5:
            #Full english purchased?
            if money >= 25:
              money -= 25
              hunger -= 25
              print('You purchased a full english breakfast!')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              hunger_reset()
          elif food_option == 6:
            #Headache pills purchased?
            if money >= 100:
              money -= 100
              drunk_lvl -= 100
              if drunk_lvl < 0:
                drunk_lvl = 0
              print('You a consumed headache pills.')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}.')
              time.sleep(1)
            else:
              print('You are too poor.')
          elif food_option == 7:
            #SLAB OF NUTRITION purchased?
            if money >= 100:
              money -= 100
              hunger -= 100
              print('\nYou purchased the SLAB OF NUTRITION.')
              time.sleep(1)
              print(f'You now have ${money}.00')
              time.sleep(1)
              hunger_reset()
              time.sleep(1)
            else:
              print('You are too poor.')
          elif food_option == 8:
            print('\nYou decide not to eat anything.')
            time.sleep(1)
          elif food_option == 69:
            #Secret mouldy Lunchly
            if lunchly_found == False:
              print('\nYou found a secret!')
              time.sleep(3)
              lunchly_purchased = input('Would you like to buy mouldy Lunchly for $50? ')
              if lunchly_purchased.lower() in ['y','yes']:
                if money >= 50:
                  lunchly_found = True
                  print('\nYou bought mouldy Lunchly! (I like my cheese mouldy bruh)')
                  time.sleep(2)
                  money_reset()
                  time.sleep(2)
                  print('\nYou take a bite of the mouldy, drippy cheese...')
                  time.sleep(3)
                  print("\n'This is fire!' You say.")
                  time.sleep(3)
                  print('You gain 25 aura!')
                  aura += 25
                  time.sleep(2)
                  aura_reset()
                  time.sleep(2)
                  print('\nBut wait...Lunchly discountinued.')
                  time.sleep(3)
                  print('You can only have mouldy Lunchly once.')
                  time.sleep(3)
                else:
                  print("\nYou're too poor to buy mouldy Lunchly.")
              else:
                print('\nAlright, no mouldy lunchly for you...')
            else:
              print('\nYou really tried to get more mouldy Lunchly?')
              time.sleep(3)
              print('You lost 10 aura.')
              aura -= 10
              aura_reset()
      if option == 5:
        #'Leave' and secret game
        elapsed_time = round(time.time() - start_time, 2)
        print("I'm impressed. You did it. You left this horrible cycle of intoxication and depression. Good on you, you took the easy way out.") 
        time.sleep(3)
        elapsed_time = round(time.time() - start_time, 2)
        time_minutes = math.trunc(elapsed_time / 60)
        time_seconds = int(round(elapsed_time))
        seconds_minus_minutes = time_seconds - (time_minutes * 60)
        if time_seconds < 60:
          print(f"You lasted {time_minutes} minutes and {time_seconds} seconds.")
        else:
          print(f"You lasted {time_minutes} minutes and {seconds_minus_minutes} seconds.")
        time.sleep(10)
        print()
        print("JUST KIDDING, DAMN YOUUUU!!!!!!!! DRINKING AND DRIVING IS WHAT WE'RE BORN FOR BABBYYY!!!! I'M GLAD YOU'RE OUT OF HERE!!!!!")
        time.sleep(10)
        print()
        print('Wow...still here huh? Weirdo...')
        time.sleep(10)
        print("Alright fine, here's the deal. Wait here longer and I'll give you something really special.")
        time.sleep(30)
        print('Hold on...let me just get it...')
        print()
        time.sleep(60)
        print('Here it is! 1 point.')
        time.sleep(3)
        points += 1
        print(f'You now have {points} points.')
        time.sleep(3)
        while True:
          print()
          print("=-=-=-=-=-=-SECRET MENU=-=-=-=-=-=-=")
          print("1. Get another point")
          print("2. Leave FOR GOOD.")
          secret_menu_option = int(input('What would you like to do? '))
          if secret_menu_option == 1:
            print('There you go...another point.')
            points += 1
            print(f'You now have {points} points.')
          elif secret_menu_option == 2:
            print('Okay fine...bye.')
            time.sleep(3600)
            print('THERE IS NO WAY THAT YOU WAITED...A WHOLE HOUR!!!!!!!!!!')
            time.sleep(3)
            print('YOU ARE INSANE!!!!!!!!')
            print('Okay...this is actually it (I promise you)')
            exit()
          else:
            print('DEFY ME?????')
            time.sleep(3)
            print('*Beats your limbs with a metal bat, over and over again.*')
            time.sleep(3)
            print('You die. Better luck next time!')
            exit()
      if option == 6:
        stats()
      if option == 3:
        print("=-=-=-=-=-=-CRIME MENU=-=-=-=-=-=-=")
        print("1. Pickpocket somebody")
        print("2. Rob the cashier")
        print("3. Rob the shop")
        print("4. Rob a car")
        print("5. Start a fight")
        print("6. Exit\n")
        crime_option = int(input('What crime would you like to commit? '))
        print()
        time.sleep(0.5)
        if crime_option == 1:
          hunger += 5
          crimes_commited += 1
          pickpocket_victim_list1 = ['n innocent old lady',' tall, bald man',' young child',' mother with her baby', ' programmer']
          pickpocket_victim_list2 = ['n obnoxious french man',' teen eshay',' crazy Trump supporter',' terrorist',' climate activist']
          pickpocket_victim_list3 = [' nerd wearing glasses',' minor celebrity',' generic man',' homeless man',' feminist']
          pickpocket_victim1 = random.choice(pickpocket_victim_list1)
          pickpocket_victim2 = random.choice(pickpocket_victim_list2)
          pickpocket_victim3 = random.choice(pickpocket_victim_list3)
          print("=-=-=-=-=-=-PICKPOCKET OPTIONS=-=-=-=-=-=-=")
          print(f'1. A{pickpocket_victim1}')
          print(f'2. A{pickpocket_victim2}')
          print(f'3. A{pickpocket_victim3}\n')
          pickpocket_choice = int(input('Who would you like to pickpocket? '))
          if pickpocket_choice == 1:
            chosen_pickpocket_victim = pickpocket_victim1
          elif pickpocket_choice == 2:
            chosen_pickpocket_victim = pickpocket_victim2
          elif pickpocket_choice == 3:
            chosen_pickpocket_victim = pickpocket_victim3
          print(f'\nYou begin your attempt to pickpocket a{chosen_pickpocket_victim}.\n')
          time.sleep(1.5)
          print('Pickpocketing...\n')
          time.sleep(3)
          pickpocket_luck = random.randint(1,3)
          ran_pickpocket_money = random.randint(5,25)
          if pickpocket_luck == 3:
            print(f"You were succesful in pickpocketing a{chosen_pickpocket_victim}!")
            time.sleep(1)
            print(f'They had ${ran_pickpocket_money}.00 in their pocket.')
            time.sleep(1)
            money += ran_pickpocket_money
            net_worth += ran_pickpocket_money
            money_reset()
            time.sleep(1)
            print('You gained 5 aura!')
            time.sleep(1)
            aura += 5
            aura_reset()
          else:
            print(f"You were unsuccesful in pickpocketing a{chosen_pickpocket_victim}...")
            time.sleep(1.5)
            pickpocket_punishments_num = random.randint(1,3)
            if pickpocket_punishments_num == 1:
              print('They pushed to the ground and told you to watch yourself.')
              time.sleep(1)
              aura -= 3
              print('\nYou lost 3 aura!')
              time.sleep(1)
              aura_reset()
            elif pickpocket_punishments_num == 2:
              print('They let you off with a strong warning.')
              time.sleep(1)
              aura -= 3
              print('\nYou lost 3 aura!')
              time.sleep(1)
              aura_reset()
            elif pickpocket_punishments_num == 3:
              print('They punched you in the nose, causing you to bleed.')
              time.sleep(1)
              aura -= 5
              print('\nYou lost 5 aura!')
              time.sleep(1)
              aura_reset()
          time.sleep(1)
          hunger_end()
        elif crime_option == 2:
          hunger += 5
          crimes_commited += 1
          print('dog')
          hunger_end()
        elif crime_option == 3:
          hunger += 5
          crimes_commited += 1
          print("=-=-=-=-=-=-THINGS TO STEAL=-=-=-=-=-=-=\n")
          time.sleep(1)
          print("=-=-=-EASY-=-=-=")
          print("1. Mars bar ------------- $2.00")
          print("2. Chippy chips --------- $5.00\n")
          print("=-=-=-MEDIUM-=-=-=")
          print("3. Beer ----------------- $8.00")
          print("4. Bucket of cheese balls $10.00\n")
          print("=-=-=-VERY HARD-=-=-=")
          print("5. Headache pills ------- $100.00")
          print("6. SLAB OF NUTRITION ---- $100.00")
          print('7. 95% VODKA ------------ $120.00\n')
          print("=-=-=-DARE TO TRY?-=-=-=")
          print('8. GLASS OF GOLD -------- $2000.00\n')
          steal_shop = int(input('What would you like to steal? '))
          easy_steal_luck = random.randint(1,2)
          medium_steal_luck = random.randint(1,4)
          veryHard_steal_luck = random.randint(1,30)
          if steal_shop == 1:
            print('\nYou begin your attempt to steal a Mars bar.')
            time.sleep(1)
            print('\nStealing...')
            time.sleep(3)
            #Mars bar stolen?
            if easy_steal_luck == 2:
              hunger -= 5
              print('\nYou stole a Mars bar!')
              hunger_reset()
              print('\nYou gained 1 aura!')
              aura_reset()
            else:
              time.sleep(1)
              print("\nThe store owner caught you trying to steal the Mars bar!")
              time.sleep(1)
              print('He has made you pay $1.00!\n')
              time.sleep(1)
              money -= 1
              money_reset()
              print('\nYou have lost 3 aura!')
              time.sleep(1)
              aura -= 3
              aura_reset()
          elif steal_shop == 2:
            print('\nYou begin your attempt to steal Chippy chips.')
            time.sleep(1)
            print('\nStealing...')
            time.sleep(3)
            #Chippy chips stolen?
            if easy_steal_luck == 2:
              hunger -= 10
              print('\nYou stole Chippy chips!')
              hunger_reset()
              print('\nYou gained 3 aura!')
              aura_reset()
            else:
              time.sleep(1)
              print("\nThe store owner caught you trying to steal Chippy chips!")
              time.sleep(1)
              print('He has made you pay $3.00!\n')
              time.sleep(1)
              money -= 3
              money_reset()
              print('\nYou have lost 4 aura!')
              time.sleep(1)
              aura -= 5
              aura_reset()
          elif steal_shop == 3:
            print('\nYou begin your attempt to steal Beer.')
            time.sleep(1)
            print('\nStealing...')
            time.sleep(3)
            #Beer stolen?
            if medium_steal_luck == 4:
              drunk_lvl += 10
              print('\nYou stole Beer!')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}%.')
              time.sleep(1)
              print('\nYou gained 5 aura!')
              aura_reset()
            else:
              time.sleep(1)
              print("\nThe store owner caught you trying to steal Beer!")
              time.sleep(1)
              print('He has made you pay $5.00!\n')
              time.sleep(1)
              money -= 5
              money_reset()
              print('\nYou have lost 8 aura!')
              time.sleep(1)
              aura -= 8
              aura_reset()
          elif steal_shop == 4:
            print('\nYou begin your attempt to steal a Bucket of cheese balls.')
            time.sleep(1)
            print('\nStealing...')
            time.sleep(3)
            #Bucket of cheese balls stolen?
            if medium_steal_luck == 4:
              hunger -= 5
              print('\nYou stole a Bucket of cheese balls!')
              hunger_reset()
              print('\nYou gained 5 aura!')
              aura_reset()
            else:
              time.sleep(1)
              print("\nThe store owner caught you trying to steal a Bucket of cheese balls!")
              time.sleep(1)
              print('He has made you pay $5.00!\n')
              time.sleep(1)
              money -= 5
              money_reset()
              print('\nYou have lost 8 aura!')
              time.sleep(1)
              aura -= 8
              aura_reset()
          elif steal_shop == 5:
            print('\nYou begin your attempt to steal Headache pills.')
            time.sleep(1)
            print('\nStealing...')
            time.sleep(3)
            #Headache pills stolen?
            if veryHard_steal_luck == 21:
              drunk_lvl -= 100
              if drunk_lvl < 0:
                drunk_lvl = 0
              print('\nYou stole Headache pills!')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}%.')
              time.sleep(1)
              print('\nYou gained 8 aura!')
              aura_reset()
            else:
              time.sleep(1)
              print("\nThe store owner caught you trying to steal Headache pills!")
              time.sleep(1)
              print('He has made you pay $20.00!\n')
              time.sleep(1)
              money -= 30
              money_reset()
              print('\nYou have lost 12 aura!')
              time.sleep(1)
              aura -= 12
              aura_reset()
          elif steal_shop == 6:
            print('\nYou begin your attempt to steal a Slab of nutrition.')
            time.sleep(1)
            print('\nStealing...')
            time.sleep(3)
            #Slab of nutrition stolen?
            if veryHard_steal_luck == 21:
              hunger -= 100
              print('\nYou stole a Slab of nutrition!')
              hunger_reset()
              print('\nYou gained 8 aura!')
              aura_reset()
            else:
              time.sleep(1)
              print("\nThe store owner caught you trying to steal a Slab of nutrition!")
              time.sleep(1)
              print('He has made you pay $20.00!\n')
              time.sleep(1)
              money -= 30
              money_reset()
              print('\nYou have lost 12 aura!')
              time.sleep(1)
              aura -= 12
              aura_reset()
          elif steal_shop == 7:
            print('\nYou begin your attempt to steal 95% VODKA.')
            time.sleep(1)
            print('\nStealing...')
            time.sleep(3)
            #95% VODKA Stolen?
            if veryHard_steal_luck == 21:
              drunk_lvl += 150
              print('\nYou stole 95% VODKA!')
              time.sleep(1)
              print(f'Your drunk level is now {drunk_lvl}%.')
              time.sleep(1)
              print('\nYou gained 10 aura!')
              aura_reset()
            else:
              time.sleep(1)
              print("\nThe store owner caught you trying to steal 95% VODKA!")
              time.sleep(1)
              print('He has made you pay $25.00!\n')
              time.sleep(1)
              money -= 35
              money_reset()
              print('\nYou have lost 12 aura!')
              time.sleep(1)
              aura -= 12
              aura_reset()
          elif steal_shop == 8:
            time.sleep(3)
            print('\nWow...you tried.')
            time.sleep(3)
            print("That's a bold move.")
            time.sleep(3)
            print('Very bold...\n')
            time.sleep(3)
            print("You know what?")
            time.sleep(3)
            print("I'll give you options. Chose wisely...\n")
            time.sleep(3)
            print("=-=-=-=-=-=-OPTIONS=-=-=-=-=-=-=")
            print('1. Surrender and leave (-25 Aura)')
            print('2. Begin the impossible quiz (-$25.00)')
            print(f'\nYou have ${money}.00')
            glass_of_gold_option = int(input('\nWhat would you like to do? '))
            if glass_of_gold_option == 1:
              if money < 25:
                print('\nFair enough...')
                time.sleep(1)
                print("You didn't have the money anyways.")
                time.sleep(3)
                aura -= 25
                print('You lost 25 aura!')
                aura_reset()
                print(f'\nHow do you only have {money} bucks?')
                time.sleep(1)
                print('Brokie.')
              else:
                print('\nOkay...there goes your aura, I guess.')
                time.sleep(2)
                aura -= 25
                print('You lost 25 aura!')
                aura_reset()
                print(f'\nYou literally had ${money}.00!!')
                time.sleep(1)
                print("That's just a worse choice...")
                time.sleep(3)
                print("\nStuff this...")
                time.sleep(3)
                print("I'm taking your money too.")
                time.sleep(3)
                print("You lost $25.00!")
                money_reset()
            elif glass_of_gold_option == 2:
              if money < 25:
                print("\nWHY WOULD YOU DEFY ME???!!!")
                time.sleep(3)
                print("I told you how much money you had. THIS IS YOUR FAULT!!!")
                time.sleep(3)
                while True:
                  aura_taken_gog = int(input('How much aura should I take from you? '))
                  if aura_taken_gog >= 35:
                    print("\nThat's right!")
                    time.sleep(1)
                    print(f'You have to lose {aura_taken_gog}!')
                    time.sleep(3)
                    print('Never defy me again.')
                    time.sleep(1)
                    break
              else:
                print("\nNice!!!")
                time.sleep(1)
                print("For the low price of only $25.00, you have entered Jack and Ari's Glass of Gold Quiz!!")
                money -= 25
                money_reset()
                time.sleep(3)
                print('\nThis is the first question: ')
                time.sleep(1)
                question_1 = input('\nWould you rather be drunk or sober? ')
                if question_1.lower() == 'drunk':
                  print("\nThat's correct!")
                  time.sleep(3)
                  print('Question 2:')
                  time.sleep(1)
                  correct_gog += 1
                  print("\n=-=-=-=-=-=-QUESTION 2=-=-=-=-=-=-=")
                  print("1. 2")
                  print("2. ")
                  print("3. A window")
                  print("4. 11")
                  print("11. 2\n")
                  question_2 = int(input('1 + 1 = '))
                  if question_2 == 11:
                    print("\nThat's correct!")
                    correct_gog += 1
                    time.sleep(3)
                    print('Question 3: \n')
                    time.sleep(1)
                    question_3 = int(input('How many letters in this queestion? '))
                    if question_3 == 13:
                      print("That's wrong! There is 12 letters in 'this question'!")
                      time.sleep(10)
                      print("Just kidding...that's the correct answer.")
                      correct_gog += 1
                      time.sleep(3)
                      print('Question 3: \n')
                      time.sleep(1)
                      question_4 = int(input('8868888800000888666000\nhoow maany hooooooooooooleeeeeessssssss? '))
                      if question_4 == 54:
                        print('\nHAHA!! I just wasted your time! It is correct though.')
                        correct_gog += 1
                        time.sleep(3)
                        print("Final 'question': \n")
                        time.sleep(1)
                        gog_num1 = random.randint(1,10)
                        question_5 = int(input('Pick a number between 1-10: '))
                        if question_5 == gog_num1:
                          print('\nWow...you did it!')
                          time.sleep(3)
                          print(f'You picked {question_5} and the answer was {gog_num1}.')
                          time.sleep(3)
                          print('Congratulations! Here is the GLASS OF GOLD!!')
                          time.sleep(3)
                          print('\nYou have the Glass of gold.')
                          time.sleep(3)
                          print('You take a sip...')
                          time.sleep(3)
                          print('You insatantly feel the effec-')
                          time.sleep(3)
                          print("\nNo you don't...this-")
                          time.sleep(3)
                          print('is fake!!!')
                          time.sleep(3)
                          print("\nYou get on your knees and scream...'NOOOOOOOO!!!!!'.")
                          time.sleep(3)
                          print('You lose 25 aura.')
                          aura -= 25
                          time.sleep(2)
                          aura_reset()
                          time.sleep(2)
                        else:
                          print('Wow...you did it!')
                          time.sleep(3)
                          print(f'You picked {question_5} and the answer was {question_5}.')
                          time.sleep(3)
                          print(f'\nHAHAHA!!! JUST KIDDING!!! THE ANSWER WAS {correct_gog}!! YOU WILL NEVER WIN!!')
                          time.sleep(2)
                      else:
                        print('\nBro this question was just counting. Go back to kindergarten.')
                        time.sleep(1)
                    else:
                      print("Your terrible at this.")
                      time.sleep(1)
                  else:
                    print("You've got to think sharper than that to win at Jack and Ari's Glass of Gold Quiz!!")
                    time.sleep(1)
                else:
                  print('You only made it one quesiton...')
                  time.sleep(1)
                  print("That's embarassing.")
          else:
            print("\nThat isn't an option. Pick again!")
          hunger_end()
        if crime_option == 4:
          hunger += 5
          crimes_commited += 1
          car_list1 = ['Tesla Model 3','Toyota Corolla','Volkswagen beetle']
          car_list2 = ['Lamborgini Urus','Ferrari Roma','Porsche 911','Bugatti Veyron']
          car_list3 = ['Ford F-Series','Ford Ranger','Audi A7','Toyota Camry']
          victim_car1 = random.choice(car_list1)
          victim_car2 = random.choice(car_list2)
          victim_car3 = random.choice(car_list3)
          print("=-=-=-=-=-=-CARS TO STEAL=-=-=-=-=-=-=")
          print(f'1. {victim_car1}')
          print(f'2. {victim_car2}')
          print(f'3. {victim_car3}\n')
          car_to_steal = int(input('What car would you like to steal? '))
          if car_to_steal == 1:
            chosen_car_to_steal = victim_car1
          elif car_to_steal == 2:
            chosen_car_to_steal = victim_car2
          elif car_to_steal == 3:
            chosen_car_to_steal = victim_car3
          else:
            print("\nThat isn't an option. Pick again!")
          if chosen_car_to_steal == victim_car2:
            ran_car_luck = random.randint(1,8)
          else:
            ran_car_luck = random.randint(1,5)
          print(f'\nYou begin your attempt to steal the {chosen_car_to_steal}.\n')
          time.sleep(1)
          print('Stealing...\n')
          time.sleep(3)
          if ran_car_luck == 4:
            if chosen_car_to_steal == victim_car2:
              print(f'You successfully stole the {chosen_car_to_steal}!!!\n')
              user_car = chosen_car_to_steal
              aura += 15
              print('You gained 15 aura!')
              aura_reset()
            else:
              print(f'You succesfully stole the {chosen_car_to_steal}!\n')
              user_car = chosen_car_to_steal
              aura += 8
              print('You gained 8 aura!')
              aura_reset()
          else:
            car_punishment = random.randint(1,3)
            if car_punishment == 1:
              print('You have caught the atteniton of some nearby cops!')
              time.sleep(1)
              if chosen_car_to_steal == victim_car2:
                print(f'They caught you trying to steal the expensive {chosen_car_to_steal}!')
                time.sleep(3)
                print('You have been fined $75.00')
                money -= 75
                money_reset()
                aura -= 10
                time.sleep(3)
                print('You have lost 10 aura.')
                aura_reset()
              else:
                print(f'They caught you trying to steal the {chosen_car_to_steal}.')
                time.sleep(3)
                print('You have been fined $50.00')
                money -= 50
                money_reset()
                aura -= 8
                time.sleep(3)
                print('You have lost 8 aura.')
                aura_reset()
            elif car_punishment == 2:
              print(f'The owner of the {chosen_car_to_steal} has caught you trying to steal it!\n')
              time.sleep(3)
              print('They beat you up and took your shoes!!')
              time.sleep(1)
              print('You lost your $35.00 shoes!')
              money -= 35
              money_reset()
              time.sleep(1)
              aura -= 15
              print('You lost 15 aura!')
              time.sleep(1)
              aura_reset()
            elif car_punishment == 3:
              print(f'Somebody spotted you trying to steal the {chosen_car_to_steal}.\nYou managed to escape and avoid them.')
              time.sleep(3)
              print('You lost 3 aura.')
              aura -= 3
              aura_reset()
          hunger_end()      
        elif crime_option == 5:
          hunger += 5
          crimes_commited += 1
          print('dog')

        elif crime_option == 6:
          print('You had freaky thoughts...')
          time.sleep(1)
      if option == 5:
        print('You leave the gas station...')
        num1 = random.randint(1,100)
        if num1 == 69:
          time.sleep(3)
          print('Wait...')
          time.sleep(3)
          print(f"Where's your {user_car}?...")
          time.sleep(3)
          print('"NOOOO!!!" You scream. "How am I supposed to drink and drive??"')
          time.sleep(5)
          print('You urgently search for your car...')
          time.sleep(5)
          print("You can't find anything...")
          time.sleep(3)
          print("There's only one option...")
          time.sleep(5)
          print('You must steal a car.\n')
          time.sleep(3)
          carlist = ['Lamborghini Veneno','Porsche 911','Rolls-Royce Sweptail','Ferrari 275','Old toyota Corolla']
          secret_win = False
          while secret_win == False:
            rand_car = random.choice(carlist)
            steal_it = input(f'{rand_car}\nSteal this car? ')
            print()
            if steal_it.lower() in ['y','1','yes','sure','s','steal']:
              if rand_car == 'Old toyota Corolla':
                secret_win = True
                print('Congratulations! You succesfully stole the Old toyata Corolla!')
                time.sleep(3)
                print('Thanks for paticipating in the secret ending!')
                time.sleep(3)
              else:
                ran_steal = random.randint(1,3)
                if ran_steal == 1:
                  print(f'You try to steal the expenisve {rand_car}, but an old man catches you, comes over and beats you with a metal pole!\n')
                  aura -= 5
                  aura_reset()
                  time.sleep(8)
                elif ran_steal == 2:
                  print(f"You try to steal the expensive {rand_car} by punching through the window, but the glass is too strong and it doesn't break, causing your knuckles to bleed.\n")
                  aura -= 10
                  aura_reset()
                  time.sleep(8)
                elif ran_steal == 3 and drunk_lvl > 100:
                  print(f"You try to steal the expensive {rand_car}, but you're too drunk and forget how to turn the car on!\n")
                  aura -= 2
                  aura_reset()
                  time.sleep(8)
                else:
                  print(f"You try to steal the expensive {rand_car}, but your attention is caught by Kai Cenat walking on the pavement, and the owner drives off in the car!\n")
                  aura -= 8
                  aura_reset()
                  time.sleep(8) 
            else:
              print("That isn't an option!")
              time.sleep(1)
              print("you don't get to complete the secret ending!!!")
              time.sleep(5)
        else:
          print()
      if option == 7:
        achievements()

