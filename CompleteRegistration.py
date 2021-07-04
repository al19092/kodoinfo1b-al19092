"""
*******************************************
*** File Name :CompleteRegistration.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.07.04
*** Purpose   :課題情報をデータベースに登録する．
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.07.04
"""

from Priority import Priority
import sqlite3

def CompleteRegistration(user_id, #使用者のID
                         task_name, #課題名
                         deadline, #課題の期日
                         importance, #課題の重要度
                         notice_time) : #通知が届く日時
    """
    ***********************************
    *** Function Name :CompleteRegistration()
    *** Designer      :城谷拓身
    *** Date          :2021.07.04
    *** Function      :課題情報をデータベースに登録する.
    ***********************************
    """
    #Task.dbにアクセスする.
    dbname = 'Task.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    priority = Priority(deadline, importance)

    #入力された課題情報をデータベースに登録する.
    cur.execute('INSERT INTO task(user_id, task_name, deadline, importance, notice_time, priority) values(?,?,?,?,?,?)',(user_id,task_name,deadline,importance,notice_time, priority))
    conn.commit()
    conn.close()