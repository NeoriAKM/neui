import neui, random

x = 0
y = 0
id = 1
id2 = 1000

main = neui.Draw(50, 25, 15)

main.add_ui((0, 2, f"x: {x}", 1))
main.add_ui((1, 2, f"row: {y}", 2))

while True: # main cycle
    try:
        main.draw() # drawing a frame
        main.add((x, y, '#', id))
        if random.random() > 0.5:
            main.add((random.randint(0, main.w), random.randint(0, main.h), '@', id2))

        x += 1
        id += 1
        id2 += 2

        if main.isempty(main.w - 1, y) == True: # moving y to down
            y += 1
            x = 0
        
        main.update_ui(f"x: {x}", 1)
        main.update_ui(f"row: {y}", 2)
    except KeyboardInterrupt:
        main.endsession("Goodbye!")