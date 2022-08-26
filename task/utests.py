#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Для индивидуального задания лабораторной работы 2.21 добавьте тесты с
использованием модуля unittest, проверяющие операции по работе с базой данных.
"""

import unittest
import os
import sqlite3
import ind_1 as funcs


class DbTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        funcs.create_table("test.db")
        self.conn = sqlite3.connect("test.db")
        self.cur = self.conn.cursor()
        print("!!!!!!!!!!!!!!!!!!!!!!!СЕТ АП ВЫПОЛНЕН!!!!!!!!!!!!!!!!!!!!!!!")

    def test_create_table(self):
        self.cur.execute("SELECT name from sqlite_master where type='table'")
        rows = self.cur.fetchall()
        self.rows = rows

        self.assertEqual(rows, [('students_info',),
                                ('sqlite_sequence',),
                                ('students',)])

    def test_add_student(self):
        funcs.add_student("anton", "ivt-19", 1, 4.8, 2002, "test.db")
        funcs.add_student("ivan", "ivt-20", 2, 4.9, 2001, "test.db")
        self.cur.execute("""SELECT * FROM students WHERE id LIKE(1)""")
        rows = self.cur.fetchall()
        self.test_stud = [
            {
                "name": row[1],
                "group_name": row[2],
                "estimation": row[3]
            }
            for row in rows
        ]
        self.assertEqual(
            self.test_stud,
            [{'name': 'anton', 'group_name': 'ivt-19', 'estimation': 4.8}]
        )

    def test_select_students(self):
        result = funcs.select_students("test.db", "ivt-20")
        self.assertEqual(
            result,
            [{'name': 'ivan', 'group_name': 2, 'estimation': 2001}]
        )

    @classmethod
    def tearDownClass(self):
        self.conn.close()
        os.remove("test.db")
        print("!!!!!!!!!!!!!!!!!!!!!!ТИРДАУН ВЫПОЛНЕН!!!!!!!!!!!!!!!!!!!!!!!")


if __name__ == '__main__':
    unittest.main()
