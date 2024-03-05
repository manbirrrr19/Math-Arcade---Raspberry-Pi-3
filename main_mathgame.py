import time
import I2C_LCD_driver
from threading import Thread
import queue
import random 
from flask import render_template
import website
from hal import hal_led as led
from hal import hal_buzzer as buzzer
from hal import hal_keypad as keypad
from hal import hal_input_switch as input_switch
from hal import hal_servo as servo
import requests





#Empty list to store sequence of keypad presses
shared_keypad_queue = queue.Queue()


#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    shared_keypad_queue.put(key)


def get_user(): #find reg number of student

    regnumlist = []
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()

    LCD.lcd_display_string("Enter reg no.", 1)

    for i in range(2):
        while True:
            keyvalue= shared_keypad_queue.get() #get key inputted          
            if keyvalue == "*":
                break
            elif (keyvalue==1 or keyvalue==2 or keyvalue==3 or keyvalue==4 or keyvalue==5 or keyvalue==6 or keyvalue==7 or keyvalue==8 or keyvalue==9 or keyvalue == 0):
                LCD.lcd_display_string(str(keyvalue), 2, i)
                regnumlist.append(keyvalue)
                time.sleep(1)
                break
    regnumber = ''.join(map(str, regnumlist))
    return regnumber

def get_difficulty():
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()
    LCD.lcd_display_string("Press 1 for EASY", 1)
    LCD.lcd_display_string("Press 2 for HARD", 2)
    while True:
        keyvalue= shared_keypad_queue.get() #get key inputted
        if keyvalue == 1:
            mode = "easy"
            LCD.lcd_clear()
            time.sleep(1)
            LCD.lcd_display_string("Mode = EASY!", 1)
            LCD.lcd_display_string("* to submit ans", 2)
            time.sleep(1)
            break
        if keyvalue == 2:
            mode = "hard"
            LCD.lcd_clear()
            time.sleep(1)
            LCD.lcd_display_string("Mode = HARD!", 1)
            LCD.lcd_display_string("* to submit ans", 2)
            time.sleep(1)
            break
    return mode 

def easy_q():
    led.init()
    buzzer.init()
    servo.init()
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()
    global lives

    while lives > 0:
        randomvar = random.randint(1,2)
        if randomvar == 1:
            user_ans = []
            var1 = random.randint(50,100)
            var1_str = str(var1)
            var2 = random.randint(1,50)
            var2_str = str(var2)
            ans = var1 + var2
            ans_str = str(ans)
            LCD.lcd_display_string(var1_str + " + " + var2_str, 1)
        elif randomvar ==2:
            user_ans = []
            var1 = random.randint(50,100)
            var1_str = str(var1)
            var2 = random.randint(1,50)
            var2_str = str(var2)
            ans = var1 - var2
            ans_str = str(ans)
            LCD.lcd_display_string(var1_str + " - " + var2_str, 1)


        for i in range(5):
            keyvalue= shared_keypad_queue.get()
            if (keyvalue==1 or keyvalue==2 or keyvalue==3 or keyvalue==4 or keyvalue==5 or keyvalue==6 or keyvalue==7 or keyvalue==8 or keyvalue==9 or keyvalue == 0):    
                LCD.lcd_display_string(str(keyvalue), 2, i)
                user_ans.append(keyvalue)
            elif keyvalue == "*":
                userans = ''.join(map(str, user_ans))
                if userans == ans_str:
                    correct()
                    time.sleep(1)
                    break
                if userans != ans_str:
                    wrong()
                    time.sleep(1) 
                    break
 
    gameover()
    return points
    



def hard_q():
    led.init()
    buzzer.init()
    servo.init()
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()
    global lives

    while lives > 0:
        randomvar = random.randint(1,2)
        if randomvar == 1:
            user_ans = []
            var1 = random.randint(600,1000)
            var1_str = str(var1)
            var2 = random.randint(100,600)
            var2_str = str(var2)
            ans = var1 + var2
            ans_str = str(ans)
            LCD.lcd_display_string(var1_str + " + " + var2_str, 1)
        elif randomvar ==2:
            user_ans = []
            var1 = random.randint(600,1000)
            var1_str = str(var1)
            var2 = random.randint(100,600)
            var2_str = str(var2)
            ans = var1 - var2
            ans_str = str(ans)
            LCD.lcd_display_string(var1_str + " - " + var2_str, 1)


        for i in range(5):
            keyvalue= shared_keypad_queue.get()
            if (keyvalue==1 or keyvalue==2 or keyvalue==3 or keyvalue==4 or keyvalue==5 or keyvalue==6 or keyvalue==7 or keyvalue==8 or keyvalue==9 or keyvalue == 0):    
                LCD.lcd_display_string(str(keyvalue), 2, i)
                user_ans.append(keyvalue)
            elif keyvalue == "*":
                userans = ''.join(map(str, user_ans))
                if userans == ans_str:
                    correct_hard()
                    time.sleep(1)
                    break
                if userans != ans_str:
                    wrong()
                    time.sleep(1) 
                    break
 
    gameover()
    return points
    

def correct():
    led.init()
    buzzer.init()
    input_switch.init()
    servo.init()
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()

    global points
    points += 10
    points_str = str(points)
    LCD.lcd_display_string("Correct!", 1)
    LCD.lcd_display_string("POINTS: " + points_str, 2)
    servo.set_servo_position(60)
    time.sleep(2)
    servo.set_servo_position(0)
    #buzzer.play_melody([262, 294, 330, 349, 392, 440, 494], [4, 4, 4, 4, 4, 4, 4], 500)
    #time.sleep(3)
    #buzzer.stop()
    time.sleep(3)
    LCD.lcd_clear()

def wrong():
    led.init()
    buzzer.init()
    input_switch.init()
    servo.init()
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()

    global lives
    lives -= 1
    lives_str = str(lives)
    LCD.lcd_display_string("Wrong!", 1)
    LCD.lcd_display_string("LIVES: " + lives_str, 2)
    led.set_output(1, 1)
    time.sleep(3)
    led.set_output(1, 0)
    #buzzer.play_melody([262, 587, 523, 349, 87, 392, 494], [4, 5, 5, 4, 2, 4, 4], 500)
    #time.sleep(3)
    #buzzer.stop()
    LCD.lcd_clear()

def correct_hard():
    led.init()
    buzzer.init()
    input_switch.init()
    servo.init()
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()

    global points
    points += 25
    points_str = str(points)
    LCD.lcd_display_string("Correct!", 1)
    LCD.lcd_display_string("POINTS: " + points_str, 2)
    LCD.lcd_display_string("Correct!", 1)
    servo.set_servo_position(60)
    time.sleep(2)
    servo.set_servo_position(0)
    #buzzer.play_melody([262, 294, 330, 349, 392, 440, 494], [4, 4, 4, 4, 4, 4, 4], 500)
    #time.sleep(3)
    #buzzer.stop()
    time.sleep(3)
    LCD.lcd_clear()



def gameover():
    led.init()
    buzzer.init()
    input_switch.init()
    servo.init()
    LCD = I2C_LCD_driver.lcd()
    LCD.lcd_clear()

    global points
    points_str = str(points)
    LCD.lcd_display_string("Game over!!", 1)
    LCD.lcd_display_string("Total pts:" + points_str, 2)
    servo.set_servo_position(180)
    led.set_output(1, 1)
    time.sleep(3)
    led.set_output(1, 0)
    LCD.lcd_clear()
    
def send_to_thinkspeak(regnum,points):
    # ThingSpeak API endpoint URL
    url = 'https://api.thingspeak.com/update'

    # ThingSpeak channel API key
    api_key = 'W127YFEXOFV8HRFR'  # Replace with your ThingSpeak channel API key

    # Create a dictionary with the data to be sent
    data = {
        'api_key': api_key,
        'field1': regnum,
        'field2': points
    }

    # Send a POST request to ThingSpeak API
    response = requests.post(url, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        print("Data sent to ThingSpeak successfully")
    else:
        print("Failed to send data to ThingSpeak")
        print("Response:", response.text)


if __name__ == '__main__':
    website_thread = Thread(target=website.website_run)
    website_thread.start()
    keypad.init(key_pressed)
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    global points
    lives = 3
    points = 0
    regnum = get_user()
    game_mode = get_difficulty()
    if game_mode == "easy":
        easy_q()
    elif game_mode == "hard":
        hard_q()
    website.load_game_data()
    website.update_game_data(regnum, points, game_mode)
    
    send_to_thinkspeak(regnum, points)
     