import datetime
import application.salary
import application.db.people

if __name__ == '__main__':
    application.salary.calculate_salary()
    application.db.people.get_employees()
    dt = datetime.datetime.today()
    print(dt)
