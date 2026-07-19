import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id', 'age']) 
#pd - название библиотеки (выше) ,DataFrame - создание красивой таблицы ,columns - создание колонок (студент айди и эйдж)
