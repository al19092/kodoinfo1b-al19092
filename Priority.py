"""
*******************************************
*** File Name :Priority.py
*** Version   :V1.0
*** Designer  :城谷拓身
*** Date      :2021.07.04
*** Purpose   :課題の期日と重要度から優先度を算出する.
***
*******************************************
"""

"""
*** Revision
*** V1.0:城谷拓身,2021.07.04
"""

import datetime
from sys import int_info
import time
import re
import sqlite3

def Priority(deadline, #課題の期日
             importance) : #重要度

    """
    ***********************************
    *** Function Name :Priority()
    *** Designer      :城谷拓身
    *** Date          :2021.07.04
    *** Function      :課題の期日と重要度から優先度を算出する.
    *** Return        :Priority (優先度)
    ***********************************
    """

    #現在時刻を取得
    c_time = str(datetime.datetime.now())
    #現在時刻をそれぞれ月、日、時、分の情報に分ける
    strList = re.compile(r"\d+").findall(c_time)
    #文字列の数字をint型に変換
    intList = [int(s) for s in strList] 
    c_year = intList[0]
    c_month = intList[1]
    c_day = intList[2]
    c_hour = intList[3]
    c_minute = intList[4]
    
    #取得した課題の期日から数字部分のみ取出し
    strList = re.compile(r"\d+").findall(deadline)
    #文字列の数字をint型に変換
    intList = [int(s) for s in strList] 
    #課題の期日をそれぞれ月、日、時、分の情報に分ける
    d_month = intList[0]
    d_day = intList[1]
    d_hour = intList[2]
    d_minute = intList[3]
    #期日が現在時刻より前だったら年をまたぐ
    if (d_month < c_month) or (d_day < c_day) or (d_hour < c_hour) or (d_minute < c_minute) :
        d_year = c_year +1
    else :
        d_year = c_year

    #優先度計算
    #c_time:現在時刻
    c_time = datetime.datetime(year=c_year, month=c_month, day=c_day, hour=c_hour, minute=c_minute)
    #d_time:課題の期日
    d_time = datetime.datetime(year=d_year, month=d_month, day=d_day, hour=d_hour, minute=d_minute)

    #横軸:課題の期日-現在時刻 差が小さいほど緊急
    dd = d_time - c_time
    #時間差を秒に統一
    dd = dd.days*24*60*60+dd.seconds
    #時間差を分に換算
    dd = int(dd/60)
    #dd:現在時刻から期日（分）までの分差
    
    #縦軸:重要度 大きいほど重要 (100から引いて、小さいほど重要にする)
    importance = 100 - int(importance)
    #重要度が100のときは0になってしまう.
    #99のときは1になるので，0.5になるように調整する.
    if (importance == 0) :
        importance = 0.5
    
    #期日に近いほど高く、重要度が高いほど高い
    priority = dd * importance

    #どんなに期日が近くて重要度が100に近くても3桁以上あるためできるだけ値を小さくする.
    priority = priority/100
    
    #優先度を，値が大きいほど高くする.
    priority = 1000 - priority

    return(priority)