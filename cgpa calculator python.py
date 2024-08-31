from tkinter import *
from tkinter import messagebox

from matplotlib.pyplot import text


class App:
    def __init__(self, parent):
        self.parent = parent

        self.frame_1 = Frame(parent)
        self.frame_1.pack(padx=0)
        self.lbl_1 = Label(self.frame_1, text="Current CGPA :")
        self.label = Label(self.frame_1, text="Subject 1")
        self.lbl_1.grid(row=0, column=0)
        self.entry_1 = Entry(self.frame_1)
        self.entry_1.grid(row=0, column=1)

        self.lbl_2 = Label(self.frame_1, text="Units Completed :")
        self.lbl_2.grid(row=1, column=0)
        self.entry_2 = Entry(self.frame_1)
        self.entry_2.grid(row=1, column=1)

        self.lbl_3 = Label(self.frame_1, text="Number of Courses to add :")
        self.lbl_3.grid(row=2, column=0)
        self.entry_3 = Entry(self.frame_1)
        self.entry_3.grid(row=2, column=1)

        self.btn_1 = Button(self.frame_1, text="Add Courses !",
                            command=self.add_courses)


        self.btn_1.grid (row=3, column=1)



        self.frame_3 = Frame(root)
        self.frame_3.pack(pady=10)
        self.frame_4 = Frame(root)
        self.frame_4.pack(pady=8)

        self.frame_2 = Frame(parent)
        self.frame_2.pack(pady=10)
        self.gpa = []

    def add_courses(self):
        if ((self.entry_3.get() != '') & (self.entry_3.get().isdigit())):
            self.num_courses = int(self.entry_3.get())
            self.grades_list = []
            self.units_list = []
            self.grades_list2 = []
            self.units_list2 = []


            self.lbl_sub = Label(self.frame_2, text="Subjects  names:", padx=20)
            self.lbl_sub.grid(row=0, column=0)
            self.lbl_units = Label(self.frame_2, text="Units :")
            self.lbl_units.grid(row=0, column=1)
            self.lbl_grades = Label(self.frame_2, text="Grades :")
            self.lbl_grades.grid(row=0, column=2)
            p = self.num_courses + 2
            for i in range(0, self.num_courses):
                self.units_list.append(
                    Spinbox(self.frame_2, values=(1, 2, 3, 4, 5), width=5))
                self.units_list2.append(
                    Spinbox(self.frame_2, values=(1, 2, 3, 4, 5), width=5))
                self.entryi = Entry(self.frame_2)
                self.entryi.grid(row=i+1, column=0, padx=10, pady=10)
                self.entryii = Entry(self.frame_2)
                self.entryii.grid(row= p +i + 1, column=0, padx=10, pady=10)
                self.units_list[i].grid(row=i+1, column=1, padx=10, pady=10)
                self.units_list2[i].grid(row=p+i+1, column=1, padx=10, pady=10)



                self.grades_list.append(Spinbox(self.frame_2, width=5, values=(
                    "A", "A-", "B", "B-", "C", "C-", "D", "E")))
                self.grades_list[i].grid(row=i+1, column=2, padx=10, pady=10)
                self.grades_list2.append(Spinbox(self.frame_2, width=5, values=(
                    "A", "A-", "B", "B-", "C", "C-", "D", "E")))
                self.grades_list2[i].grid(row=p+i + 1, column=2, padx=10, pady=10)
            self.btn_3 =Button(self.frame_2, text="Caclculate tgpa", command=self.calc_CG)
            self.btn_3.grid(row= p , column=5)
            self.btn_4 = Button(self.frame_2, text="Caclculate tgpa", command=self.calc_CG2)
            self.btn_4.grid(row=p + p, column=5)
            self.label = Label(self.frame_2, text="Semester 1", borderwidth=10)
            self.label.grid(row=p, column=0)
            self.label2 = Label(self.frame_2, text= "Semester 2", borderwidth=10)
            self.label2.grid(row=p+p, column=0)
            self.btn_calcCG = Button(
                self.parent, text="Calculate CGPA for the year", command=self.final_cgpa)

            self.btn_calcCG.pack(pady=8)
            self.btn_1.config(state=DISABLED)
        else:
            messagebox.showinfo("Hey ! ", "Enter a Valid Value")



    def calc_CG(self):
        print("Calculating !")
        credits_this_sem = 0
        units_this_sem = 0
        for j in range(0, self.num_courses):
            credits_this_sem = credits_this_sem + \
                int(self.units_list[j].get()) * \
                (self.grade(self.grades_list[j].get()))
            units_this_sem = units_this_sem + int(self.units_list[j].get())
        final_cgpa = (credits_this_sem + float(self.entry_1.get()) *
                      int(self.entry_2.get())) / (units_this_sem+int(self.entry_2.get()))
        self.gpa.append(final_cgpa)
        messagebox.showinfo("Predicted TGPA  for semester 1", str(final_cgpa))
    def calc_CG2(self):
        print("Calculating !")
        credits_this_sem = 0
        units_this_sem = 0
        for j in range(0, self.num_courses):
            credits_this_sem = credits_this_sem + \
                int(self.units_list2[j].get()) * \
                (self.grade(self.grades_list2[j].get()))
            units_this_sem = units_this_sem + int(self.units_list[j].get())
        final_cgpa = (credits_this_sem + float(self.entry_1.get()) *
                      int(self.entry_2.get())) / (units_this_sem+int(self.entry_2.get()))
        self.gpa.append(final_cgpa)
        messagebox.showinfo("Predicted TGPA for semester 2 ", str(final_cgpa))

    def final_cgpa(self):
        i=0
        a = 0
        for g in self.gpa:
            a = a + g

        final_cgpa = float(a/2)
        self.gpa = []
        messagebox.showinfo("Predicted CGPA for the year", str(final_cgpa))
    def grade(self, grd):
        dict_ = {'A': 10, 'A-': 9, 'B': 8, 'B-': 7,
                 'C': 6, 'C-': 5, 'D': 4, 'E': 2}
        return dict_[grd]


root = Tk()
root.title("CGPA Calculator")
root.geometry("600x600")
app = App(root)
root.mainloop()