def solution(xs):
    # edge cases
    if (len(xs)==0):
        return str(0)
    if (len(xs)==1):
        return str(xs[0])

    # find, sort, count pos and neg values in array
    pos_list = []
    neg_list = []
    for n in xs:
        if n > 0: pos_list.append(n)
        if n < 0: neg_list.append(n)
        
    pos_count = len(pos_list)
    neg_count = len(neg_list)

    # edge case for only one negative number
    if neg_count == 1 and pos_count == 0:
      return str(xs[0])
      
    # edge case for no numbers, shouldn't ever get here 
    if neg_count == 0 and pos_count == 0:
      return str(0)

    # multiply values
    power_output = 1
    for n in pos_list:
        power_output *= n

    if neg_count % 2 == 1:
        neg_list.remove(max(neg_list))
        
    for n in neg_list:
        power_output *= n

    return str(power_output)

test1 = [2,2,0,2,0]
test2 = [-2,-3,4,-5]
