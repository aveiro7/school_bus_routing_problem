import sys

def read_data(filename):
	f = open(filename, 'r')
	max_loading = int(f.readline()[:-1])
	print "maksymalne obciazenie:", max_loading
	max_distance = int(f.readline()[:-1])
	print "maksymalny dystans:", max_distance
	N = int(f.readline()[:-1])
	print "liczba przystankow:", N

	
	for i in range(N + 1):
		f.readline()

	line = f.readline().split()
	students_list = [int(x) for x in line]
	print "lista uczniow", students_list
	students = sum(students_list)
	print "liczba uczniow:", students
	f.close()


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "provide filename!"
		exit()

	filename = sys.argv[1]

	read_data(filename)

