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
- end_of_day class - it controls the simulated scenes of the end of the game.

## ATP

Test #1:
- Step 1: Start game
    - Open terminal , go to project folder type:
        - ''py
        python history.py
        '''
- Expected Result:
   - History class should show with first question to answer on screen"

Test #2:
- Step 1: Start game
    - Open terminal , go to project folder type:
         - ''py
        python end_of_day.py
        '''
- Expected Result:
    - Should have school pop up  then bus with noise.

Test #3:
- Step 1: Start history class 
    - Open terminal , go to project folder type:
         - ''py
        python history.py
        '''
- Step 2: Load screen with trivia questions
    - Player clicks on a box on the screen
- Expected result:
    - Should show teachers response if correct 

Test #4:
- Step 1: Start math class
    - Open terminal , go to project folder type:
         - ''py
        python math.py
        '''
- Step 2: Load screen with trivia question
    - Player click on box to choose answer
- Expected results:
    - Should load noise if correct or incorrect

Test #5:
- Step 1: Start lunch
    - Open terminal , go to project folder type:
          - ''py
        python lunch.py
        '''
- Step 2: Load screen 
    - Player should read the lines
- Expected results:
    - Conversation should run between player and other student
