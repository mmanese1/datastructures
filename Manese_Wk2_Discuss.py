#create class that is common to every patient
class PatientPopulation:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex   
 
#some patient will have diagnosis
#use inheritance PatientPopulation class
class PtDx:
    def __init__(self, name, age, sex, diagnosis):
        PatientPopulation.__init__(self, name, age, sex)
        self.diagnosis = diagnosis
        print(name, age, sex, diagnosis,"\n")
        
#some patients will have insurance
#use inheritance PatientPopulation class
class PtInsure:
    def __init__(self, name, age, sex, insurance):
        PatientPopulation.__init__(self, name, age, sex)
        self.insurance = insurance
        print(name, age, sex, insurance,"\n")
        
#some patients will have labtest 
#use inheritance PtDx class becaus labtest is conducted after dx or suspected dx 
class PtTest:
    def __init__(self, name, age, sex, diagnosis, labtest):
        PtDx.__init__(self, name, age, sex, diagnosis)
        self.labtest = labtest
        print(name, age, sex, diagnosis, labtest)
        
# Create a patient database
PtDx("Mary Smith", "33", "Female","diabetes")
PtInsure("John Steel", "45", "Male","HealthPartners")
PtTest("Jane Doe", "30", "Female","hypertension","liver panel")
 
