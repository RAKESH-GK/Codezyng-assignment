# program that helps users to keep track of their daily water intake and reminds them to stay hydrated.

import time # time module used in this program to get time

# total timeline 6 mins in seconds
total_seconds = 6 * 60 
# secments of 3 mins in seconds
segment_seconds = 3 * 60 
# reminder seconds to reminde user
reminder_seconds = 20

#initializing y and n counts to 0
count_Y = 0
count_N = 0

# geting start time
start_time = time.time()

print("\nWaterintake Tracker")

# running loop until completion of 6 mins timeline
while((time.time() - start_time) < total_seconds):

    # getting current time
    time_now = time.localtime() 

    # checking which segment it is
    if((time.time() - start_time ) < segment_seconds):
        segment=1
    else:
        segment=2
    
    if(int(time.time() - start_time) % reminder_seconds == 0):

        if(time_now.tm_hour>12):
            current_time=time_now.tm_hour-12
        else:
            current_time=time_now.tm_hour

        print("\n--------------------------------------------------------------")
    
        print(f"[Current Time {current_time}:{time_now.tm_min}:{time_now.tm_sec}] Segment ({segment}) reminder ({count_N + count_Y + 1})")
        status = input("Did you drink water (Y/N):")

        # make 1 seconds delay to avoid continous reminder
        time.sleep(1)

        # counting y and n
        if(status.upper() == "Y"):
            count_Y += 1
        else:
            count_N += 1

        # checking for next reminder or result
        if(int(time.time() - start_time)<total_seconds and count_N + count_Y < 18):
            print("Next reminder will come soon...")
        else:
            # printing final result
            print("\n----------------water consumption analysis--------------------\n")
            print(f"total {count_Y} times you drinked water today")
            print("status : ",end = " ")
            if(count_N > count_Y):
                print("Poor! Drink water to stay healthy")
            elif(count_Y >= 15):
                print("You are Great!")
            elif(count_Y >= 9):
                print("Good! Keep it up")
            else:
                print("Improvement needed to stay healthy")
            break
    
print("\n--------------------------------------------------------------")
            

            





