import matplotlib.pyplot as plt
import numpy as np

marks = np.array([75, 80, 90])
subjects = np.array(["Math", "English", "Science"])
mylabels = ["Math", "English", "Science"]

plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.title("Student Marks Data")
plt.grid()
plt.plot(marks, subjects)
plt.show()


x = np.array([60, 90])
y = np.array([70, 85])


plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.title("Student Marks Data")
plt.grid()
plt.scatter(x, y)
plt.show()

plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.title("Student Marks Data")
plt.grid()
plt.bar(marks, subjects)
plt.show()

plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.title("Student Marks Data")
plt.grid()
plt.hist(marks)
plt.show()

plt.pie(marks, labels=mylabels)
plt.legend(title="3 Subjects:")
plt.show()

student1 = np.array([34, 67, 34])
plt.subplot(1, 2, 1)
plt.plot(student1)

student2 = np.array([67, 34, 90])
plt.subplot(1, 2, 2)
plt.plot(student2)

plt.show()
