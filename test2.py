import math
def process_nums (func) :
    try:
        final_nos=list(map (lambda x:math.pow(x,2) , func))
        convert_nums=[math.ceil (1.5*x) for x in final_nos]
        return convert_nums
    except Exception as e:
        print (e)
def numbers (nums) :
    return nums
print(process_nums(numbers([num for num in range(5)])))