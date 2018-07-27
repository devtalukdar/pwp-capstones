class User(object):
	def __init__(self, name, email):
		if isinstance(name, str):
			self.name = name
		if isinstance(email, str):
			self.email = email
		# book object to user's rating
		self.books = {}

	def get_email(self):
		return self.email

	def change_email(self, address):
		if isinstance(address, str):
			self.email = address
			print("Your email has been changed! to {new}!".format(new=self.email))

	def __repr__(self):
		return "User {name}, email: {email}, books read: {amt}".format(name=self.name, email=self.email, amt=len(self.books))

	def __eq__(self, other):
		if (self.name == other.name) and (self.email == other.email):
			return True
		else:
			return False

	#Book object for book
	def read_book(self, book, rating=None):
		self.books.update({str(book): rating})
		# return self.books

	def get_average_rating(self):
		c_rating = 0
		for value in self.books.values():
			if value != None:
				c_rating += value
			else:
				continue
		avg =  (c_rating / len(self.books))
		return avg


class Books:
	def __init__(self, title, isbn):
		if isinstance(title, str) and isinstance(isbn, int):
			self.title = title
		if isinstance(isbn, int):
			self.isbn = isbn
		self.ratings = []

	def get_title(self):
		return self.title

	def get_isbn(self):
		return self.isbn

	def set_isbn(self, new_isbn):
		if isinstance(new_isbn, int):
			self.isbn = new_isbn
			print("The books ISBN has been updated to {new}!".format(
			new=self.isbn))
		# This is not neccessary:
		#return self.isbn

	def add_rating(self, rating):
		if 0 <= rating <= 4:
			self.ratings.append(rating)
		else:
			print("Invalid Rating")

	def __eq__(self, other):
		if (self.title == other.title) and (self.isbn == other.isbn):
			return True
		else:
			return False

	def get_average_rating(self):
		total = 0
		for rating in self.ratings:
			total += rating
		return total / len(self.ratings)

	def __hash__(self):
		return hash((self.title, self.isbn))

	def __repr__(self):
		return "Title: {}, ISBN: {}".format(self.title, self.isbn)


class Fiction(Books):
	def __init__(self, title, author, isbn):
		super().__init__(title, isbn)
		if isinstance(author, str):
			self.author = author

	def get_author(self):
		return self.author

	def __repr__(self):
		return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Books):
	def __init__(self, title, subject, level, isbn):
		super().__init__(title, isbn)
		if isinstance(subject, str):
			self.subject = subject
		if isinstance(level, str):
			self.level = level

	def get_subject(self):
		return self.subject

	def get_level(self):
		return self.level

	def __repr__(self):
		return "{title}, a {lvl} manual on {subj}.".format(title=self.title, lvl=self.level, subj=self.subject)


class TomeRater:
	def __init__(self):
		# empty dictionary that maps users email to corresponding User Object
		self.users = {}
		# maps book objects to number of users whove read it
		self.books = {}

	def create_book(self, title, isbn):
		new_book = Books(title, isbn)
		self.books[new_book] = 0
		return new_book

	def create_novel(self, title, author, isbn):
		new_fbook = Fiction(title, author, isbn)
		self.books[new_fbook] = 0
		return new_fbook

	def create_non_fiction(self, title, subject, level, isbn):
		new_nfbook = Non_Fiction(title, subject, level, isbn)
		self.books[new_nfbook] = 0
		return new_nfbook

	def add_book_to_user(self, book, email, rating=None):
		if email in self.users:
			self.users[email].read_book(book, rating)
		else:
			print("No user with email {}".format(email))
		if rating != None:
			book.add_rating(rating)
			if book not in self.books:
				self.books.update({book: 1})
			else:
				self.books[book] += 1

	def add_user(self, name, email, user_books=None):
		self.users[email] = User(name, email)
		if user_books != None:
			for book in user_books:
			# To use method within class need to use "self." or in general you need to assign with it a class to work off of
				self.add_book_to_user(book, email)

	def print_catalog(self):
		for book in self.books:
			print(book)

	def print_users(self):
		for user in self.users:
			print(user)

	def get_most_read_book(self):
		for book in self.books.keys():
			if self.books[book] == max(self.books.values()):
				print(book)

	def highest_rated_book(self):
		ratings = []
		for key in self.books.keys():
			ratings.append(key.get_average_rating())
		for key in self.books.keys():
			if key.get_average_rating() == max(ratings):
				return key
			else:
				continue

	def most_positive_user(self):
		ratings = []
		for value in self.users.values():
			ratings.append(value.get_average_rating())
		for value in self.users.values():
			if value.get_average_rating() == max(ratings):
				return value
			else:
				continue

	def __repr__(self):
		return "Number of users: {}, Number of Books: {}".format(len(self.users.values()),len(self.books.keys()))

	# def __eq__(self):
 #  		if (self.users == other.users) and (self.book == other.book):
	# 		return True
 # 		else:
	# 		return False
	
	def get_n_most_read_books(self, n):
		counter = 0
		while counter <= n:
			x = self.books
			for book in x:
				if x[book] == max(x.values()):
					most = book
					print(most)
					counter += 1
					x.pop(book)
					break
				else:
					continue

	def get_n_most_prolific_reader(self, n):
		users = list(self.users.values())
		output_list = []
		for i in range(n):
			highest_books_read = 0
			user_who_read_it = None
			for user in users:
				number_of_books_read = len(user.books.keys())
				if number_of_books_read > highest_books_read:
					highest_books_read = number_of_books_read
					user_who_read_it = user
			output_list.append(user_who_read_it)
			users.pop(users.index(user_who_read_it))
		return output_list




Tome_Rater = TomeRater()


print("---TEST---")
print(Tome_Rater.get_n_most_read_books(2))

print(Tome_Rater.get_n_most_prolific_reader(2))