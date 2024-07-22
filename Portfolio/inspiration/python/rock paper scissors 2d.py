#back when I was in a nice environment :
def winner(move,second):
    posible_m = ['rock','paper', 'scissors']
    if move not in posible_m:
        return 'invalid'
    if move == 'paper':
        if move == second:
            return 'draw'
        elif second == 'rock':
            return 'winner '+ '('+move+ ' '+ second+')'+ '== '+ first
        elif second == 'scissors':
            return 'winner '+ '('+move+ ' '+ second+')'+ '== '+ second

    elif move== 'rock':
        if move == second:
            return 'draw'
        elif second == 'paper':
            return 'winner '+ '('+move+ ' '+ second+')'+ '== '+ second
        elif second == 'scissors':
            return 'winner '+ '('+move+ ' '+ second+')'+ '== '+ first
   
    elif first== 'scissors':
        if first == second:
            return 'draw'
        elif second == 'paper':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ first
        elif second == 'rock':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ second
##
move = input('What will it be: ')
print(winner(move, 'scissors'))
