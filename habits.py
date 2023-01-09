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
    def __init__(self, name, category, frequency = 0, mark='', description=""):
        self.name = name
        self.category = category
        self.frequency = frequency
        self.mark = mark
        self.description = description

class Action(Habit):
    def __init__(self, time_in, time_out, location, description=""):
        self.location = location
        self.time = {"in":time_in, "out":time_out}
        self.description = description

    def time_interval(self):
        if self.time['in'].day != self.time['out'].day:
            return (240000-int(str(self.time['in'].intify())[6:]))+int(str(self.time['out'].intify())[6:])
        return self.time["out"].intify()-self.time["in"].intify()

class Habit_Card:
    def __init__(self, habit_list, date):
        self.habit_list=habit_list
        self.date = date
        self.score = [x.mark for x in habit_list].count('+')/len(habit_list)

def get_data(filename):
    with open(filename, "r") as file:
        txt = file.read()
    return [x.split(';') for x in txt.split('\n')]

def get_spending_list(data):
    all_categories = set(x[1] for x in data if x[0]=='Spend')
    spendings = {x:0 for x in all_categories}
    all_spendings = [(x[1],x[2]) for x in data if x[0]=='Spend']
    for spending in all_spendings:
        spendings[spending[0]]+=float(spending[1].replace(',','.'))
    return spendings

def calculate_spendings(spending_list):
    s=0
    for x in spending_list:
        s+=spending_list[x]
    return s

def cash_out(filename):
    return calculate_spendings(get_spending_list(get_data("doing.txt")))

def cash_in(filename):
    data = get_data(filename)
    s = 0
    for line in data:
        if line[0]=="Cash-in":
            s+=(float(line[1].replace(',', '.')))
    return s

def money_left(filename):
    return cash_in(filename)-cash_out(filename)

def max_spent(filename):
    spending_list = get_spending_list(get_data(filename))
    c,max=0,""
    for x in spending_list:
        if c<spending_list[x]:
            max=x
            c=spending_list[x]
    return max,c

def min_spent(filename):
    spending_list = get_spending_list(get_data(filename))
    c,min=max_spent(filename)[1],""
    for x in spending_list:
        if c>spending_list[x]:
            min=x
            c=spending_list[x]
    return min,c

def counted_spendings(filename):
    data = get_data(filename)
    

print(max_spent("doing.txt"))









