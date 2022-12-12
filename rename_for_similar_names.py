import os

for (dirpath, dirnames, filenames) in os.walk("."):
    for filename in filenames:
        if filename.split(".")[1] == "pdf":
            split_arr = filename.split("_")
            # wenn mittelname noch gebraucht einfach counter und arr[2] noch zufuegen
            os.rename(filename, split_arr[0] + "_" + split_arr[1] + ".pdf")
    break
