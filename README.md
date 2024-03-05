This is a math game using Raspberry Pi 3(Python)
Flow: Asks for register number -> Asks difficulty level(Easy[+10] or Hard[+25]) -> Questions(Random generated variables within a range, comes in addition or subtraction) -> Uploads data to Website and Thinkspeak
*If you input a single digit regnum, press "*" to submit 
*All inputs are with lcd keypad 
Website: Displays register number, timestamp, difficulty level, score

If Q is answered RIGHT:
Servo motor to move forward when a Q is answered right(in demo, I pasted a cutout of steve holding a sword so it seems like an you are "attacking" someone when a Q is answered right. 
Score increases. 
Message displayed to show correct and score 

If Q is answered WRONG:
Red LED for when a Q is answered wrongly. 
Lives decrease(start with 3 lives)
Message displayed to show wrong and lives left  

Gameover(no more lives):
Servo motor makes 180 degree turn(to like "hang yourself" lol)
Red LED lights up
Message displayed to show GAMEOVER and final score 
Data is uploaded to thinkspeak(see register num/score at given time)
