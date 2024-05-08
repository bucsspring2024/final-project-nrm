[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14587810&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << School day simulator >>
## CS110 Final Project  << spring , 2024 >>

## Team Members

<< Natalie Mastrantoni, Lily Aronov>>

***

## Project Description

<< We will simulate a day of school that starts with an alarm, proceeds to go through trivia in history and math classes, enters a foodfight during lunch, and leaves on the school bus >>

***    

## GUI 



### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design
<< The program comprises several classes:
End Class: Represents the end of the school day, displaying messages and playing a video of a school bus.
History Class: Represents the history class session, displaying the history teacher's image.
Math Class: Represents the math class session, displaying the math teacher's image and playing their sound.
Academics Class: Manages academic sessions, fetching trivia questions, displaying them, and checking user responses.
Lunch Class: Manages lunchtime activities, including interactive scenes such as food fights.
Controller Class: Orchestrates the program flow, controlling transitions between activities and managing the main loop.
Each class focuses on specific aspects of the school day, aiming to provide an engaging educational experience for the user through interactive content and fun activities. >>


### Features
<<
1. Fetch trivia questions using API and display feedback based on user interaction 
2. Uses screendisplay and alarm sound to simuate waking up 
3. Simulates a simulation of a lunch room experience including food fight 
4. Presents a simulation of ending school 
5. Utilizes an indexed list of object instances for each relevant class to access the mainloop and relevant methods in each of them >>

### Classes
<<
- Math Class - it controls the specific features of the math class such as screen display and api url
- History class - it controls the specific features of the math class
- academics class - it controls the methods that relate to both the history and math class, such as fetching trivia questions, checking if answers are correct
- Lunch class - controls the screen display and methods of a simulated food fight
- end_of_day class - it controls the simulated scenes of the end of the game
>> 

### Citations
<< @article{opencv_library,
    author = {Bradski, G.},
    citeulike-article-id = {2236121},
    journal = {Dr. Dobb's Journal of Software Tools},
    keywords = {bibtex-import},
    posted-at = {2008-01-15 19:21:54},
    priority = {4},
    title = {{The OpenCV Library}},
    year = {2000}
}
>>

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
