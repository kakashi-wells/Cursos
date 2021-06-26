def salaryWeek(hrs, salaryHr, job):
    salary = hrs * salaryHr
    salary = salary * 7
    print("El sueldo de un ", job, "es ", salary)
salaryWeek(8, 284, "Doctor")
salaryWeek(4, 10, "Jardinero")