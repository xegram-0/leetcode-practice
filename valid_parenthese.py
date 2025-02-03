def checkValid(theString:str):
    stack:list = []
    parentheseHashMap:dict = {')':'(',']':'[','}':'['}

    for char in theString:
        if char in parentheseHashMap:
            if stack and stack[-1] == parentheseHashMap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False
def main():
    s1:str = "()"
    s2:str = "()[]"
    s3:str = "()[]{}" # what???
    s4:str = "((((((())))))"
    print(checkValid(s4))
if __name__ == "__main__":
    main()