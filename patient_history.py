import datetime


class History:
	symptoms = []
	allergy = []
	symptom_date = []
	problems = {
		"1": "Asthama",
		"2": "Cancer",
		"3": "Thyroid",
		"4": "Diabetes",
		"5": "Heart problems"
	}

	def ask_user_history(self):
		print("Any past disease history ?")
		choice = input(" 1.Yes \n 2.No ")
		if choice == "1":
			self.starting_of_symptoms()
			self.basic_symptoms()
			self.ask_user_for_problems()
			self.ask_for_allergy()
			self.ask_for_surgeries()
		else:
			print("Thankyou for your time")

	def starting_of_symptoms(self):
		print("When did your symptoms start showing ?")
		year = int(input("Enter the year"))
		date = int(input("Enter the date"))
		month = int(input("Enter the month"))
		self.symptom_date = datetime.datetime(year, date, month)

	def basic_symptoms(self):
		print("What were your basic symptoms ? ")
		self.symptoms = input("Enter you symptoms :")

	def ask_user_for_problems(self):
		print("Do you have any disease ?")
		print(self.problems)
		choice = input("Enter the serial no")
		if int(choice) == 1:
			disease = self.problems.get("1")
			print(disease)
		elif int(choice) == 2:
			disease = self.problems.get("2")
			print(disease)
		elif int(choice) == 3:
			disease = self.problems.get("3")
			print(disease)
		elif int(choice) == 4:
			disease = self.problems.get("4")
			print(disease)
		elif int(choice) == 5:
			disease = self.problems.get("5")
			print(disease)
		else:
			print("Enter valid serial number")

	def ask_for_allergy(self):
		print("Do you have any allergy ?")
		allergy = input("Enter : \n 1.Yes \n 2.No ")
		if allergy == "1":
			self.allergy = input("Enter your allergy :")
		else:
			print("You can proceed further")

	def ask_for_surgeries(self):
		print("Did you have any past surgeries ?")
		surgery = input(" 1.Yes \n 2.No ")
		if surgery == "1":
			self.allergy = input("enter which surgery you did : ")
		else:
			print("You can proceed further")


history = History()
history.ask_user_history()
