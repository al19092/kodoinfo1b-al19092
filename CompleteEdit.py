"""
*******************************************
*** File Name :CompleteEdit.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.07.04
*** Purpose   :データベース上の課題情報を編集する．
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.07.04
"""

import datetime
import time
import re
import sqlite3
from Priority import Priority

def CompleteEdit(user_id, #使用者のID
                 task_name, #課題名
                 deadline, #課題の期日
                 importance, #課題の重要度
                 notice_time): #通知が届く日時
    """
    ***********************************
    *** Function Name :CompleteEdit()
    *** Designer      :城谷拓身
    *** Date          :2021.07.04
    *** Function      :データベース上の課題情報の編集を完了する．
    ***********************************
    """
    #Task.dbにアクセスする.
    dbname = 'Task.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    priority = Priority(deadline, importance)

    #入力された課題情報をもとにデータベース上の課題情報を更新する.
    #主キーが使用者のIDと課題名の複合キーなので課題名だけの変更はできない
    #課題編集画面で編集できるのは期日と重要度
    #課題名変更は新規課題扱いになり，編集後に削除してもらう
    cur.execute('REPLACE INTO task (user_id, task_name, deadline, importance, notice_time, priority) values(?,?,?,?,?,?)',(user_id,task_name,deadline,importance,notice_time,priority))
    conn.commit()
    conn.close()


