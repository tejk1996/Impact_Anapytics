class StudentsClass:
    def __init__(self, days):
        if type(days) == 'int':
            raise TypeError("Days argument should be of integer type")
        self.days = days

    def numberOfWayOfClasses(self):
        return len(self.listOfAttendClasses())

    def probabilityToMissGradutionCeremony(self):
        ways = self.NoAttendClasses()
        return len(ways) / self.numberOfWayOfClasses()

    def listOfAttendClasses(self):
        arr = []
        pattern = ""
        self.process(self.days, pattern, arr)
        return arr

    def process(self, days, pattern, arr):
        if days == 0:
            arr.append(pattern)
        else:
            # At any given day there are only two possibalities
            self.process(days - 1, pattern + 'A', arr)  # Absent Scenerio
            self.process(days - 1, pattern + 'P', arr)  # Present Scenerio

    def NoAttendClasses(self):
        # Filter out ways where 4 or more consective days classes are missed
        return list(filter(lambda way: "AAAA" in way, self.listOfAttendClasses()))



#"Enter No of days
days = int(input("Enter No of days:"))
solution = StudentsClass(days)
print(solution.numberOfWayOfClasses())
print(solution.probabilityToMissGradutionCeremony())