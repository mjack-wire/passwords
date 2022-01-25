#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Passwords File
#  
#  Copyright 2022 Michael Jack <michael@michael-stream>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sqlite3
from encrypt import encrypt,decrypt
import hashlib

rootDir = "/home/michael/Desktop/passwords"

class passwords:
	
	dataFile = None
	cur = None
	
	autoIncrement = None
	accounts = []
	accountData = []
	
	def __init__(self):
		self.dataFile = sqlite3.connect(rootDir+"/data.db")
		self.cur = self.dataFile.cursor()
		
	def __del__(self):
		self.dataFile.close()
		
	def checkUser(self,password):
		hashPass = hashlib.sha256(password.encode()).hexdigest()
		self.cur.execute("SELECT * FROM `users`")
		dbPassword = self.cur.fetchall()
		
		if hashPass == dbPassword[0][1]:
			return "TRUE"
		else:
			return "FALSE"
	
	def changeUserPassword(self,currentPassword,newPassword):
				
		if self.checkUser(currentPassword) == "TRUE":
			hashPass = hashlib.sha256(newPassword.encode()).hexdigest()
			self.cur.execute("UPDATE `users` SET `userPassword` = ?",[hashPass])
			self.dataFile.commit()
			
			self.cur.execute("SELECT * FROM `accounts`")
			rows = self.cur.fetchall()
			
			for row in rows:
				decryptedPassword = decrypt(row[3],currentPassword).decode('UTF-8')
				encryptedPassword = encrypt(decryptedPassword,newPassword)
				
				self.cur.execute("UPDATE `accounts` SET `accountPassword` = ? WHERE `accountId` = ?",(encryptedPassword,row[0]))
				self.dataFile.commit()
		
	def newAccount(self,accountName,accountUsername,accountPassword,userPassword):
		encPassword = encrypt(accountPassword,userPassword)
		self.cur.execute("INSERT INTO `accounts` (`accountName`,`accountUsername`,`accountPassword`) VALUES (?,?,?)",(accountName,accountUsername,encPassword))
		self.dataFile.commit()
		
	def showAccounts(self):
		self.cur.execute("SELECT `accountName` FROM `accounts`")
		rows = self.cur.fetchall()
		outputList = []
		
		for row in rows:
			outputList.append(row[0])
		
		return outputList
		
	def viewAccount(self,accountName):
		self.cur.execute("SELECT * FROM `accounts` WHERE `accountName` = ?",(accountName,))
		rows = self.cur.fetchall()
		
		if len(rows) == 0:
			print("Issue with account information")
		else:
			accountName = rows[0][1]
			accountUsername = rows[0][2]
			accountPassword = rows[0][3]
		
			return [accountName,accountUsername,accountPassword]
	
	def delAccount(self,accountName):
		self.cur.execute("DELETE FROM `accounts` WHERE `accountName` = ?",(accountName,))
		self.dataFile.commit()
