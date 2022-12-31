class Date:
    def __init__(self, second, minute, hour, day, month, year):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.day = day
        self.month = month
        self.year = year

    def stringify(self):
        result, s = [], ""
        for x in [self.second, self.minute, self.hour, self.day, self.month, self.year]:
            s = "0"+str(x)
            result.append(s[-2]+s[-1])
        return ":".join(result[:3][::-1])+" "+"-".join(result[3:])
    
    def intify(self):
        d = self.stringify().split(' ')[1]
        t = self.stringify().split(' ')[0]
        d = ''.join(d.split('-')[::-1])+''.join(t.split(':'))
        return int(d)

class Habit:
    def __init__(self, name, category, time_in, time_out, frequency = 0, mark='', location=''):
        self.name = name
        self.category = category
        self.frequency = frequency
        self.mark = mark
        self.location = location
        self.time = {"in":time_in, "out":time_out}

    def time_interval(self):
        if self.time['in'].day != self.time['out'].day:
            return (240000-int(str(self.time['in'].intify())[6:]))+int(str(self.time['out'].intify())[6:])
        return self.time["out"].intify()-self.time["in"].intify()0

class Habit_Card:
    def __init__(self, habit_list, date):
        self.habit_list=habit_list
        self.date = date
        self.score = [x.mark for x in habit_list].count('+')/len(habit_list)
    
h = Habit("Sleep", "Genuin Health Obligatory", Date(0,30,23,1,1,2023), Date(0,30,6,2,1,2023), 1, "+", "Home Bedroom")
print(h.time_interval())