import pandas as pd

importfolder = r'C:\Users\Hugh\PycharmProjects\Graphical_TImetabler\Graphical Timetable\''
importfile = r'C:\Users\Hugh\PycharmProjects\Graphical_TImetabler\Graphical Timetable\pupil-lesson-list.xlsx'
importsaveddf = r'C:\Users\Hugh\PycharmProjects\Graphical_TImetabler\Graphical Timetable\export.xlsx'
num_sheets = 6
all_students = pd.DataFrame()
lesson_col_names = ['Lesson', 'Picture', 'Name']
school_lessons = pd.DataFrame(columns=lesson_col_names)


def student_into_df(file_address, file_sheet):  # adds new excel document to all_students dataframe
    global all_students
    timetable = pd.read_excel(file_address, file_sheet, index_col=None, na_values=['NA'])
    timetable.dropna(inplace=True)  # drop empty rows
    new = timetable["Group"].str.split(":", n=3,
                                       expand=True)  # split Group field into three new fields Lesson, Teacher, Room
    timetable["Lesson"] = new[0]
    timetable["Teacher"] = new[1]
    timetable["Room"] = new[2]

    new = timetable["Lesson"].str.replace('\d+', '')  # remove numbers from Lesson field
    timetable["Lesson"] = new

    new = timetable["Lesson"].str.replace(r'\b\w\b', '').str.replace(r'\s+', ' ')  # remove single letters
    timetable["Lesson"] = new
    timetable["Lesson"] = timetable["Lesson"].str.strip()  # remove any spaces
    timetable["Teacher"] = timetable["Teacher"].str.strip()  # remove any spaces
    all_students = all_students.append(timetable)


def load_workbook(file_address, numofsheets):
    for x in range(1, numofsheets):
        load_student(file_address, "Sheet" + str(x))


def save_asd_to_excel(filename):  # save all_students dataframe(asd) to excel
    all_students.to_excel(importfolder[:-1] + filename + ".xlsx")  # remove literal quote at end of folder name


def load_from_saved_frame_excel():  # temporarily set to fixed file
    global importsaveddf  # temporarily set to fixed file
    global all_students
    file_address = importsaveddf  # temporarily set to fixed file
    timetable = pd.read_excel(file_address, 'Sheet1', index_col=None, na_values=['NA'])
    all_students = all_students.append(timetable)


def lessons_into_df():
    global school_lessons
    global all_students
    school_lessons["Lesson"] = all_students["Lesson"]
    school_lessons = school_lessons.drop_duplicates(keep="first")


load_from_saved_frame_excel()
