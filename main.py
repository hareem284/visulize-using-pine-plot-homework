#sorry i was sick so i might have not done some parts but i think i did them all

import matplotlib.pyplot as py
day=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
birth=[1,3,19,7,17,12,10]
py.plot(day,linestyle='dashdot',marker='1')
py.plot(birth,linestyle='',marker=7)
py.title("CHECKING ALL THE BIRTHS IN THE WEEK")
py.xlabel("day")
py.ylabel("birth")
py.legend()
py.show()