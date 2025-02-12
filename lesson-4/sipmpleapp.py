while True:
    a=int(input('a='))
    b=int(input('b='))
    
    operator=input("Enter operators (+,-,*,/): ")
    if operator =='+':
        print('a+b=', a+b)
    elif operator =='-':
        print("a-b=", a-b)
    elif operator =='*':
        print('a*b=', a*b)
    elif operator=='/':
        print('a/b=',a/b)
        
    
    ans=input("Do you want to run again?")
    if ans.lower() in ['q', 'quit', 'no', 'n']:
        break
    
    

