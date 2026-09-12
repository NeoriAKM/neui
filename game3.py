import neui, random

x = 0
y = 0
x1 = 0
y1 = 0

main = neui.Draw(100, 25, 15)

main.add((x,  y,  '#', 1))
main.add((x1, y1, '@', 2))

while True: # main cycle
    try:

        x += random.randint(-1, 1)
        y += random.randint(-1, 1)

        x1 += random.randint(-1, 1)
        y1 += random.randint(-1, 1)

        # making him stay in land
        x = max(0, min(x, main.w-1))
        y = max(0, min(y, main.h-1))
        x1 = max(0, min(x1, main.w-1))
        y1 = max(0, min(y1, main.h-1))

        main.draw()

        main.move(1, x , y )
        main.move(2, x1, y1)


    except KeyboardInterrupt:
        main.endsession("byebye.")