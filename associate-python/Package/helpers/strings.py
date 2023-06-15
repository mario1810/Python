def extract_upper(phrase):
    return list(filter(str.isupper,phrase))

def extract_lower(phrase):
    return list(filter(str.islower,phrase))

if __name__ == "__main__": #thsi indicates that if this files is main(script that is executed), print the following
    print("Hello from helpers")