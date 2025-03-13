import math

texts = {1: ["Test", 1, 0], 3: ["This is some random s*** that doesn't matter", 0, 0], 5: ["", 0, 1], 7: ["This is badly centered text", 1, 0]}
wm_height = 29
wm_width = 120

inner_wm_height = 20
inner_wm_width = 69

while True:
    print("\n" * math.floor(wm_height / 2 - inner_wm_height / 2 - 1))
    
    print(" " * round(wm_width / 2 - inner_wm_width / 2), '=' * inner_wm_width)
    index=0
    for i in range(inner_wm_height - 2):
        index += 1
        if index in texts:
            if texts[index][1] == 1:
                    print(" " * (wm_width // 2 - inner_wm_width // 2), '=' + " " * ((inner_wm_width - len(texts[index][0]) - 2) // 2) + texts[index][0] + " " * (inner_wm_width - 3 - len(texts[index][0]) - (inner_wm_width - len(texts[index][0]) - 2) // 2), "=")
            elif texts[index][2] == 1:
                print(" " * round(wm_width / 2 - inner_wm_width / 2), '= ' + "=" * (inner_wm_width - 4) + " =")
            else:
                print(" " * round(wm_width / 2 - inner_wm_width / 2), '= ' + texts[index][0] + " " * (inner_wm_width - 3 - len(texts[index][0])) + "=")
        else:
            print(" " * round(wm_width / 2 - inner_wm_width / 2), '=' + " " * (inner_wm_width - 2) + "=")
    print(" " * round(wm_width / 2 - inner_wm_width / 2), '=' * inner_wm_width)
    
    print("\n" * math.floor(wm_height / 2 - inner_wm_height / 2))
    input()
