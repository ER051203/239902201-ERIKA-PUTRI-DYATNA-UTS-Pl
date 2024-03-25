print("--MEMBUAT PROGRAM YANG MENGHITUNG DAN MENYIMPAN TB DAN BB DALAM METRIK--")

class BMI:
    def __init__(self, berat_lb: float, tinggi_ft: float):
        self.berat_lb = berat_lb
        self.tinggi_ft = tinggi_ft

    @property
    def berat_lb(self):
        return self._berat_lb

    @berat_lb.setter
    def berat_lb(self, berat):
        if not isinstance(berat, (int, float)) or berat <= 0:
            raise ValueError("berat (in pounds) must be a positive number.")
        self._berat_lb = berat

    @property
    def tinggi_ft(self):
        return self._tinggi_ft

    @tinggi_ft.setter
    def tinggi_ft(self, tinggi):
        if not isinstance(tinggi, (int, float)) or tinggi <= 0:
            raise ValueError("tinggi (in feet) must be a positive number.")
        self._tinggi_ft = tinggi

    def bmi_value(self) -> float:
        berat_kg = self.berat_lb * 0.453592
        tinggi_m = self.tinggi_ft * 0.3048
        return round(berat_kg / (tinggi_m ** 2), 2)

    def __eq__(self, other):
        if not isinstance(other, BMI):
            return NotImplemented
        return self.berat_lb == other.berat_lb and self.tinggi_ft == other.tinggi_ft

# Usage example:

p1 = BMI(150, 6.0)
p2 = BMI(150, 6.7)

print(f"BMI of person 1: {p1.bmi_value()}")
print(f"BMI of person 2: {p2.bmi_value()}")

if p1 == p2:
    print("Person 1 and Person 2 memiliki berat dan tinggi yang sama.")
else:
    print("Person 1 and Person 2 memiliki berat dan tinggi yang berbeda.")