import matplotlib.pyplot as plt
import numpy as np

before = [0]*4
after = [0]*4
file_path = 'D:/GitHub/python_mipt_dafe_tasks/solutions/sem02/lesson07/data/medic_data.json'
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()

        if '"before"' in line:
            if '"I"' in line or '"II"' in line or '"III"' in line or '"IV"' in line:
                if '"I"' in line and '"IV"' not in line:
                    before [0] += 1
                if '"II"' in line:
                    before[1] += 1
                if '"III"' in line:
                    before [2]+=1
                if '"IV"' in line:
                     before [3]+= 1
        
        if "after" in line:
            if '"I"' in line or '"II"' in line or '"III"' in line or '"IV"' in line:
                if '"I"' in line and '"IV"' not in line:
                    after[0]+=1
                if '"II"' in line:
                    after[1]+=1
                if '"III"' in line:
                    after[2] += 1
                if '"IV"' in line:
                     after[3] +=1


figure, axis = plt.subplots(figsize=(9, 9))

x = np.arange(4)
width = 0.35

axis.bar(x - width/2, before, width, color='cornflowerblue', edgecolor='blue')
axis.bar(x + width/2, after, width, color='lightcoral', edgecolor='red')

axis.set_ylabel('amount of people')
axis.set_title('Mitral desease stages')

plt.show()