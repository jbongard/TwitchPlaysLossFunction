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

1. Modify fitnessFunctions to pickle a default fitness function.

1. Then, chatbot can add, modify, or remove variables to/from pickled fit fn. 

1. Fill in drawing of robot from here: https://docs.google.com/drawings/d/1v_ECJ3ZAOSW_05xPlm-8kim38GA94JrakpJc98ihnmw/edit?usp=sharing

1. Create turret: the red/blue/green side barrels represent the rgb components of the ray sensor. The longer black barrel represents the length of the ray. The gun will sit on a turret that can rotate the gun side to side and up and down.

1. Create tutorial with levels:

1. f = 1

1. a = 1

1. f = a

1. f = s[1,1]

1. f = s[500,1]

1. f = s[1,500]

1. and so on.

## Miscellaneous notes.

1. Josh Powers: Why not use genetic programming to evolve fitness functions, where the
fitnes of any one fitness function is how many people preferred robots evolved using it
compared with others?
