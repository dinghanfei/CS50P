str = input("Expression: ")
exp = str.strip()
exp_list = exp.split()
num1 = int(exp_list[0])
op = exp_list[1]
num2 = int(exp_list[2])
match op:
    case "+":
        ans = num1 + num2
    case "-":
        ans = num1 - num2
    case "*":
        ans = num1 * num2
    case "/":
        ans = num1 / num2
print('%.1f' %ans) 
