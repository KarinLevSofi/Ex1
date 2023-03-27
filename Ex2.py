# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:36:03 2023

@author: קארין
"""



def revword(word: str) -> str: #בניית פונק שמטרתה להפוך סדר האותיות של המיל מההתחלה לסוף ולאותיות קטנות
    return word.lower()[::-1]

def countword() -> int: #פונק שמטרתה לספור בתוך טקסט כמה פעמים מופיעה המילה הראשונה 
    word = '' #מציאת המילה המבוקשת
    count = 1
    with open('text.txt', 'r') as myfile: #קריאת הטקסט
        for line_number, line in enumerate(myfile): #יצירת מילון על מנת שנוכל לזהות מילה מבוקשת
            if line_number == 0: #תנאי למילה המבוקשת הראשונה
                word = line.strip() #חילוץ המילה
                
            else:
                words = line.split() 
                for w in words: # יצירת לולאה למעבר על הטקסט מילה מילה 
                    if w.lower() == revword(word): # תנאי לספירת מילים קיימות כמו המבוקשת
                        count = count + 1
                    print(revword(w)) # כתיבת הטקסט ושימוש בפונק ההופכת ומקטינה כתב
                    
    return count

print(countword())
