n=int(input())
fingers=['Thumb','Index','Middle','Ring','Pinky']

finger_day=fingers[(n-1)%5]

print(finger_day)