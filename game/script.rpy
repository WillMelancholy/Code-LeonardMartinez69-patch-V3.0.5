init :
    # Background images
    image bg laboratory = "images/Laboratory.png"
    image bg laboratory_table = "images/Laboratory.png"
    image bg classroom = "images/classroom.png"
    image bg classroom_pov = "images/classroom_pov.png"
    image bg menu = "images/MenuBG.png"
    image bg hallway = "images/Hallway1.png"

    # Irene images
    image irene speaking:
        "images/Irene_Speak.png"
        zoom 0.5
    image irene speak2:
        "images/Irene_Speak2.png"
        zoom 0.5
    image irene default:
        "images/Irene_Default.png"
        zoom 0.5

    # Lead moore images
    image Lead Moore speaking:
        "images/LEADMORE_HAPY.png"
        zoom 0.5
    image Lead Moore cry:
        "images/nevercookagain.png"
        zoom 0.5
    image Lead Moore happy:
        "images/LEADMORE_ABSOLUTE CINEMA.png"
        zoom 0.5

    # Titania images
    image titania speaking:
        "images/Titania_Speak.png"
        zoom 0.5
    image titania smile:
        "images/Titania_Smile.png"
        zoom 0.5
    image titania idle:
        "images/Titania_Idle.png"
        zoom 0.5

    # Chlory images
    image chlory speaking:
        "images/Chlory_Speak.png"
        zoom 0.525
        yalign -0.2
    image chlory confused:
        "images/Chlory_Confused.png"
        zoom 0.5
    image chlory idle:
        "images/Chlory_Idle.png"
        zoom 0.5
        yanchor 0.95
    image chlory happy:
        "images/Chlory_Happy.png"
        zoom 0.5
        yanchor 0.95

    # Yuranno images
    image yuranno speaking:
        "images/Yuranno_Speak.png"
        zoom 0.5
    image yuranno confused:
        "images/Yuranno_Confused.png"
        zoom 0.5
    image yuranno default:
        "images/Yuranno_Default.png"
        zoom 0.5

    # Additional character images
    image characA idle1:
        "images/characA_IDLE1.png"
        zoom 0.5
    image characA greet:
        "images/characAGREET.png"
        zoom 0.5

    # Icon placeholder
    image icon placeholder:
        "images/ICON_PLACEHOLDER.png"
        zoom 0.5

#FOR CHARACTER SPEAKING GENERATOR
init python:

    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

define e = Character("Eileen")
define player = Character("Player")
define A = Character("Irene")
define B = Character("Titania")
define C = Character("Chlory")
define D = Character("Yuranno")
define L = Character("Lead Moore", who_style="small_name")

style small_name:
    size 50
    xpos 50
    ypos 60
define correct = "You got the right answer!"
define wrong = "You got the wrong answer!"

style large_text :
    size 20
default materials = {
    "Wire": "images/wire.png",
    "Tongs": "images/tongs.png",
    "Bunsen Burner": "images/bunsen_burner.png",
    "Evaporating Dish": "images/evaporating_dish.png",
    "Magnesium": "images/magnesium.png",
    "Test Tubes": "images/test_tubes.png",
    "Test Tube Holder": "images/test_tube_holder.png",
    "Matches": "images/matches.png",
    "Copper (II) Carbonate (CuCO3)": "images/copper_carbonate.png",
    "5mL of 3M Hydrochloric Acid (HCl)": "images/hydrochloric_acid.png",
    "Zinc Metal (Zn)": "images/zinc_metal.png",
    "Wood Splint": "images/wood_splint.png",
    "5mL of 1M Copper (II) Sulfate (CuSO4)": "images/copper_sulfate.png",

}

label before_main_menu:
    $ preferences.set_volume("music", 0.2)  # set default main music
    return


label start:
    show screen Backbutton

    play music "<loop 6.33>audio/classroom.ogg" fadein 1.0

    call variables from _call_variables  
    show screen ScoreOverlay  
    

    scene bg classroom_pov
    with fade

    show irene default
    A "Yo! are you awake? "
    hide irene default

    show irene speak2 at left
    A "We were assigned as {i}{color=#E2A602} groupmates {/color}{/i} for the experiment"
    hide irene speak2 
    
    show irene speaking at left
    A "Oh, It's me {color=#9858CD}[A]{/color} btw, Nice to meet you I guess."
    hide irene speaking

    show titania speaking at left
    B "And I'm {color=#9192C8}[B]{/color}. Let's split up the parts, I'll do the second experiment!"
    hide titania speaking

    show chlory speaking
    C "Then the third should be mine! {color=#E2A602}[C]{/color} by the way, nice to meet you!"
    hide chlory speaking

    show yuranno speaking at right
    D "I guess the last one's mine then. The name's {color=#00C02D}[D]{/color}."
    hide yuranno speaking

    show titania smile
    B "Guess you should {color=#E2A602}help them and contribute to the group{/color} then, [player]!"
    hide titania smile

    player "Sure!"

    show irene speaking at left
    A "Let's do mine first!"
    hide irene speaking

   
    jump scene_2

label scene_2:
    show screen Backbutton
    scene bg laboratory_table
    with fade
    
    show irene speaking at left
    A "I'll {color=#E2A602}read out the process in the book, then you keep it in mind.{/color}"
    hide irene speaking

    player "*nods*"
    
    show irene speaking at left
    A "Here I go! It says that we should-"
    A "{color=#EC15DA}Note the appearance of the wire.{/color}"
    A "Using the {color=#EC15DA}tongs{/color}..."
    A "We must hold the {color=#EC15DA}wire{/color} in the hottest part of a {color=#EC15DA}burner flame for 1 to 2 minutes.{/color}"
    A "But first, to do that, we need to fix the {color=#EC15DA}Bunsen burner{/color}. Put the end of the tube into the yellow faucet, and the other end to the {color=#EC15DA}Bunsen burner.{/color}"
    A "Then, we place the {color=#EC15DA}evaporating dish{/color} near the base of the burner."
    A "After that, we get a piece of {color=#EC15DA}magnesium{/color} from the laboratory coordinator."
    A "Using {color=#EC15DA}crucible tongs{/color}, hold the sample in the burner flame until the{color=#EC15DA} magnesium {/color}starts to burn"
    A "REMEMBER,{color=#ff0000} DO NOT LOOK DIRECTLY AT THE FLAME.{/color}"
    A "When the ribbon stops burning, put the remains in the evaporating dish. Then we examine all that!"
    A "Did you get all that?"
    hide irene speaking
    
    player "*nods*"
    
    show irene speaking at left
    A "Great! Let's start!"
    hide irene speaking
    $ first_try = True
    jump scene_3

label scene_3:
    hide screen Backbutton
    if "q1" in variables.wrong_answers or first_try:
        show irene speaking at left
        A "What are the materials we need?"
        hide irene speaking

        call screen tutorial1(scene_3_info)

        # Define correct materials and all items
        $ correct_materials = {"Wire", "Tongs", "Bunsen Burner", "Evaporating Dish", "Magnesium"}
        $ all_items = list(materials.keys())

        # Ensure correct materials are included
        $ remaining_items = [item for item in all_items if item not in correct_materials]

        # Randomly select enough items to make a total of 6
        $ additional_items = renpy.random.sample(remaining_items, 9 - len(correct_materials))

        # Combine correct materials and additional items
        $ all_items = list(correct_materials) + additional_items
        $ renpy.random.shuffle(all_items)

        call screen material_selection(correct_materials, all_items, tutorial_info=scene_3_info)

        # Evaluate selection
        $ correct_selected = _return & correct_materials  # Intersection of selected and correct items
        $ points_earned = len(correct_selected)  # 1 point for each correct item

        show irene speaking at left
        if _return == correct_materials:
            # all materials correct, so the question was answered correctly
            $ variables.correct_answer("q1")
            A "[correct] You selected all the right materials!"
        else:
            # some materials are missing or incorrect, so we will make
            # this check again in the next run
            $ variables.wrong_answer("q1")
            $ missing_items = correct_materials - _return
            if missing_items:
                A "[wrong] You missed the following items: [', '.join(missing_items)]."
            else:
                A "[wrong] You selected incorrect items."
        hide irene speaking

    if "q2" in variables.wrong_answers or first_try:
        show irene speaking at left
        A "What do we do with this?"
        hide irene speaking

        menu:
            "Hold the sample in the burner flame until the magnesium starts to burn":
                $ variables.correct_answer("q2")
                show irene speaking at left
                A "Right! I remember now! DON'T LOOK AT IT DIRECTLY!"
                hide irene speaking
            "Put aside":
                $ variables.wrong_answer("q2")
                show irene speaking at left
                A "[wrong]"
                hide irene speaking
            "Hold the sample beside the burner flame for 2 to 3 minutes":
                $ variables.wrong_answer("q2")
                show irene speaking at left
                A "[wrong]"
                hide irene speaking
            "furiously start eating the magnesium":
                $ variables.wrong_answer("q2")
                show irene speaking at left
                A "[wrong]"
                hide irene speaking
    
    if len(variables.wrong_answers) > 0:
        $ first_try = False
        jump scene_2
    
    jump scene_4

label scene_4:
    show screen Backbutton

    show irene speaking at left
    A "We're finally done!"
    hide irene speaking
    
    show Lead Moore happy at left
    L "Great Job!"
    hide Lead Moore happy

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_5

label scene_5:
    
    show screen Backbutton

    scene bg laboratory_table
    with fade
    
    show titania speaking at left
    if not variables.wrong_answers:
        B "Oh! Great, you've finished the first experiment. Let's move on to mine next. It says here in the book that-"
    else:
        B "Let's see what went wrong. Here's what the book says-"
    
    B "{color=#EC15DA}Place 2 heaping micro spatulas of copper (II) carbonate (CuCO3) {/color} in a clean, dry test tube. {color=#EC15DA}Note the appearance of the sample.{/color}"
    
    B "Watch the appearance closely—it's a light green powder."
    
    B "Next, we'll heat it for about {color=#EC15DA}3 minutes.{/color} Use the test tube holder like this.{color=#EC15DA} Make sure you hold it at the top, and don't touch the bottom.{/color}"
    
    B "After heating, {color=#EC15DA}we insert a burning wood splint into the test tube. If carbon dioxide (CO2) is present, it will extinguish the flame.{/color}"

    B "{color=#D17D61}Make sure you observe any changes in the residue inside the test tube.{/color}"
    
    B "Did you get all that?"
    hide titania speaking
    
    player "*nods*"
    
    show titania speaking at left
    B "Great! Let's start!"
    hide titania speaking
    
    jump scene_6

label scene_6:
    hide screen Backbutton

    if "q1" in variables.wrong_answers or first_try:
        show titania speaking at left
        B "What are the materials we need?"
        hide titania speaking
        
        # Define correct materials and all items
        $ correct_materials = {"Test Tube Holder", "Test Tubes", "Matches", "Copper (II) Carbonate (CuCO3)", "Bunsen Burner"}
        $ all_items = list(materials.keys())

        # Ensure correct materials are included
        $ remaining_items = [item for item in all_items if item not in correct_materials]

        # Randomly select enough items to make a total of 6
        $ additional_items = renpy.random.sample(remaining_items, 9 - len(correct_materials))

        # Combine correct materials and additional items
        $ all_items = list(correct_materials) + additional_items
        $ renpy.random.shuffle(all_items)

        call screen material_selection(correct_materials, all_items)

        # Evaluate selection
        $ correct_selected = _return & correct_materials  # Intersection of selected and correct items
        $ points_earned = len(correct_selected)  # 1 point for each correct item

        show titania speaking at left
        if _return == correct_materials:
            $ variables.correct_answer("q1")
            B "[correct] You selected all the right materials!"
        else:
            $ variables.wrong_answer("q1")
            $ missing_items = correct_materials - _return
            if missing_items:
                B "[wrong] You missed the following items: [', '.join(missing_items)]."
            else:
                B "[wrong] You selected incorrect items."
        hide titania speaking

        show titania speaking at left
        B "Great! Next, what will we put in the clean, dry test tube?"
        hide titania speaking
    else:
        show titania speaking at left
        B "What will we put in the clean, dry test tube?"
        hide titania speaking
    
    if "q2" in variables.wrong_answers or first_try:
        menu:
            "2 heaping micro spatulas of copper (II) carbonate (CuCO3)"(is_correct=True):
                $ variables.correct_answer("q2")
                show titania speaking at left
                B "That's amazing!"
                hide titania speaking
            "3 heaping micro spatulas of copper (II) carbonate (CuCO3)":
                $ variables.wrong_answer("q2")
                show titania speaking at left
                B "Haha! I see you got confused. Let's try again later."
                hide titania speaking
            "2 heaping micro spatulas of Copper (II) carbonate (CuCO4)":
                $ variables.wrong_answer("q2")
                show titania speaking at left
                B "Haha! I see you got confused. Let's try again later."
                hide titania speaking
            "3 heaping micro spatulas of Copper (II) carbonate (CuCO2)":
                $ variables.wrong_answer("q2")
                show titania speaking at left
                B "Haha! I see you got confused. Let's try again later."
                hide titania speaking
    
    
    if "q3" in variables.wrong_answers or first_try:
        show titania speaking at left
        B "Now, let's heat it for 3 minutes. Do you have the test tube holder ready?"
        hide titania speaking
        menu:
            "Hold the top of the test tube firmly"(is_correct=True):
                $ variables.correct_answer("q3")
                show titania speaking at left
                B "Wow, that's great!"
                hide titania speaking
            "Hold the middle half of the test tube firmly":
                $ variables.wrong_answer("q3")
                show titania speaking at left
                B "Oh no! Be careful with that. You need to hold the test tube like this—"
                hide titania speaking
    
    
    if "q4" in variables.wrong_answers or first_try:
        show titania speaking at left
        B "How long will we heat this up?"
        hide titania speaking
        menu:
            "3 minutes"(is_correct=True):
                $ variables.correct_answer("q4")
                show titania speaking at left
                B "Wow, you have good memory!"
                hide titania speaking  
            "2 minutes":
                $ variables.wrong_answer("q4")
                show titania speaking at left
                B "Oh you got it wrong. Here look at the textbook again." 
                hide titania speaking
            "20 seconds":
                $ variables.wrong_answer("q4")
                show titania speaking at left
                B "Oh you got it wrong. Here look at the textbook again."
                hide titania speaking
            "1 minute":
                $ variables.wrong_answer("q4")
                show titania speaking at left
                B "Oh you got it wrong. Here look at the textbook again."
                hide titania speaking
    
    
    if "q5" in variables.wrong_answers or first_try:
        show titania speaking at left
        B "It's almost 3 minutes, what do we put inside the test tube?"
        hide titania speaking
        menu:
            "Burning wood splint"(is_correct=True):
                $ variables.correct_answer("q5")
                show titania speaking at left
                B "Wow, that's great!"
                hide titania speaking
            "Copper (II)":
                $ variables.wrong_answer("q5")
                show titania speaking at left
                B "No! Put this instead."
                hide titania speaking
    
    
    if "q6" in variables.wrong_answers or first_try:
        show titania speaking at left
        B "Oh shoot! I forgot, what's present if the flame of the burning wood splint inside the test tube gets put out?"
        hide titania speaking
        menu:
            "Carbon dioxide gas (CO2) is present"(is_correct=True):
                $ variables.correct_answer("q6")
                show titania speaking at left
                B "Okay, thanks!"
                hide titania speaking
            "Copper (II) carbonate (CuCO3) is present":
                $ variables.wrong_answer("q6")
                show titania speaking at left
                B "Hmm, are you sure?"
                hide titania speaking
    
    if "q7" in variables.wrong_answers or first_try:
    
        show titania speaking at left
        B "Okay, are we finished?"
        hide titania speaking
        menu:
            "No, we have to take note of the appearance of the residue in the test tube"(is_correct=True):
                $ variables.correct_answer("q7")
                show titania speaking at left
                B "Oh, right!"
                hide titania speaking
            "Yes, let's move on to the next experiment":
                $ variables.wrong_answer("q7")
                show titania speaking at left
                B "Oh no, did you take note of the appearance of the residue? Hmm, that's okay, I did!"
                hide titania speaking
    
    if len(variables.wrong_answers) > 0:
        $ first_try = False
        jump scene_5
    
    jump scene_7

label scene_7:
    show screen Backbutton
    show titania speaking at left
    B "We're finally done!"
    hide titania speaking
    show Lead Moore happy at left
    L "Absolute Cinema!"
    hide Lead Moore happy
    
    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_8

label scene_8:
    show screen Backbutton
    $ first_try = True
    scene bg laboratory_table
    with fade
    
    show chlory happy
    if not variables.wrong_answers:
        C "Congratulations! You've made it to the third experiment, substitution! I'm eager to explain what the book says here. So listen carefully!"
    else:
        C "Let's see what went wrong. The third experiment is substitution. Listen carefully to the instructions."
    hide chlory happy
    
    player "*nods*"
    
    label substitution_book:
    show screen Backbutton
    show chlory speaking
    C "{color=#EC15DA}CAUTION. IT IS IMPORTANT TO WEAR PROPER ATTIRE INSIDE THE LABORATORY EXPERIMENT SUCH AS: LABORATORY GOWN, SAFETY GOGGLES, FACE MASK, AND DISPOSABLE GLOVES.{/color}"
    
    C "Let's start! First, stand a clean, {color=#EC15DA}dry test tube{/color} in the test tube rack."
    
    C "Add about {color=#EC15DA}5 mL of 3 M hydrochloric acid (HCl){/color} to the tube."
    
    C "Then, carefully {color=#EC15DA}drop a small piece of zinc metal (Zn) into the acid in the test tube{/color}. Observe and record what happens."
    
    C "{color=#D17D61}Using a test tube holder{/color}, {color=#EC15DA}invert a second test tube over the mouth of the test tube in which the reaction is taking place."

    C "{color=#D17D61}Then, remove the inverted tube after 30 seconds and quickly insert a burning wood splint into the mouth of the tube{/color}."

    C "A 'pop' indicates the presence of hydrogen gas."
    
    C "Take note of the appearance of the substance in the reaction test tube."
    
    C "Now, for the second part: {color=#EC15DA}Add about 5 mL of 1 M copper (II) sulfate (CuSO4) solution{/color} to a clean, dry test tube."
    
    C "Then, {color=#EC15DA}Place a small amount of zinc metal in the solution{/color}." 
    
    C "Lastly, observe the solution and the zinc before and after the reaction."
    
    C "Did you get all that?"

    player "*nods*"
    
    hide chlory speaking
    show chlory happy
    C "Great! Let's start!"
    
    jump scene_9
    
label scene_9:
    hide screen Backbutton
    show chlory speaking
    C "Alright, to check your knowledge, it's time for a quiz!"

    if "q1" in variables.wrong_answers or first_try:
        C "What are the materials we need?"
        # Define correct materials and all items
        $ correct_materials = {"5mL of 3M Hydrochloric Acid (HCl)", "Zinc Metal (Zn)", "Wood Splint", "5mL of 1M Copper (II) Sulfate (CuSO4)", "Test Tubes", "Test Tube Holder"}
        $ all_items = list(materials.keys())

        # Ensure correct materials are included
        $ remaining_items = [item for item in all_items if item not in correct_materials]

        # Randomly select enough items to make a total of 6
        $ additional_items = renpy.random.sample(remaining_items, 9 - len(correct_materials))

        # Combine correct materials and additional items
        $ all_items = list(correct_materials) + additional_items
        $ renpy.random.shuffle(all_items)

        call screen material_selection2(correct_materials, all_items)

        # Evaluate selection
        $ correct_selected = _return & correct_materials  # Intersection of selected and correct items
        $ points_earned = len(correct_selected)  # 1 point for each correct item

        if _return == correct_materials:
            $ variables.correct_answer("q1")
            C "[correct] You selected all the right materials!"
        else:
            $ variables.wrong_answer("q1")
            $ missing_items = correct_materials - _return
            if missing_items:
                C "[wrong] You missed the following items: [', '.join(missing_items)]."
            else:
                C "[wrong] You selected incorrect items."
    
    if "q2" in variables.wrong_answers or first_try:
        C "Why should you be careful when handling hydrochloric acid (HCl)?"
        menu:
            "A. It can cause fire":
                $ variables.wrong_answer("q2")
                C "Oh no! You did not pay attention to the caution."
            "B. It can cause painful burns"(is_correct=True):
                $ variables.correct_answer("q2")
                C "That's right! It is important to handle acids with care."
            "C. It can stain your clothes":
                $ variables.wrong_answer("q2")
                C "Oh no! You did not pay attention to the caution."
        
    if "q3" in variables.wrong_answers or first_try:
        C "What is the next step after inverting the test tube for 30 seconds?"
        menu:
            "A. Immediately add about 5 mL of 1 M copper (II) sulfate (CuSO4) solution":
                $ variables.wrong_answer("q3")
                C "Oh no! Let me read the book again for you."
                jump substitution_book
            "B. Remove the inverted test tube and quickly insert burning wood splint into the mouth of the tube"(is_correct=True):
                $ variables.correct_answer("q3")
                C "Very good! You have remembered the procedure."
            "C. Smell the test tube and wait for another 1 minute":
                $ variables.wrong_answer("q3")
                C "Oh no! Let me read the book again for you."
                jump substitution_book
        
        hide chlory speaking

    if len(variables.wrong_answers) > 0:
        $ first_try = False
        jump scene_8

    jump scene_10
    
label scene_10:
    show screen Backbutton
    if variables.points >= 40:
        show chlory idle
        C "We're finally done!"
        hide chlory idle
        show Lead Moore happy at left
        L "You cooked hard, You're getting passing grades for that!"
        hide Lead Moore happy
    else:
        show Lead Moore cry at right
        L "Im gonna obliterate you both unless you take this seriously bro, redo it now."
        jump scene_8

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    jump scene_11

label scene_11:
    show screen Backbutton

    scene bg laboratory_table
    with fade

    show yuranno speaking

    if not variables.wrong_answers:
        D "Good morning! Are you ready for our last experiment? This one is called metathesis! I'm excited to walk you through it, so pay close attention!"
    else:
        D "Let's see what went wrong. The last experiment is metathesis. Listen carefully to the instructions."

    hide yuranno speaking
    show yuranno default
    
    D "First, we'll start by adding about {color=#EC15DA}2 mL of 0.1 M Lead Nitrate Pb (NO3)2{/color} to a clean, {color=#EC15DA}dry test tube.{/color}"
    
    D "Next, we'll add {color=#EC15DA}2 mL of 0.1 M Potassium Iodide (KI){/color} to the test tube. Watch closely!"
    
    D "Look at that! Observe the reaction and note any changes in the mixture."
    
    D "Next, we need to prepare three solutions. For Beaker A, add 5 drops of alcohol and 5 drops of phenolphthalein."
    
    D "For Beaker B, we'll prepare a saturated lead nitrate solution. That means adding 30g of lead nitrate to 10 mL of H2O."
    
    D "And for Beaker C, we'll add 15g of copper sulfate to 100 mL of H2O."
    
    D "Now, let's fill an Erlenmeyer flask with 1M ammonium hydroxide (NH4OH). We'll dissolve 3.5 g in 100 mL of H2O."
    
    D "Now comes the fun part! We'll fill each beaker with the ammonium hydroxide solution to produce red, white, and blue solutions."
    
    D "Make sure to {color=#EC15DA}observe the colors that develop!{/color}"

    D "Look! It's {color=#DCC43D}{b}Yellow!{/color}"
    
    jump scene_12

label scene_12:
    hide screen Backbutton

    D "Did you follow all of that? Let's do a quick quiz to check your understanding!"
    
    if "q1" in variables.wrong_answers or first_try:
        D "What should we add to the first test tube to start our reaction?"
        menu:
            "A. 2 mL of sodium chloride (NaCl)":
                hide yuranno speaking
                show yuranno confused
                $ variables.wrong_answer("q1")
                D "Not quite! It should be potassium iodide. Let's remember that for next time!"
                hide yuranno confused
                show yuranno speaking
            "B. 2 mL of potassium iodide (KI)"(is_correct=True):
                $ variables.correct_answer("q1")
                D "Exactly! Potassium iodide is correct!"
    
    if "q2" in variables.wrong_answers or first_try:
        D "What color did the mixture turn after adding the potassium iodide?"
        menu:
            "A. Blue":
                hide yuranno speaking
                show yuranno confused
                $ variables.wrong_answer("q2")
                D "Nope! It was yellow. Let's keep an eye out for that!"
                hide yuranno confused
                show yuranno speaking
            "B. Yellow"(is_correct=True):
                $ variables.correct_answer("q2")
                D "Right! It turned bright yellow!"
    
    if "q3" in variables.wrong_answers or first_try:
        D "What do we need to observe in the beakers after adding the ammonium hydroxide solution?"
        menu:
            "A. The color changes in the solutions"(is_correct=True):
                $ variables.correct_answer("q3")
                D "Correct! We need to observe the color changes!"
            "B. The temperature of the solutions":
                hide yuranno speaking
                show yuranno confused
                $ variables.wrong_answer("q3")
                D "That's not it! We're looking for color changes, not temperature."
                hide yuranno confused
                show yuranno speaking
    
    if len(variables.wrong_answers) > 0:
        $ first_try = False
        jump scene_11

    jump scene_13

label scene_13:
    show screen Backbutton
    $ first_try = True
    D "We did it! Great job!"
    hide yuranno speaking
    
    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."
    
    jump scene_14

label scene_14:
    show screen Backbutton

    scene bg classroom
    with fade

    show irene speaking at left
    A "Good morning, everyone! We are here today to present our findings on four interesting chemistry experiments: Synthesis, Analysis, Substitution, and Metathesis."
    hide irene speaking

    show titania speaking at right
    B "Let's begin with the Synthesis experiment, where we observed the reaction of magnesium with a Bunsen burner flame."
    hide titania speaking

    show irene speaking at left
    A "We noted the {color=#EC15DA}appearance of the wire {/color} before heating and then heated it in the hottest part of the flame for 1-2 minutes."
    A "The key thing was to observe the changes."
    hide irene speaking

    show chlory speaking
    C "Next, the Analysis experiment. We heated copper(II) carbonate and observed its color change and the {color=#EC15DA}emission of carbon dioxide.{/color}"
    hide chlory speaking

    show yuranno speaking at left
    D "The Substitution experiment involved the reaction of zinc with hydrochloric acid and copper(II) sulfate. {color=#EC15DA}Safety precautions were very important{/color}, as we worked with acids."
    hide yuranno speaking

    show irene speaking at right
    A "Finally, the Metathesis experiment. We mixed {color=#EC15DA}lead nitrate with potassium iodide and observed the precipitate formation.{/color}"
    hide irene speaking

    show titania speaking at left
    B "Now, let's test your knowledge with a quiz!"
    hide titania speaking

    jump quiz

label quiz:
    hide screen Backbutton
    
    if "q1" in variables.wrong_answers or first_try:
        show titania speaking at left
        B "Question 1: What important observation must be made in the Synthesis experiment before heating the wire?"
        hide titania speaking

        menu:
            "A. The color of the flame":
                $ variables.wrong_answer("q1")
                show chlory speaking
                C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
                hide chlory speaking
            "B. The length of the wire":
                $ variables.wrong_answer("q1")
                show chlory speaking
                C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
                hide chlory speaking
            "C. The appearance of the wire"(is_correct=True):
                $ variables.correct_answer("q1")
                show titania speaking at left
                B "That's right! Observing the wire before heating is crucial."
                hide titania speaking
            "D. The temperature of the burner":
                $ variables.wrong_answer("q1")
                show chlory speaking
                C "Not yet! If you don't record the original look of the wire, you cannot see how it changed."
                hide chlory speaking

    if "q2" in variables.wrong_answers or first_try:
        show chlory speaking
        C "Question 2: In the Analysis experiment, what gas was tested using the burning splint method?"
        hide chlory speaking

        menu:
            "A. Hydrogen":
                $ variables.wrong_answer("q2")
                show irene speaking at left
                A "Oops, incorrect! We tested for carbon dioxide."
                hide irene speaking
            "B. Oxygen":
                $ variables.wrong_answer("q2")
                show irene speaking at left
                A "Oops, incorrect! We tested for carbon dioxide."
                hide irene speaking
            "C. Carbon dioxide"(is_correct=True):
                $ variables.correct_answer("q2")
                show yuranno speaking at right
                D "That is correct! Carbon dioxide extinguished the flame."
                hide yuranno speaking
            "D. Nitrogen":
                $ variables.wrong_answer("q2")
                show irene speaking at left
                A "Oops, incorrect! We tested for carbon dioxide."
                hide irene speaking

    if "q3" in variables.wrong_answers or first_try:
        show yuranno speaking at right
        D "Question 3: In the Substitution experiment, what safety precaution is most important when handling hydrochloric acid?"
        hide yuranno speaking

        menu:
            "A. Wear gloves":
                $ variables.wrong_answer("q3")
                show titania speaking at left
                B "Not quite, though gloves are important!"
                hide titania speaking
            "B. Wear a lab coat":
                $ variables.wrong_answer("q3")
                show titania speaking at left
                B "Not quite, though protective clothing is needed!"
                hide titania speaking
            "C. Don't inhale fumes":
                $ variables.wrong_answer("q3")
                show titania speaking at left
                B "Important, but there's more to consider."
                hide titania speaking
            "D. All of the above"(is_correct=True):
                $ variables.correct_answer("q3")
                show yuranno speaking at right
                D "Correct! Safety first in all cases!"
                hide yuranno speaking

    if "q4" in variables.wrong_answers or first_try:
        show irene speaking at left
        A "Question 4: What was the noticeable change when lead nitrate reacted with potassium iodide in a Metathesis reaction?"
        hide irene speaking

        menu:
            "A. Temperature change":
                $ variables.wrong_answer("q4")
                show chlory speaking
                C "No, we were expecting a color change due to a precipitate forming."
                hide chlory speaking
            "B. Color change"(is_correct=True):
                $ variables.correct_answer("q4")
                show chlory happy
                C "That's correct! A precipitate formed, causing a color change."
                hide chlory happy
            "C. Gas production":
                $ variables.wrong_answer("q4")
                show chlory speaking
                C "No, we were expecting a color change due to a precipitate forming."
                hide chlory speaking
            "D. No change":
                $ variables.wrong_answer("q4")
                show chlory speaking
                C "No, we were expecting a color change due to a precipitate forming."
                hide chlory speaking

    if len(variables.wrong_answers) > 0:
        $ first_try = False
        jump scene_14

    python:
        if variables.is_online():
            player_name = renpy.input("Enter your name for the leaderboard:")
            variables.leaderboard.update({player_name: variables.points})
            variables.save_leaderboard()

    jump results

label results:
    show screen Backbutton
    if variables.points >= 40:
        "You have [variables.points] points."
        "In total, you made [variables.mistakes] wrong choices."
        B "Well done! You certainly listened well."
        D "Congratulations!"
    else:
        A "Looks like you're a bit of practice away. Don't worry!"
        C "You need to retake the quiz to improve your score. Let's go over the main observations again."
        D "Reloading the slideshow for review."
        jump quiz

    B "We hope you learned something new about these experiments. Thanks for trying it out!"    

    if variables.is_online():
        call screen Leaderboard(variables)

        menu leaderboard_menu:
            "Retry from the beginning":
                hide screen Leaderboard
                jump start
            "Exit":
                return
        
        hide screen ScoreOverlay
    return

label rightchoice:
    e "This is the right choice"

    return

label variables:
    python:
        variables = Variables()  
    return

