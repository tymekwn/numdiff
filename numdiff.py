### NumDiff - An esolang conceptualised and programmed by Tymoteusz Niewodniczański ###
### Yes, it is a BrainF**k derivative ###

def execute(filename):                                  #Function to read code from file
    with open(filename, "r") as f:
        algo = f.read()                                 
        algo = algo.split(" ")                          #Turn the code into a list of numbers
        evaluate(algo)                                  

def evaluate(algo):                                     #The main function
    
    loopmap = make_loopmap(algo)                        #Forms any loopmaps
    cell, cell_counter, ins_counter = [0],0,0           #Define needed variables

    while ins_counter < len(algo):                                      
        numdiff = int(algo[ins_counter]) - int(algo[ins_counter-1])     #Command determiner
        if numdiff == 1:
            cell_counter+=1
            if cell_counter == len(cell): cell.append(0)                #Go to next cell or create a new cell if needed
        elif numdiff == 2:
            cell_counter = 0 if cell_counter <= 0 else cell_counter -1  #Go to previous cell unless at the first cell, where you remain
        elif numdiff == 3:
            cell[cell_counter] = cell[cell_counter] + 1                 #Incrememnt cell value
        elif numdiff == 4:
            cell[cell_counter] = cell[cell_counter] - 1                 #Decrement cell value
        
        elif numdiff == 5 and cell[cell_counter] == 0: ins_counter = loopmap[ins_counter]       #Open Loop
        elif numdiff == 6 and cell[cell_counter] != 0: ins_counter = loopmap[ins_counter]       #Close Loop
    
        elif numdiff == 7:
            cell[cell_counter] = int(input("Input number"))             #Input Command
        elif numdiff == 8: print(cell[cell_counter])                    #Output Command

        ins_counter+=1                                                  #Goes to the next instruction
        #print(cell, numdiff)                                           #A way to viualise

def make_loopmap(algo):                                                 #Function to make loopmaps      
    temploopmap, loopmap = [], {}                                       
    for position in range(len(algo)):                                   
        position = int(position)                                        
        numdiff = int(algo[position]) - int(algo[position-1])           #Command determiner
        if numdiff == 5: temploopmap.append(position)                    #List the start of the loop
        if numdiff == 6:
            start = temploopmap.pop()                                   #Add the start of the loop
            loopmap[start] = position                                   
            loopmap[position] = start                                   #Adds end of loop
    return loopmap

def main():                                     #Defines main function
    execute("script.txt")                       

if __name__ == "__main__":main()                #Runs the code