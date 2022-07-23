#!/usr/bin/python3

'''
《计算之魂》 思考题2.3 Q1
写出简单计算器的伪代码

author: Jack Lee
Date:   July 23, 2022
'''

'''
simple calculator routine with STACK
simple_calc( s_in: list ) -> result: int, success: boolean 
para:
    s_in: input string
'''

def _calc_top3( s ):
    if len(s) == 1: return s[0], True
    if len(s) == 2: return 0, False

    operand2 = s.pop()
    op = s.pop()
    operand1 = s.pop()
    result = 0.0

    match op:
        case '+':
            result = float(operand1) + float(operand2)
        case '-':
            result = float(operand1) - float(operand2)
        case '*':
            result = float(operand1) * float(operand2)
        case '/':
            if float(operand2) != 0.0:
                result = float(operand1) / float(operand2)
            else: 
                return 0, False

    return result, True


def simple_calc( s_in ):
    stack_calc = []
    dict_op = { '+': 0, '-': 1, '*':2, '/':3, '=':4 }
    op_plus_minus = ('+', '-')
    op_multiple_div = {'*', '/'}
    top_op = ''
    result = 0.0

    for x in s_in :
        # if x is operator +-*/=
        if x in dict_op :
            # if no op, push in stack
            if top_op == '' :
                top_op = x
                stack_calc.append(x)
            elif (top_op in op_plus_minus) and (x in op_multiple_div):
                #if top_p in '+,-'; x in '*, /', push do not calc
                stack_calc.append(x)
                top_op = x
            else :
                result, success = _calc_top3(stack_calc)
                if success != True :
                    return 0.0, False
                
                # push result and op into stack
                stack_calc.append(str(result))
                if x != '=' :
                    stack_calc.append(x)
                    top_op = x
                else:
                    # the end
                    return _calc_top3(stack_calc)
        else:   
            # numbers, if top_op is *, /, just do it
            if top_op in op_multiple_div:
                op = stack_calc.pop()
                operand1 = stack_calc.pop()
                operand2 = x
    
                match op:
                    case '*':
                        result = float(operand1) * float(operand2)
                    case '/':
                        if  float(operand2) != 0.0:
                            result = float(operand1) / float(operand2)
                        else: 
                            return 0, False
                top_op = stack_calc[-1]
                stack_calc.append(str(result))
            else:
                stack_calc.append(x)


'''
    test function
'''
if __name__ == "__main__":
    
    sample1 = ['5', '+', '4', '-', '2', '=']
    sample2 = ['5', '-', '4', '*', '3', '/', '4', '=']
    sample3 = ['5', '-', '4', '*', '3', '/', '4', '+', '10', '*', '2', '=']

    print(sample1, simple_calc(sample1))
    print(sample2, simple_calc(sample2))
    print(sample3, simple_calc(sample3))
