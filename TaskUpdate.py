"""
*******************************************
*** File Name :TaskUpdate.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.06.14
*** Purpose   :課題情報を更新する．
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.06.14
"""

import datetime
import time
import re
import sqlite3
from Priority import Priority

def TaskUpdate(user_id) : #使用者のID

    """
    ***********************************
    *** Function Name :TaskUpdate()
    *** Designer      :城谷拓身
    *** Date          :2021.6.25
    *** Function      :課題情報を更新する．
    ***********************************
    """

    #更新条件:日付変更時等

    #Task.dbにアクセスする.
    dbname = 'Task.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('SELECT * FROM task WHERE user_id = user_id')
    for row in cur:
        user_id = str(row[0])
        task_name = str(row[1])
        deadline = str(row[2])
        importance = int(row[3])
        notice_time = str(row[4])
        
        priority = Priority(deadline, importance)
        #期日小 重要度低
        #期日大 重要度高

        cur.execute('REPLACE INTO task (user_id, task_name, deadline, importance, notice_time, priority) values(?,?,?,?,?,?)',(user_id,task_name,deadline,importance,notice_time,priority))

   
    #user_idは昇順、priorityは降順でソート
    cur.execute('SELECT * FROM task order by user_id asc, priority desc')
    #全コード表示
    cur.execute('SELECT task_name, deadline, priority FROM task')
    print(cur.fetchall())
    conn.commit()
    conn.close()