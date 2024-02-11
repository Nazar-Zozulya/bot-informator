# import sqlite3

# class DB():
#     def __init__(self,db_file):
#         self.con = sqlite3.connect(db_file)
#         self.cursor = self.con.cursor()

#         def add_user(self, user_id):
#             with self.con:
#                 self.cursor.execute("INSERT INTO admin (user_id) VALUES(?)",(user_id,))

#         def exists(self, user_id):
#             with self.con:
#                 result = self.cursor.execute("SELECT * FROM admin WHERE user_id = ?",(user_id,)).fetchall()
#                 return bool(len(result))
        
#         def set_email(self, user_id, email):
#             with self.con:
#                 return self.cursor.execute("UPDATE admin SET email = ? WHERE user_id = ?",(user_id, email,))
            
#         # def set_email(self, user_id, nickname):
#         #     with self.con:
#         #         return self.cursor.execute("UPDATE admin SET nickname = ? WHERE user_id = ?",(user_id, nickname,))
            
#         # def set_email(self, user_id, email):
#         #     with self.con:
#         #         return self.cursor.execute("UPDATE admin SET password = ? WHERE user_id = ?",(user_id, email,))
            
#         # def set_email(self, user_id, email):
#         #     with self.con:
#         #         return self.cursor.execute("UPDATE admin SET phone = ? WHERE user_id = ?",(user_id, email,))
            
#         def get_signup(self, user_id):
#             with self.con:
#                 result = self.con.execute("SELECT signup FROM admin WHERE user_id = ?",(user_id,)).fetchall()
#                 for row in result:
#                     signup = str(row[0])
#                 return signup
            
#         def set_signup(self, user_id, signup):
#             with self.con:
#                 return self.cursor.execute("UPDATE admin SET email = ? WHERE user_id = ?",(user_id, signup,))