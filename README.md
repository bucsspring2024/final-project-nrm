[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14587810&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << School day simulator >>
## CS110 Final Project  << spring , 2024 >>

## Team Members

<< Natalie Mastrantoni, Lily Aronov>>

***

## Project Description

<< We will simulate an average highschool day, with the player aswering questions or tasks in some  periods >>

***    

## GUI 


### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. << Feature 1 >> Presents history class with qestions for player to answer
2. << Feature 2 >> Presents math class with questions for player to answer
3. << Feature 3 >> Presents a simulation of a lunch room experience
4. << Feature 4 >> presents a simulation of ending school
5. << Feature 5 >>

### Classes

- Math Class - it controls the background and questions of the math simulated class
- History class - it controls the background and questions of the history simulated class
- Lunch class - it controls the simulated scense in the lunch room 
- end_classclass - it controls the simulated scenes of the end of the game.
- Controller Class - allows the mai 

## ATP

Test #1: Start screen
Descrition: Verify that the game starts.
- Step 1: Start game
    - Open terminal , go to project folder type:
        - ''py
        python main.py
        '''
- Step 2: Verify that start screen appears
- Step 3: Verify that alarm sound plays
- Expected Result:
   - Screen should appear that shows an alarm clock along with an alarm sound that plays.

Test #2: Prodcue a picture
Descrition: verifies that the intened end of day message and images appear on screen on order.
- Step 1: Start end_of day py
    - Open terminal , go to project folder type:
         - ''py
        python end_of_day.py
        '''
- Step 2: Verify that image stays on screen.
- Steo 3: Verty that sentences change to continue. 
- Expected Result:
    - Should have images appear on a window with messages appearing in order.

Test #3: 
Descrition: Api function for Math class
- Step 1: Start math_class.py 
    - Open terminal , go to project folder type:
         - ''py
        python math_class.py
        '''
- Step 2: Verify image and questions appear on screen.
- Step 3: Try to answer multiple choice math question.
    - use mouse to click on an answer.
- Step 4: Verify that response appears on screen according to result.
- Step 5: Verify that noise playsn according to result.
- Expected result:
    - Once question is answered a noise and message will play depending on if you got the question correct or not.

Test #4: Player interaction
Descrition: Ensures that code functions when player interacts with the simulator
- Step 1: Start lunch py
    - Open terminal , go to project folder type:
         - ''py
        python end_of_day.py
        '''
- Step 2: Follow instructions on screen
    - use mouse to click on the food to start foodfight
- Step 3: Verify that image changes once clicked
- Step 4: Verify that images continue to change following
- Expected results:
    - Should load series of images once player clicked on food to simulate foodfight

Test #3: 
Descrition: Api function for history class
- Step 1: Start history.py 
    - Open terminal , go to project folder type:
         - ''py
        python history.py
        '''
- Step 2: Verify image and questions appear on screen.
- Step 3: Try to answer multiple choice history question.
    - use mouse to click on an answer.
- Step 4: Verify that response appears on screen according to result.
- Step 5: Verify that noise playsn according to result.
- Expected result:
    - Once question is answered a noise and message will play depending on if you got the question correct or not.
