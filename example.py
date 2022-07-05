import TaggedTimeLine as tt
from time import sleep

def ex_noloop():
    print(":::: Example Without Loop ::::")
    print(" My Daily Routine")

    tag_time = tt.TaggedTimeLine()

    print("sleeping...");sleep(1);tag_time.check(tag ="1. sleep")
    print("having a lunch...");sleep(1.3);tag_time.check(tag = "2. have lunch")
    print("studying python...");sleep(1);tag_time.check(tag = "3. study python")
    print("attending a lecture...");sleep(2);tag_time.check(tag = "4. attend a lecture")
    print("having a dinner...");sleep(1);tag_time.check(tag = "5. have dinner")

    print("\n-- print all --")
    tag_time.print_all()

    
    print("\n-- print tag --")
    tag_time.print_tag("5. have dinner")

    
    print("\n-- print interval --")
    tag_time.print_interval("2. have lunch","5. have dinner" )
    print()


def ex_loop():    
    print(":::: Example With Loop ::::")
    print(" My Daily Routine")

    tag_time = tt.TaggedTimeLine(cnt_limit = 3-1)
    while True:
        tag_time.start() # !Impoortant! call start on the top of the loop
        print("\n! loop !")

        print("sleeping...");sleep(1);tag_time.check(tag ="1. sleep")
        print("having a lunch...");sleep(1.3);tag_time.check(tag ="2. have lunch")
        print("studying python...");sleep(1);tag_time.check(tag="3. study python")
        print("attending a lecture...");sleep(2);tag_time.check(tag ="4. attend a lecture")
        print("having a dinner...");sleep(1);tag_time.check(tag ="5. have dinner")
 
        isStopping = tag_time.accumulate(increment = 1) # !Important! 

        print("-- print all --")
        tag_time.print_all()

        # you can add print_tag or print_interval here
        # print("\n-- print tag --")
        # tag_time.print_tag("5. have dinner")
        # print("\n-- print interval --")
        # tag_time.print_interval("2. have lunch","5. have dinner" )

        if(isStopping):
            break

    print("\n-- print avg --")
    tag_time.print_avg(delimiter = "\n      ")
    print()

if __name__ == "__main__":
    ex_noloop()
    ex_loop()
