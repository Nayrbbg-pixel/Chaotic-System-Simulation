import random

def luck_skill(applicants_num:int):
    data = {}
    for i in range(1,applicants_num):
        data[str(i)]= {
            'skills':random.randint(30,99),
            'luck':random.randint(1,5)
        }
    return data

def make_decision(data:dict):
    col1 = {}
    vals =[] 

    for s in range(1,len(data)+1,1):
        cal = (data[str(s)]['skills'] + data[str(s)]['luck'])/105*100
        col1[str(s)]= cal
        vals.append(cal)

    sorted_out_data = sorted(vals,reverse=True)

    for p in range(1,10):
        z=sorted_out_data[p]
        for x in col1:
            if col1[str(x)] == z:
                name= str(x)
                skills = data[name]['skills']
                luck = data[name]['luck']
        
        print(f"Candidate no. - {name}\nMaths Percentage of skill and luck(100 points for skill and 5 points for luck) - {sorted_out_data[p]}\
\nskills - {skills}\nluck - {luck}\n\n")


def make_action():
    data = luck_skill(100)
    make_decision(data)

make_action()
exit()
