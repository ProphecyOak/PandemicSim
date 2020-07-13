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
7. The "Reset" button will set the people on the screen back to all healthy.
8. Clicking "Close" will exit the application.

Notes/Trivia:
1. The colors and meanings are as follows: Healthy: Blue, Infected Symptomatic: Red, Infected Asymptomatic: Orange, Recovered: Gray, Dead: Black
2. The strictness values are related to how "rebellious" each person is. People with higher rebelliousness are more likely to move when symptomatic and less likely to social distance effectively.
