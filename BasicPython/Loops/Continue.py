
while True:


    line = input(">")

    if line[0] == "#":

        #With this command we go back to the beginning of the loop again.
        continue

    if line == "done":

        break

    print (line)

print ("Done!")
