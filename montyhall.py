from random import randint

def assign_doors(num_doors: int) -> tuple[int] :
    if 2 > num_doors :
        return tuple([])
    i = randint(0,num_doors-1)
    return (0,)*i+(1,)+(0,)*(num_doors-i-1)

def open_doors(doors: tuple[int], guess: tuple[int]) -> tuple[int] :
    num_doors: int = len(doors)
    assert(len(guess) == num_doors)
    result = [0]*num_doors
    while sum(result) < num_doors-2 : # until all but two doors have been opened
        i = randint(0,num_doors-1)
        if result[i] or doors[i] or guess[i] :
            continue # Monty will not open the door you have chosen or the door in front of the prize
        else :
            result[i] = 1
    return tuple(result)

def simulate(num_trials: int, num_doors: int) -> dict[str,int] :
    if 0 > num_trials:
        return tuple([])
    if 2 > num_doors :
        return tuple([])
    wins: dict[str,int] = {"switch":0,"stay":0}
    for i in range(num_trials) :
        doors = assign_doors(num_doors)
        guess = assign_doors(num_doors)
        opened = open_doors(doors,guess)
        for is_opened,is_guessed,is_prize in zip(opened,guess,doors) :
          if is_opened :
            continue
          else :
            if is_prize :
              if is_guessed :
                wins["stay"] += 1
              else :
                wins["switch"] += 1
    print(f"After {num_trials} trials of a {num_doors}-door Monty Hall problem,\n\
staying yielded {wins['stay']} prizes, and switching yielded {wins['switch']} prizes.")
    return wins

if "__main__" == __name__ :
    num_trials = int(input("How many trials? "))
    num_doors = int(input("How many doors? "))
    result = simulate(num_trials,num_doors)
    assert(sum(result.values()) == num_trials)
