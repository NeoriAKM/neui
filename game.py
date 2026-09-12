import neui

# base variables to spam a '#'
x = 0
y = 0
id = 1

main = neui.Draw(50, 25, 15)
# 50 is miliseconds between frame
# 25 and 15 - width height of display

main.add_ui((0, 2, f"x: {x}", 1))   # making UI with pos - left and 2 row, info with x and UI-ID=1
main.add_ui((1, 2, f"row: {y}", 2)) # one more.

while True: # main cycle
    main.draw() # drawing a frame
    main.add((x, y, '#', id)) # creating new '#' and placing it

    x += 1
    id += 1

    if main.isempty(main.w - 1, y) == True: # moving y to down
        y += 1
        x = 0
    
    # Updating UI. fact: we could do this a better. How? Just make new variable content1 and content2
    main.update_ui(f"x: {x}", 1)
    main.update_ui(f"row: {y}", 2)