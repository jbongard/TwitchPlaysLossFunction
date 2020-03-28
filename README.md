# TwitchPlaysLossFunction

Rationale:  Deep learning required massive scale ups in data and architecture size. Robotics needs a massive scale up in loss functions.

Hypothesis: A crowd can create more perverse-instantiation resistant objective functions (PIROFs) than lone experts can.

## Experimental design

1. Double blind study.

2. Experts and non-experts submit objective functions via chat in Twitch.

3. Non-experts are shown robots evolved against both sets of functions.

4. If non-experts prefer those evolved using non-expert objective functions, this supports the hypothesis.

## Interface design

1. Users type equations into chat.

2. Equations manipulate matrices, but must ultimately result in a scalar.

3. Matrices are visualized as heatmaps.

4. Sensor data is visualized in the 'root' matrix.

5. The robot's body parts are colorized; sensor columns are shown in matching colors.

## To do list:

1. See if you can colorize the vertical axis of the raw sensor data.

2. Visualize 'sensor' data drawn from a file.

3. Create and left and right sides of equations.

4. Allow the typing in of equations.

5. Fill in drawing of robot from here: https://docs.google.com/drawings/d/1v_ECJ3ZAOSW_05xPlm-8kim38GA94JrakpJc98ihnmw/edit?usp=sharing

6. Create turret: the red/blue/green side barrels represent the rgb components of the ray sensor. The longer black barrel represents the length of the ray. The gun will sit on a turret that can rotate the gun side to side and up and down.
