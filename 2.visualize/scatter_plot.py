import sys
sys.path.append('../tools/')
import tools as tools
import matplotlib.pyplot as plt

def scatter(data, course1, course2):
	plt.figure()
	plt.scatter(data[course1], data[course2], label = 'Students')
	plt.legend()
	plt.title('Correlated Features')
	plt.xlabel(course1)
	plt.ylabel(course2)
	plt.show()

def visualize(data):
	data = data.dropna()
	course1 = 'Defense Against the Dark Arts'
	course2 = 'Astronomy'
	scatter(data, course1, course2)

	# print('Hello hello')
	# col = 0
	# for column in data.columns:
	# 	if col > 5:
	# 		print('Hi hi')######
	# 		course1 = column
	# 		print(course1)##
	# 		col2 = 0
	# 		for column in data.columns:
	# 			if col > 5:
	# 				course2 = column
	# 				print(course1)##
	# 				print(course2)##				
	# 			col2 += 1
	# 		course2 = data[col]
	# 		print(course2)##
	# 		scatter(data, course1, course2)
	# 	col += 1

def main():
	usage = 'Display a scatter plot answering the question:\
			 What are the two features that are similar?'
	data = tools.parse_arg(usage)
	visualize(data)

if __name__ == '__main__':
	main()




