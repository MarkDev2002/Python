


class Student:
    def __init__(self, name, number):
        self.score = [0] * number
        self.name = name
        self.number = number

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_score(self, i):
        return self.score[i]

    def inputScore(self):
        for i in range(self.number):
            print("Nhap diem mon thi", format(i + 1),":") 
            self.score.append(int(input()))

    def getAverage(self):
        return sum(self.score)/self.number

    def getHighScore(self):
        max = self.score[0]
        for i in range(1, self.number):
            if(self.score[i] > max):
                max = self.score[i]
        return max

    def scholarshipCheck(self):
        if(self.getAverage >= 8.0):
            for i in self.score:
                if(i < 4):
                    return False
            return True
        else:
            return False

    def __str__(self):
        return "Name : {} , score = {} ".format(self.name, self.getAverage())


s = str(input("Nhap ten : "))
sub = int(input("Nhap so mon thi : "))
s1 = Student(s, sub)
s1.inputScore()
print(s1.__str__())
