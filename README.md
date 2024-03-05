<h1>MATH ARCADE</h1> 
This is a math game using Raspberry Pi 3(Python) <br>
Flow: Asks for register number -> Asks difficulty level(Easy[+10] or Hard[+25]) -> Questions(Random generated variables within a range, comes in addition or subtraction) -> Uploads data to Website and Thinkspeak <br>
*If you input a single digit regnum, press "*" to submit <br>
*All inputs are with lcd keypad <br>
Website: Displays register number, timestamp, difficulty level, score<br>

If Q is answered RIGHT:<br>
Servo motor to move forward when a Q is answered right(in demo, I pasted a cutout of steve holding a sword so it seems like an you are "attacking" someone when a Q is answered right. <br>
Score increases. <br>
Message displayed to show correct and score <br>

If Q is answered WRONG:<br>
Red LED for when a Q is answered wrongly. <br>
Lives decrease(start with 3 lives)<br>
Message displayed to show wrong and lives left  <br>

Gameover(no more lives):<br>
Servo motor makes 180 degree turn(to like "hang yourself" lol)<br>
Red LED lights up<br>
Message displayed to show GAMEOVER and final score <br>
Data is uploaded to thinkspeak(see register num/score at given time)<br>
