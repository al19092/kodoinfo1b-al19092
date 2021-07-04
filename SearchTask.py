"""
*******************************************
*** File Name :SearchTask.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.06.24
*** Purpose   :データベース上の課題情報を検索する．
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.06.24
"""

import sqlite3

def SearchTask(user_id, #使用者のID
               task_name) : #課題名
    """
    ***********************************
    *** Function Name :SearchTask()
    *** Designer      :城谷拓身
    *** Date          :2021.6.24
    *** Function      :データベース上の課題情報を検索する．
    *** Return        :task_name 課題名
                       deadline 課題の期日
    ***********************************
    """
    #Task.dbにアクセスする.
    dbname = 'Task.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute('SELECT * FROM task WHERE (user_id = ?) AND (task_name = ?)',(user_id,task_name))
    
    for row in cur:
        user_id = str(row[0])
        task_name = str(row[1])
        deadline = str(row[2])
        importance = int(row[3])
    conn.close()
    return user_id, task_name, deadline, importance
    