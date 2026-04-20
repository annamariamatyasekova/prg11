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
        scores = self.scores.copy()  # povodni seznam bez zmeny
        for serazeno_od_konce in range(len(scores)):
            has_changed = False
            print(serazeno_od_konce)
            for pozice_porovnani in range(len(scores) - 1 - serazeno_od_konce):
                if scores[pozice_porovnani] > scores[pozice_porovnani + 1]:
                    has_changed = True
                    scores[pozice_porovnani], scores[pozice_porovnani + 1] = scores[pozice_porovnani + 1], scores[pozice_porovnani]
            if not has_changed:
                break
        return scores

    def main(self):
        results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
        print ("Pocet studentov:{results.count()}")
        for i, body in enumerate(results.scores):
            letter = results.get_letter (points)
            print("Student {i}: {points} points - {letter}")

        super = []
        for i, g in enumerate(self.scores):
            if g == 100:
                super.append[i]
        print("Studenti s plnym poctom: {super}")
        if __name__ == "__main__":
            main()