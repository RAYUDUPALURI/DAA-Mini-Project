import random
def main():
    min_num=int(input("Enter the minimum number:"))
    max_num=int(input("Enter the maximum number:"))
    value=random.randint(min_num,max_num)
    count=1
    max_attemtps=5
    while count<=max_attemtps:
      unum=int(input("Guess a number:"))
      if(unum==value):
        print("Success!")
        break
      elif(unum>value):
        print('Too high')
      else:
        print("Too low")
      count+=1
        
    if(count>max_attemtps):
        print("You have reached maximum attemtps")
    print(f"This is value:",value)
    
main()
