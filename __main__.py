#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Password Manager
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

from passwords import passwords
from encrypt import encrypt,decrypt

p = passwords()
rootDir = "/home/michael/Desktop/passwords"
active = 1
isLoggedIn = "FALSE"
userPassword = ""
command = ""

while active == 1:
	
	if isLoggedIn == "FALSE":
		print("\x1b[2J\x1b[0;0H  ____                                     _     \n |  _ \\ __ _ ___ _____      _____  _ __ __| |___ \n | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` / __|\n |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| \\__ \\\n |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|___/\n")
		userPassword = input(" User Password\n > \x1b[30m")
		print("\x1b[0m")
		
		isLoggedIn = p.checkUser(userPassword)
		
	else:
		
		print("\x1b[2J\x1b[0;0H  ____                                     _     \n |  _ \\ __ _ ___ _____      _____  _ __ __| |___ \n | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` / __|\n |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| \\__ \\\n |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|___/\n")
		print(" 1: Add new Account\n 2: View Accounts\n 3: View Account Data\n 4: Delete Account\n 5: Change Master Password\n q: Quit")
		command = input("\n >>> ")

		if command == "1":
			print("\x1b[2J\x1b[0;0H  ____                                     _     \n |  _ \\ __ _ ___ _____      _____  _ __ __| |___ \n | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` / __|\n |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| \\__ \\\n |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|___/\n")
			print(" | Create new account | ")
			
			accountName = input(" Account Name\n > ")
			accountUsername = input(" Username\n > ")
			accountPassword = input(" Password\n > ")
			
			# try:
			p.newAccount(accountName,accountUsername,accountPassword,userPassword)
			# except:
				# print(" There was an error submitting your new account.\n Please contact your system administrator")
			# else:
				# print(" Account created successfully")
			
			command = ""
			
			input("")
		elif command == "2":
			print("\x1b[2J\x1b[0;0H  ____                                     _     \n |  _ \\ __ _ ___ _____      _____  _ __ __| |___ \n | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` / __|\n |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| \\__ \\\n |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|___/\n")
			print(" +---------------+\n | View Accounts | \n +---------------+")
			
			accounts = p.showAccounts()
			
			for row in accounts:
				print(" > "+row)
			
			command = ""
			
			input("")
		elif command == "3":
			print("\x1b[2J\x1b[0;0H  ____                                     _     \n |  _ \\ __ _ ___ _____      _____  _ __ __| |___ \n | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` / __|\n |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| \\__ \\\n |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|___/\n")
			print(" | View Account Information | ")
				
			template = " +----------------------------+\n | {:26s} |\n | {:26s} |\n +----------------------------+"
			
			accountName = input(" Enter Account Name\n >  ")
			accountInfo = p.viewAccount(accountName)
			
			accountPassword = decrypt(accountInfo[2],userPassword).decode('UTF-8')
			
			print(template.format(accountInfo[1],accountPassword))
			
			command = ""
			input("")
		
		elif command == "4":
			print("\x1b[2J\x1b[0;0H  ____                                     _     \n |  _ \\ __ _ ___ _____      _____  _ __ __| |___ \n | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` / __|\n |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| \\__ \\\n |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|___/\n")
			print(" | Delete Account Information | ")
			
			accountName = input(" Search Account\n > ")
			
			p.delAccount(accountName)
			
			command = ""
			
			input("")
		elif command == "5":
			print("\x1b[2J\x1b[0;0H  ____                                     _     \n |  _ \\ __ _ ___ _____      _____  _ __ __| |___ \n | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` / __|\n |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| \\__ \\\n |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|___/\n")
			
			currentPassword = input(" Current Password\n > \x1b[30m")
			print("\x1b[0m")
			newPassword = input(" New Password\n > \x1b[30m")
			print("\x1b[0m")
			
			p.changeUserPassword(currentPassword,newPassword)
			
			command = ""
			input("")
		elif command == "q":
			active = 0
