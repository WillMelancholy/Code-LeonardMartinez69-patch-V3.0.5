screen Leaderboard(data):
    tag leaderboard
    $ print(data.leaderboard)
    vbox style "st_leaderboard_box":
        hbox style "st_leaderboard_box":
            frame style "st_leaderboard_col1":
                background Solid("#bba67eff")
                text "Player Name" style "st_leaderboard_header"
            frame style "st_leaderboard_col2":
                background Solid("#8a6868ff")
                text "Points" style "st_leaderboard_header"
        $ index = 0
        for name, score in data.leaderboard.items():
            python:
                index += 1
                row_color = "#8a7d61bb" if index % 2 == 0 else "#92917fc4"
            hbox style "st_leaderboard_box":
                frame style "st_leaderboard_col1":
                    background Solid(row_color)
                    text "[name]" style "st_leaderboard_text"
                frame style "st_leaderboard_col2":
                    background Solid(row_color)
                    text "[score]" style "st_leaderboard_text"
    frame:
        background None
        anchor (1.0, 0.0)
        offset (-10, 10)
        pos (1.0, 0.0)
        vbox:
            xalign 1.0
            spacing 5
            button style "st_leaderboard_button":
                action Function(data.reload_leaderboard)
                text "Reload" style "st_leaderboard_button_text"
            button style "st_leaderboard_button":
                action Return()
                text "Close" style "st_leaderboard_button_text"
        
screen ScoreOverlay():
    tag score_overlay
    frame:
        anchor (0.5, 0.0)
        background Frame("lined_paper.png")  # Use an image of lined paper as background
        offset (0, 10)
        pos (0.5, 0.0)
        xsize 250  # Ensuring the frame is wide enough for centering
        vbox:
            spacing 10  # Increased spacing further to move Points text down
            xalign 0.5  # Ensures child elements are centered
            null height 20  # Moves the Points value down by adding space
            text ("Points") style "st_score_points_text"
            text "[variables.points]" style "st_score_variables_points_text"
            textbutton "Leaderboard":
                xalign 0.5
                background Solid("#e2e2e299")
                hover_background Solid("#757575cc")
                xsize 150  # Reduced width
                ysize 40   # Adjusted height
                text_size 22  # Ensures text scales properly within the button
                action ShowMenu("Leaderboard", variables)

style st_score_points_text:
    size 28 
    bold True 
    xalign 0.5

style st_score_variables_points_text:
    size 48 
    bold True 
    xalign 0.5

style st_leaderboard_text:
    xalign 0.5

style st_leaderboard_header is st_leaderboard_text:
    size int(gui.text_size * 1.4)
    bold True

style st_leaderboard_box:
    align (0.5, 0.5)
    spacing 5

style st_leaderboard_col1:
    xsize 400
    xalign 0.5

style st_leaderboard_col2 is st_leaderboard_col1:
    xsize 200

style st_leaderboard_button:
    background Solid("#ffffff99")
    hover_background Solid("#ffffff66")
    xsize 200

style st_leaderboard_button_text:
    xalign 0.5

style st_tutorials_text:
    size 30
    xalign 0.5
    yalign 0.5

style st_backandnext_buttons:
    xpos 200
    ypos 900

transform Back_button:
    xalign 1.0
    yalign 1.0
    xoffset -200  
    yoffset 100
    xsize 200
    ysize 200

transform Next_button:
    xalign 1.0
    yalign 1.0
    xoffset -100  
    yoffset 100
    xsize 200
    ysize 200

style st_go_back_button_text:
    size 30
    bold True 
    xalign 0.5

screen material_selection(correct_items, all_items, tutorial_info=None):
    modal True
    zorder 200
    default selected = set()

    $ selected_len = len(selected)
    $ max_selected = selected_len >= 5
    if tutorial_info:
        frame:
            anchor (1.0, 0.0)
            pos (1.0, 0.0)
            offset (-10, 10)
            button:
                text "See Tutorial again":
                    hover_color "#cca484"
                action ShowMenu("tutorial1", tutorial_info=tutorial_info)
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30
        background Solid("#ac897eb9")
        
        vbox:
            spacing 20
            label "{color=#00000c} {b} Select the correct materials:" xalign 0.5
            
            # Display the number of selected items
            text "Selected: [selected_len]/5" xalign 0.5
            
            vpgrid:
                cols 3
                spacing 40
                for item in all_items:
                    button:
                        # Disable the button if the selection limit is reached and the item is not already selected
                        action If(
                            not max_selected or item in selected,
                            ToggleSetMembership(selected, item),
                            None
                        )
                        selected_background "#CCFFCC"
                        xfill True
                        xsize 200
                        ysize 200
                        sensitive (not max_selected or item in selected)  # Disable button if limit is reached
                        if persistent.admin and item in correct_items:
                            frame:
                                background Solid("#f5eaeaff")
                                xalign 0.5
                                xysize (1.0, 1.0)
                                frame:
                                    background Solid("#ff000079")
                                    xalign 0.5
                                    xysize (1.0, 1.0)
                        vbox:
                            xalign 0.5
                            spacing 5
                            add materials[item]:
                                xalign 2
                                ysize 150
                                fit "contain"
                            text item:
                                xalign 0.5
                                text_align 0.5
                                size 35
            
            vbox:
                spacing 10
                xalign 0.5
                hbox:
                    xalign 0.5
                    textbutton "{color=#f5eaeaff} {b} Submit":
                        sensitive max_selected
                        action [Return(selected), Hide("material_selection")]
                        xalign 0.5
                if persistent.admin:
                    hbox:
                        spacing 30
                        xalign 0.5
                        textbutton "{color=#009900}Skip (correct){/color}":
                            action [Return(correct_items), Hide("material_selection")]
                            xalign 0.5
                        textbutton "{color=#990000}Skip (incorrect){/color}":
                            action [Return(set()), Hide("material_selection")]
                            xalign 0.5

screen tutorial1(tutorial_info):
    tag tutorials

    default current_page = 0

    $ tutorial_info_page = tutorial_info[current_page]

    frame:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        background Solid("#141414fd")
        xysize (800, 600)
        
        hbox:
            xalign 0.1
            xoffset 630
            yalign 1.0
            imagebutton:
                idle "Back_Button.png" at Back_button
                if current_page > 0:
                    action SetScreenVariable("current_page", current_page - 1)
                else:
                    idle "Back_Button.png" at Back_button
                    action Return()

        hbox:
            xalign 1.0
            xoffset 200
            yalign 1.0
            imagebutton:
                if current_page < len(tutorial_info) - 1:
                    idle "Next_Button.png" at Next_button
                    action SetScreenVariable("current_page", current_page + 1)
                else:
                    idle "Next_Button.png" at Next_button
                    action Return()
            
        
        frame:
            anchor (0.5, 0.5)
            pos (0.5, 0.5)
            xysize (700, 500)
            background Solid("#1d1d1db6")
        
        frame:
            pos (0.5, 0.0)
            anchor (0.5, 0.5)
            background Solid("#ffffffff")
            
            frame:
                xalign 0.5
                background Solid("#b6b3b3")
                hbox:
                    text "Tutorial 1" style "st_leaderboard_header"
                    xalign 0.5
                    offset (3, 0)
                    yalign -0.1

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            for info_text in tutorial_info_page:
                text info_text

screen Backbutton:
    frame:
        anchor (0.0, 1.0)
        pos (0.0, 1.0)
        xoffset 30
        background Frame("lined_paper.png")
        xysize (200, 100)
        textbutton "Go Back":
            style "st_go_back_button_text"
            action Rollback()
            xalign 0.5
            yalign 0.5 
            text_color "#000000"
            



        
    


            
    
        



