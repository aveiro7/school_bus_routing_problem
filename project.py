import random
import sys


def diversification(visited_stops, stops_set, thau, eta, beta):
	result = None
	best_value = -1
	actual = visited_stops[-1]

	for stop in stops_set:
		if stop not in visited_stops:
			value = thau[actual][stop] * (eta[actual][stop] ** beta)

			if value > best_value:
				result = stop
				best_value = value

	assert(result is not None)
	return result


def distraction(visited_stops, stops_set, thau, eta, beta):
	actual = visited_stops[-1]

	possible_results = [x for x in stops_set if x not in visited_stops]

	sum_values = sum([thau[actual][x] * (eta[actual][x] ** beta) for x in possible_results])

	threshold = random.random()
	threshold *= sum_values
	value = 0

	assert(possible_results)

	for stop in possible_results:
		value += thau[actual][stop] * (eta[actual][stop] ** beta)
		if value >= threshold:
			return stop

	return possible_results[-1]


def update_pheromones_locally(thau, rho, thau_0, visited_stops):
	for i in range(len(visited_stops) - 1):
		a = visited_stops[i]
		b = visited_stops[i + 1]
		old_value = thau[a][b]
		thau[a][b] = old_value * (1.0 - rho) + rho * thau_0


def update_pheromones_globally(thau, rho, best_distance, stops_set):
	for start in stops_set:
		for stop in stops_set:
			if start != stop:
				old_value = thau[start][stop]
				thau[start][stop] = old_value * (1.0 - rho) + rho * (1.0 / best_distance)


def routing_phase(stops_set, distances):
	K = 100
	I = 20
	q_0 = 0.9
	beta = 5
	rho = 0.1
	thau_0 = 0.2

	eta = [[1.0 / d for d in x] for x in distances]
	thau = [[thau_0 for d in x] for x in distances]

	best_of_all = None
	for cycle in range(I):
		best_distance = None
		for ant in range(K):
			visited_stops = []
			while len(visited_stops) < len(stops_set)
				q = random.random()

				if q <= q_0:
					next_stop = diversification(visited_stops, stops_set, thau, eta, beta) # equation 6
				else:
					next_stop = distraction(visited_stops, stops_set, thau, eta, beta) # equation 7

				visited_stops.append(next_stop)

			
			update_pheromones_locally(thau, rho, thau_0, visited_stops) # equation 8

			distance = 0
			distance += distances[0][visited_stops[0]] # ze szkoly do pierwszego
			distance += distances[visited_stops[-1]][0] # z ostatniego do szkoly

			for i in range(len(visited_stops) - 1):
				distance += distances[visited_stops[i]][visited_stops[i + 1]]

			if best_distance is None or distance < best_distance:
				best_distance = distance

		update_pheromones_globally(thau, rho, best_distance, stops_set)
		if best_of_all is None or best_distance < best_of_all:
			best_of_all = best_distance

	return best_of_all


def find_best_fitting(actual_bus, max_distance, max_load, distances_of_sets, loading_of_sets):
	# znajduje autobus o największej liczbie dzieci, który dolaczony do aktualnego nie przekroczy limitow

	result = None
	actual_load = loading_of_sets[actual_bus]
	actual_distance = distances_of_sets[actual_bus]

	for index in range(actual_bus + 1, len(distances_of_sets)):
		if actual_distance + distances_of_sets[index] <= max_distance and actual_load + loading_of_sets[index] <= max_load:
			if result is None or loading_of_sets[result] < loading_of_sets[index]:
				result = index

	return result

def find_solution(distances, students, max_load, max_distance):
	# szkola to przystanek o indeksie 0

	assert(students[0] == 0) # przy szkole nie ma uczniów

	N = len(students) # liczba przystankow (razem ze szkola)
	sets = [[i] for i in range(1, N)] # na poczatku kazdy autobus ma odwiedzic jeden przystanek

	distances_of_sets = [2 * distances[0][x] for x in range(1, N)] # jaka odleglosc przejedzie kazdy autobus

	loading_of_sets = [x for x in students[1:]] # ile dzieci zabierze kazdy z autobusow

	actual_bus = 0 # ktory autobus probujemy zaladowac

	while actual_bus < len(sets) - 1: # dopoki mamy jak laczyc trasy autobusow

		bus_to_add = find_best_fitting(actual_bus, max_distance, max_load, distances_of_sets, loading_of_sets)

		if bus_to_add is None:
			actual_bus += 1
		else:
			sets[actual_bus] += sets[bus_to_add]
			del sets[bus_to_add]

			del distances_of_sets[bus_to_add]
			distances_of_sets[actual_bus] = routing_phase(sets[actual_bus], distances)

			loading_of_sets[actual_bus] += loading_of_sets[bus_to_add]
			del loading_of_sets[bus_to_add]

	return actual_bus


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Please provide the filename of the data file"
		print "in format", sys.argv[0], "filename"
		return

	filename = sys.argv[1]

	# read data from the file

	distances, students, max_load, max_distance = read_data(filename)
	print find_solution(distances, students, max_load, max_distance)




