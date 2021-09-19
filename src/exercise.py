def main():
    #write your code below this line
    sum = 0
    positive = 0
    
    while True:
        num = int(input(''))
        
        if num == 0:
            break
        if num > 0:
            positive += 1
            
        
        sum += num
        
    if sum == 0:
        print('Cannot calculate the average')
    elif sum != 0 and positive != 0:
        print(sum/positive)
        


if __name__ == '__main__':
    main()
