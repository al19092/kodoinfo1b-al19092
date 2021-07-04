"""
*******************************************
*** File Name :FinishedTask.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.06.25
*** Purpose   :課題情報を終了済リストに追加する．
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.06.25
"""
import sqlite3

def FinishedTask(user_id, #使用者のID
                 task_name, #課題名
                 deadline, #課題の期日
                 importance) : #課題の重要度
    """
    ***********************************
    *** Function Name :FinishedTask()
    *** Designer      :城谷拓身
    *** Date          :2021.6.25
    *** Function      :課題情報を終了済リストに追加する．
    ***********************************
    """
    #Task.dbにアクセスする.
    dbname = 'Task.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    #入力された課題情報をデータベースに登録する.
    cur.execute('INSERT INTO finished(user_id, task_name, deadline, importance) values(?,?,?,?)',("123456",task_name,deadline,importance))
    conn.commit()
    conn.close()

