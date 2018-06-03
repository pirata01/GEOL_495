import numpy as np

class MyClass:
    fileName = ""
    Name = ""
    Type = ""
    Class = ""
    Subclass = ""
    Particle_Size = ""
    Sample_No = ""
    Owner = ""
    Wavelength_Range = ""
    Origin = ""
    Collection_Date = ""
    Description = ""
    Measurement = ""
    First_Column = ""
    Second_Column = ""
    X_Units = ""
    Y_Units = ""
    First_X_Value = 0
    Last_X_Value = 0
    Number_of_X_Values = 0
    Additional_Information = ""
    arrayData = 0.0;
    
    def __init__(self, a):
        count = 0;
        self.fileName = a
        with open(self.fileName) as fp:
            for i, line in enumerate(fp):
                if i == 0:
                    self.Name = line.split("Name: ",1)[1].strip()
                elif i == 1:
                    self.Type = line.split("Type: ",1)[1].strip()
                elif i == 2:
                    self.Class = line.split("Class: ",1)[1].strip()
                elif i == 3:
                    self.Subclass = line.split("Subclass: ",1)[1].strip()
                elif i == 4:
                    self.Particle_Size = line.split("Particle Size: ",1)[1].strip()
                elif i == 5:
                    self.Sample_No = line.split("Sample No.: ",1)[1].strip()
                elif i == 6:
                    self.Owner = line.split("Owner: ",1)[1].strip()
                elif i == 7:
                    self.Wavelength_Range = line.split("Wavelength Range: ",1)[1].strip()
                elif i == 8:
                    self.Origin = line.split("Origin: ",1)[1].strip()
                elif i == 9:
                    self.Collection_Date = line.split("Collection Date: ",1)[1].strip()
                elif i == 10:
                    self.Description = line.split("Description: ",1)[1].strip()
                elif i == 11:
                    self.Measurement = line.split("Measurement: ",1)[1].strip()
                elif i == 12:
                    self.First_Column = line.split("First Column: ",1)[1].strip()
                elif i == 13:
                    self.Second_Column = line.split("Second Column: ",1)[1].strip()
                elif i == 14:
                    self.X_Units = line.split("X Units: ",1)[1].strip()
                elif i == 15:
                    self.Y_Units = line.split("Y Units:",1)[1].strip()
                elif i == 16:
                    self.First_X_Value = line.split("First X Value: ",1)[1].strip()
                elif i == 17:
                    self.Last_X_Value = line.split("Last X Value: ",1)[1].strip()
                elif i == 18:
                    self.Number_of_X_Values = line.split("Number of X Values: ",1)[1].strip()
                    self.arrayData = np.zeros([int(self.Number_of_X_Values),2], dtype = np.float32)
                elif i == 19:
                    self.Additional_Information = line.split("Additional Information: ",1)[1].strip()
                elif i >= 21:
                    self.arrayData[count][0] = float(line.split()[0])
                    self.arrayData[count][1] = float(line.split()[1])
                    count += 1
        fp.close()