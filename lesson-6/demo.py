try: 
    a=int(input())
    b=int(input())
    result=a/b
    print(f"a/b={result}")

except ZeroDivisionError:
    raise ZeroDivisionError('Denominator cannot be 0')

    