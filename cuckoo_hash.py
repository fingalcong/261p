# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List


class CuckooHash:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.tables = [[None] * init_size for _ in range(2)]

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size - 1)

	def get_table_contents(self) -> List[List[int]]:
		return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	def insert(self, key: int) -> bool:
		if self.lookup(key):
			return True
		count = 0
		t_ID = 0
		while count <= self.CYCLE_THRESHOLD:
			val = self.hash_func(key, t_ID)
			f_key = self.tables[t_ID][val]
			self.tables[t_ID][val] = key
			if f_key is None:
				return True
			else:
				t_ID = 1 - t_ID
				key = f_key
				count += 1
		return False

	def lookup(self, key: int) -> bool:
		val = self.tables[0][self.hash_func(key, 0)]
		vall = self.tables[1][self.hash_func(key, 1)]
		if(val == key or vall == key):
			return True
		else:
			return False

	def delete(self, key: int) -> None:
		if (not self.lookup(key)):
			return
		if self.tables[0][self.hash_func(key, 0)] == key:
			self.tables[0][self.hash_func(key, 0)] = None
		elif self.tables[1][self.hash_func(key, 1)] == key:
			self.tables[1][self.hash_func(key, 1)] = None

	def rehash(self, new_table_size: int) -> None:
		self.__num_rehashes += 1;
		self.table_size = new_table_size  # do not modify this line
		old_T = self.tables
		self.tables = [[None] * new_table_size for _ in range(2)]

		i = 0
		while(i < len(old_T[0])):
			if old_T[0][i] is not None:
				self.insert(old_T[0][i])
			i += 1

		j = 0
		while (j < len(old_T[1])):
			if old_T[1][j] is not None:
				self.insert(old_T[1][j])
			j += 1

# feel free to define new methods in addition to the above
# fill in the definitions of each required member function (above),
# and for any additional member functions you define

