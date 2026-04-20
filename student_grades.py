class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]
        if score>= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >=70:
            return 'C'
        elif score >= 60:
            return 'D'
        elif score >= 50:
            return 'E'
        else:
            return 'F'

    def find(self, looking4):
        idxs = []
        for s in self.scores:
            if s == looking4 :
                idx = self.scores.index(s)
                idxs.append(idx)
        return idxs

    def get_sorted(self):
        self.scores = self.scores.copy()  # povodni seznam bez zmeny
        for serazeno_od_konce in range(len(numbers)):
            has_changed = False
            print(serazeno_od_konce)
            for pozice_porovnani in range(len(numbers) - 1 - serazeno_od_konce):
                if numbers[pozice_porovnani] > numbers[pozice_porovnani + 1]:
                    has_changed = True
                    numbers[pozice_porovnani], numbers[pozice_porovnani + 1] = numbers[pozice_porovnani + 1], numbers[
                        porovnani]
            if not has_changed:
                break
        return numbers
