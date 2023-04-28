#precedence function
def precedence(ch):
    if(ch == '^'):
        return 3
    elif(ch == '/' or ch =='*'):
        return 2
    elif(ch == '+' or ch == '-'):
        return 1
    else:
        return -1
#infix to postfix
def infixToPostfix(s):
    st = []
    postfix_exp = str()
    for i in range(0,len(s)):
        ch = s[i]
        #if input char is operand
        if((ch>='a'and ch<='z')|(ch>='A'and ch<='Z')):
            postfix_exp += ch
        #if inp char is (
        elif(ch == '('):
            st.append('(')
        #if inp char is )
        elif(ch == ')'):
            while(st[-1] != '('):
                postfix_exp += st[-1]
                st.pop()
            st.pop()
        #if char is an operator
        else:
            while(len(st)>0 and precedence(s[i]) <= precedence(st.peek())):
                postfix_exp += st[-1]
                st.pop()
            st.append(ch)
    #pop all the elements from stack
    while(len(st)>0):
        postfix_exp += st[-1]
        st.pop()
    return postfix_exp
s = input("enter infix exp:")
print("The postfix string is: ",infixToPostfix(s))