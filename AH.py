#Author:Ang Xie

class Doctor:
    
    def __init__(self):
        pass
        
    def formatDrInfo(self,doctor_list):
        format_doctor=''
        for doctor in doctor_list:
            doctor=doctor[0]+'_'+doctor[1]+'_'+doctor[2]+'_'+doctor[3]+'_'+doctor[4]+'_'+doctor[5]+'\n'
            format_doctor+=doctor
        return format_doctor
        
    def readDoctorsFile(self):
        doctor_list=[]
        with open ('Project Data/files/doctors.txt','r') as rf:
            for row in rf:
                row = row.rstrip('\n')
                row=row.split('_')
                doctor_list.append(row)
        return doctor_list
    
    def addDrToFile(self,doctor_list):
        self.id=input('Enter the doctor’s ID:\n')
        self.name=input('Enter the doctor’s name:\n')
        self.speciality=input('Enter the doctor’s specility:\n')
        self.timing=input('Enter the doctor’s timing (e.g., 7am-10pm):\n')
        self.qualification=input('Enter the doctor’s qualification:\n')
        self.room_number=input('Enter the doctor’s room number:\n')
        new_doctor=[self.id,self.name,self.speciality,self.timing,self.qualification,self.room_number]
        doctor_list.append(new_doctor)
        return doctor_list
    
    def writeListOfDoctorsToFile(self,format_doctor):
        with open('Project Data/files/doctors.txt','w') as wf:
            wf.write(format_doctor)
        pass
    
    
    def searchDoctorById(self,doctor_list):
        id= input('\nEnter the doctor’s ID:\n')
        for doctor in doctor_list:
            if id == doctor[0]:
                print('\nId'.ljust(15),'Name'.ljust(15),'Speciality'.ljust(15),'Timing'.ljust(15),'Qualification'.ljust(15),'Room Number\n'.ljust(15))
                print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
                return doctor
        print("\nCan't find the doctor with the same ID on the system")
        return False
    
    def searchDoctorByName(self,doctor_list):
        name=input('\nEnter the doctor’s name:\n\n')
        for doctor in doctor_list:
            if name == doctor[1]:
                print('\nId'.ljust(15),'Name'.ljust(15),'Speciality'.ljust(15),'Timing'.ljust(15),'Qualification'.ljust(15),'Room Number\n'.ljust(15))
                print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
                return doctor
        print("\nCan't find the doctor with the same name on the system\n")
        return False
        
    def editDoctorInfo(self,doctor_list):
        id= input('\nPlease enter the id of the doctor that you want to edit their information:\n\n')
        for doctor in doctor_list:
            if id == doctor[0]:
                doctor[1]=input('Enter new Name: \n')
                doctor[2]=input('Enter new Specilist in:\n')
                doctor[3]=input('Enter new Timing: (e.g., 7am-10pm):\n')
                doctor[4]=input('Enter new Qualification: \n')
                doctor[5]=input('Enter new Room number: \n')
                index=doctor_list.index(doctor)
                doctor_list[index]=doctor
                return doctor_list
        print("Can't find the doctor with the same ID on the system")
        pass
    
    def displayDoctorsList(self,doctor_list):
        for doctor in doctor_list:
            print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
        pass
        

def doctors():
    for i in range(1000000):
        dt=Doctor()
        doctor_list=dt.readDoctorsFile()
        nav2=input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')
        if nav2=='1':
            dt.displayDoctorsList(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='2':
            dt.searchDoctorById(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='3':
            dt.searchDoctorByName(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='4':
            new_doctorList=dt.addDrToFile(doctor_list)
            format_doctor=dt.formatDrInfo(new_doctorList)
            dt.writeListOfDoctorsToFile(format_doctor)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='5':
            new_doctorList=dt.editDoctorInfo(doctor_list)
            format_doctor=dt.formatDrInfo(new_doctorList)
            dt.writeListOfDoctorsToFile(format_doctor)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='6':
            print('\nBack to the prevoius Menu\n')
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the prevoius Menu\n')

                
if __name__ == '__main__':
    for i in range(1000000):
        print('\nWelcome to Alberta Hospital (AH) Managment system\n')
        nav1=input("Select from the following options, or select 0 to stop: \n1 - 	Doctors \n2 - 	Facilities \n3 - 	Laboratories \n4 - 	Patients\n")
        if nav1=='1':
            doctors()
        if nav1=='0':
            break
        
        

    