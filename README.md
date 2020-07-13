# PandemicSim
Simulation of an outbreak and possibly, effective control.

Run App\Main.py to run.\n
Requires Python 3 and a machine that can run Tkinter.

User guide:
1. Click "Infect" to add a patient 0
2. To progress the sim, click "Move"
3. To have the sim repeatedly move, click "Start" ("Stop" to stop)
4. The "Distance!" button will toggle social distancing, shown by the rings around the dots.
5. Under "Social Distancing Strictness," you can put in how strict people will be about distancing ([0 - 15], 15 being most strict).
6. 35% of infected people will be asymptomatic. These people will go about there buisness like usual. The other 65% will quarantine to some extent. Under "Quarantine Strictness," you can put in how strict people will be about distancing ([-1 - 7]), -1 being least strict). Quarantined people still will move (with low strictness), just, at a lower speed.
7. The Population Size field works the same as the two strictness fields but it changes how many people will be on the canvas. Warning: This will reset the graph and set everyone to healthy.
8. The Person Size field works the same as the last three but instead it changes how large the dots that represent the people are. Warning: This will reset the graph and set everyone to healthy.
9. The "Reset" button will set the people on the screen back to all healthy.
10. Clicking "Close" will exit the application.

Notes/Trivia:
1. The colors and meanings are as follows: Healthy: Blue, Infected Symptomatic: Red, Infected Asymptomatic: Orange, Recovered: Gray, Dead: Black
2. The strictness values are related to how "rebellious" each person is. People with higher rebelliousness are more likely to move when symptomatic and less likely to social distance effectively.
3. The death rate is very close to the actual covid-19 death rate in the U.S. (according to our research). Each person has a chance to be of a certain age group and has a chance to be immunocompromised. These two factors affect how likely they are to die during each move in which they are infected.
