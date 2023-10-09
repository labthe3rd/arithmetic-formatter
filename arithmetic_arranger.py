import re

def arithmetic_arranger(problems,answer=False):
  #return error if more than 5 problems supplied
    print("answer is coming in as ", answer)
    if(len(problems) > 5):
      return "Error: Too many problems."
    var_problem = []
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for count,problem in enumerate(problems):
        x = re.split("\s",problem)
        #determine answer
        a = 0

        try:
            if x[1] == "-":
                a = int(x[0]) - int(x[2])
            if x[1] == "+":
                a = int(x[0]) + int(x[2])
            if x[1] != "+" and x[1] != "-":
                return "Error: Operator must be '+' or '-'."
            x.append(str(a))
            print(x)
            
            #Determine the digits for each number
            d1 = len(x[0])
            d2 = len(x[2])
            
            if d1 > 4 or d2 > 4:
                return "Error: Numbers cannot be more than four digits."
            
            #Determine spaces needed for each number
            #s1 always starts with 2 spaces since it is not next to the operator
            s1 = 2
            #s2 always starts with 1 space since it is next to the operator
            s2 = 1
            if d1 > d2:
                s2 = s2 + (d1-d2)
            if d2 > d1:
                s1 = s1 + (d2-d1)
            
            #create variable that holds all the spaces for num1 and num2
            s1_group = " "*s1
            s2_group = " "*s2
                
            #Determine number of dashes needed. Start with two then we will add the length of the largest number, or any number if the lengths are the same
            dash_num = 2
            if d1 > d2:
                dash_num = dash_num + d1
            if d2 > d1:
                dash_num = dash_num + d2
            if d1 == d2:
                dash_num = dash_num + d1
                
            #Create variable that holds all the dashes
            dash_group = "-"*dash_num
            print(dash_group)
            #Now let us attempt to format the number
            if count != 0:
                line1 = line1 + "    "
                line2 = line2 + "    "
                line3 = line3 + "    "
            line1 = line1 + s1_group + x[0]
            line2 = line2 + x[1] + s2_group + x[2]
            line3 = line3 + dash_group
            output = s1_group + x[0] + "\n" + x[1] + s2_group + x[2] + "\n" + dash_group
            
            #Handle if the answer is requested
            if answer == True:
                #Determine the number of spaces needed if there is an answer
                d3 = len(x[3])
                s3 = 2
                #If the answer is less than zero we need to reduce the default space by 1 to account for the negative sign
                if int(x[3]) < 0:
                    s3 = 1
                if d3 > d1 and d3 > d2:
                    s3 = 1
                if d1 > d2:
                    if d1 > d3:
                        s3 = s3 + (d1-d3)
                if d2 > d1:
                    if d2 > d3:
                        s3 = s3 + (d2-d3)
                if d2 == d1:
                    if d1 > d3:
                        s3 = s3 + (d1-d3)
                
                #Determine spacing grup for answer
                s3_group = " "*s3
                if count != 0:
                    line4 = line4 + "    "
                line4 = line4 + s3_group + x[3]
                #Now let us attempt to format the number
                output = s1_group + x[0] + "\n" + x[1] + s2_group + x[2] + "\n" + dash_group + "\n" + s3_group + x[3]
            print(output)
            var_problem.append(output)
            
            
            
        except:
            return "Error: Numbers must only contain digits."
    answer_raw = var_problem
    print("Answer is...")
    print(answer_raw)
    
    #Now we need to split all the answers into 4 lines
    arranged_problems = line1 + "\n" + line2 + "\n" + line3
    if answer == True:
        print("answer is true")
        arranged_problems = arranged_problems + "\n" + line4
    
    print(arranged_problems)
    #output the formatted answer
    return arranged_problems
