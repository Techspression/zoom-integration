import mss
import mss.tools
import time

with mss.mss() as sct:
    # Get information of monitor 2
    time.sleep(6)
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    monitor = {
        "top": mon["top"] + 100,  # 100px from the top
        "left": mon["left"] + 100,  # 100px from the left
        "width": 500,
        "height": 500,
        "mon": monitor_number,
    }
    monitor2 = {
        "top": mon["top"] + 100,  # 100px from the top
        "left": mon["left"] + 100,  # 100px from the left
        "width": 150,
        "height": 900,
        "mon": monitor_number,
    }
    output = "sct-mon{mon}_{top}x{left}_{width}x{height}.png".format(**monitor)
    output2 = "sct-mon{mon}_{top}x{left}_{width}x{height}2.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    sct_img2 = sct.grab(monitor2)
    mss.tools.to_png(sct_img2.rgb, sct_img.size, output=output2)
    print(output)