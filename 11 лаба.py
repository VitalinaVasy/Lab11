import random

class Patient:
    def __init__(self, surname, first_name, middle_name, address, phone, diagnosis):
        self._id = random.randint(10000, 99999)
        self._surname = surname
        self._first_name = first_name
        self._middle_name = middle_name
        self._address = address
        self._phone = phone
        self._medical_card_number = random.randint(100000, 999999)
        self._diagnosis = diagnosis

    @property
    def id(self):
        return self._id

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def medical_card_number(self):
        return self._medical_card_number

    @property
    def diagnosis(self):
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._diagnosis = value

    def __str__(self):
        return f"ID: {self.id}, Ім'я: {self.surname} {self.first_name} {self.middle_name}, Адреса: {self.address}, Телефон: {self.phone}, Номер медичної картки: {self.medical_card_number}, Діагноз: {self.diagnosis}"

class PatientDatabase:
    def __init__(self):
        self._patients = []

    def add_patient(self, patient):
        self._patients.append(patient)

    def get_patients_by_diagnosis(self, diagnosis):
        return [patient for patient in self._patients if patient.diagnosis == diagnosis]

    def get_patients_by_medical_card_number_range(self, start, end):
        return [patient for patient in self._patients if start <= patient.medical_card_number <= end]

    def display_patients(self, patients_list):
        for patient in patients_list:
            print(patient)

def display_menu():
    print("Меню:")
    print("1. Пацієнти з діагнозом 'Грип'")
    print("2. Пацієнти з діагнозом 'Лихоманка'")
    print("3. Пацієнти з діагнозом 'Струс мозгу'")
    print("4. Пацієнти з діагнозом 'Короновірус'")
    print("5. Пацієнти з діагнозом 'Перелом ноги'")
    print("6. Пацієнти, номер медичної картки яких перебуває в інтервалі 10000-200000:")
    print("7. Вийти")

db = PatientDatabase()
db.add_patient(Patient("Ахремчюк", "Іван", "Іванович", "Пушкінська 10, Харків", "+380996356245", "Грип"))
db.add_patient(Patient("Забівко", "Олександер", "Андрійович", "Пр. Інженерний 10, Харків", "+380996358525", "Грип"))
db.add_patient(Patient("Надійко", "Ванеса", "Юрівна", "Пр. Інженерний 4, Харків", "380962366455", "Лихоманка"))
db.add_patient(Patient("Іванова", "Юлія", "Сергіївна", "вул. Гоголя, 20", "380962556457", "Струс мозгу"))
db.add_patient(Patient("Тупіченко", "Іван", "Олександрович", "Пушкінська 45, Харків", "+380996356245", "Короновірус"))
db.add_patient(Patient("Васюта", "Аліса", "Дмитрівна", "Пр. Очара 17, Харків", "+380962536456", "Перелом ноги"))

while True:
    display_menu()
    choice = input("Виберіть опцію: ")

    if choice == "1":
        print("Пацієнти з діагнозом 'Грип':")
        db.display_patients(db.get_patients_by_diagnosis("Грип"))
    elif choice == "2":
        print("Пацієнти з діагнозом 'Лихоманка':")
        db.display_patients(db.get_patients_by_diagnosis("Лихоманка"))
    elif choice == "3":
        print("Пацієнти з діагнозом 'Струс мозгу':")
        db.display_patients(db.get_patients_by_diagnosis("Струс мозгу"))
    elif choice == "4":
        print("Пацієнти з діагнозом 'Короновірус':")
        db.display_patients(db.get_patients_by_diagnosis("Короновірус"))
    elif choice == "5":
        print("Пацієнти з діагнозом 'Перелом ноги':")
        db.display_patients(db.get_patients_by_diagnosis("Перелом ноги"))
    elif choice == "6":
        print("\nПацієнти, номер медичної картки яких перебуває в інтервалі 10000-200000:")
        db.display_patients(db.get_patients_by_medical_card_number_range(10000, 200000))
    elif choice == "7":
        print("Дякую за використання нашої програми!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

# Пацієнти, номер медичної картки яких перебуває в заданому інтервалі
#print("\nПацієнти, номер медичної картки яких перебуває в інтервалі 10000-200000:")
#db.display_patients(db.get_patients_by_medical_card_number_range(10000, 200000))
