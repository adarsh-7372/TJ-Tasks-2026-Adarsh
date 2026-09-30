while True:
    study_hours = input("Enter the study hours b/w 0-24 :  ")
    attendance = input("Enter the attendance b/w 0-100 :  ")

    try:
        st_raw = float(study_hours)
        att_raw = float(attendance)
        
        if 0 <= st_raw <= 24 and 0 <= att_raw <= 100:
            st = st_raw
            att = att_raw
            break
        else:
            print(f"\n{"-"*30}Enter the value in range.{"-"*30}\n")
        

    except ValueError:
        print(f"\n{"-"*30}Enter valid input!!!!{"-"*30}\n")
    
def Perceptron(attendance, study_hours):

    w1 , w2 , bias = 3.5 , 2.0 , -3.0

    x1 = study_hours / 24
    x2 = attendance / 100

    weighted_sum = (x1 * w1) + (x2 * w2) + bias
    if weighted_sum >= 0:
        return 1
    else:
        return 0

print(Perceptron(att, st))