def string_repeater():
    "Functions repeats a string 10 times"
        
    repeat_statement = "I will never spam my friends again."
    
    for i in range(10):
        print(i+1,"-", repeat_statement)

def main():
    "Test function that repeats sentence 10 times"
    
    # Call function that repeats sentence.
    string_repeater()
    
    
if __name__ == '__main__': main()    
