# expection = an event that interrupts the flow of a program
#           (ZeroDivisionError, ValueError, IndexError, KeyError, FileNotFoundError)
#           1.try, 2. except, 3. finally, 4. else

# try:
#     # Try some code
# except Exception:
#     # Handle the exception
# finally:
#     # do some clean up
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numbers!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some clean up here!")
