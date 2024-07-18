
def winner(first,second):
    posible_m = ['rock','paper', 'scissors']
    if first not in posible_m:
        return 'invalid'
    if first == 'paper':
        if first == second:
            return 'draw'
        elif second == 'rock':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ first
        elif second == 'scissors':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ second

    elif first== 'rock':
        if first == second:
            return 'draw'
        elif second == 'paper':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ second
        elif second == 'scissors':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ first
   
    elif first== 'scissors':
        if first == second:
            return 'draw'
        elif second == 'paper':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ first
        elif second == 'rock':
            return 'winner '+ '('+first+ ' '+ second+')'+ '== '+ second

move = input('WHat will it be: ')
print(winner(move, 'scissors'))
