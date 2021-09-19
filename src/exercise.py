def main():
    #write your code below this line
    sum = 0
    count = 0
    
    while True:
        num = int(input(''))
        
        if num == 0:
            break
            
        if num > 0:
            count += 1
            sum += num
        
    if sum == 0:
        print('Cannot calculate the average')
    else:
        print(sum/count)
        


if __name__ == '__main__':
    main()
