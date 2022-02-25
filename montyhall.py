from random import randint

def assign_doors(num_doors) :
    if not isinstance(num_doors,int) or num_doors < 1 :
        return tuple([])
    i = randint(0,num_doors-1)
    return (0,)*i+(1,)+(0,)*(num_doors-i-1)

def open_doors(doors,guess) :
    if not isinstance(doors,tuple) :
        return tuple([])
    if not isinstance(guess,tuple) :
        return tuple([])
    num_doors = len(doors)
    if num_doors != len(guess) :
        return tuple([])
    result = [0]*num_doors
    while sum(result) < num_doors-2 : # until all but two doors have been opened
        i = randint(0,num_doors-1)
        if result[i] or doors[i] or guess[i] :
            continue
        else :
            result[i] = 1
    return tuple(result)

def simulate(num_trials,num_doors) :
    if not isinstance(num_trials,int) or num_trials < 0 :
        return
    if not isinstance(num_doors,int) or num_doors < 0 :
        return
    wins = {"switch":0,"stay":0}
    for i in range(num_trials) :
        doors = assign_doors(num_doors)
        guess = assign_doors(num_doors)
        revealed = open_doors(doors,guess)
        for door in zip(revealed,guess,doors) :
            if door[0] : # door is already open
                continue
            if door[1] : # examining guessed door
                if door[2] : # is the prize behind the guessed door?
                    wins["stay"] += 1
                continue
            if door[2] :
                if not door[1] :
                    wins["switch"] += 1
    print(f"After {num_trials} trials of a {num_doors}-door Monty Hall problem,\n\
staying yielded {wins['stay']} prizes, and switching yielded {wins['switch']} prizes.")
    return (wins[x] for x in wins)

if __name__ == "__main__" :
    num_trials = int(input("How many trials? "))
    num_doors = int(input("How many doors? "))
    result = simulate(num_trials,num_doors)
