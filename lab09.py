# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first): loop through the integers twice,
    # once on the outside which goes through each number of list
    # second one checks each number ahead of it to find the sum of the integer
    # if arr(i) + arr(j) is equal to target then return [i,j]
    #   ...

    for i in range(len(nums)):
        print(i)
        for j in range(i+1,len(nums)):
            if (nums[i]+nums[j])==target:
                return [i,j]


    return None

def max_profit(prices):
    # Outline: loop through the list twice, once on the outside checking each price,
    # then the second one checking prices ahead, if none of the prices ahead are larger
    #move onto the next index and check. If a number is larger then your current number
    #keep searching through the list to check and see if there are any numbers even larger
    #then return that number
    #   ...

    index = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]<prices[j]:
                index=j

        if index!=0:
            return index

    return index


def max_subarray(nums):
    # Outline: loop through the list three times, the first one checks each index,
    #then in the second one you go through the list again
    #then you add up the sums in for the index i your on and you get every sum
    #removing the last element each time
    #   ...

    largest = nums[0]
    sum:int
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum=0
            for k in range(i, len(nums)-j+i):
                sum+=nums[k]

            if largest<sum:
                largest=sum



    return largest


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline: check to see which bracket you were on last and then if the next closed
    #bracket is not the right one you return false
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    myList = []
    for i in range(len(s)):
        if(s[i]=='(' or s[i]=='{' or s[i]=='[' ):
             print("test 1")
             myList.append(s[i])
        elif myList:
            print("test 2")
            if (s[i] == ')'):
                if not myList[len(myList)-1]=='(':
                    return False
                else:
                    myList.pop(len(myList)-1)

            elif (s[i] == "}"):
                if not myList[len(myList)-1]=="{":
                    return False
                else:
                    myList.pop(len(myList)-1)
            elif (s[i] == "]"):
                if not myList[len(myList)-1]=="[":
                    return False
                else:
                    myList.pop(len(myList)-1)
        else:
            print("test 3")
            return False

    if myList:
        return False
    return True


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(is_balanced("("))
    pass


if __name__ == "__main__":
    main()
