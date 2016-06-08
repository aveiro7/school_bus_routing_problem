from random import randint
import sys

def generate_data(N, max_load, max_distance, filename):
	distances = [["1" if x != y else "0" for y in range(N + 1)] for x in range(N + 1)]

	students = [str(randint(1, max_load)) for x in range(N)]
	students = ["0"] + students

	f = open(filename, 'w+')
	f.write(str(max_load) + "\n")
	f.write(str(max_distance) + "\n")
	f.write(str(N) + "\n")
	for line in distances:
		data = " ".join(line) + "\n"
		f.write(data)

	data = " ".join(students) + "\n"
	f.write(data)
	f.close()


if __name__ == "__main__":
	print "wpisz maksymalne obciazenie autobusu: ",
	line = sys.stdin.readline()[:-1]
	max_load = int(line)
	print "wpisz maksymalny dystans: ",
	line = sys.stdin.readline()[:-1]
	max_distance = int(line)
	print "wpisz liste przystankow: ",
	line = sys.stdin.readline()[:-1]
	N = int(line)
	print "wpisz nazwe pliku wyjsciowego:"
	filename = sys.stdin.readline()[:-1]

	generate_data(N, max_load, max_distance, filename)







	