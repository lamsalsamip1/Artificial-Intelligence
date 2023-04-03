
    plt.legend(loc="lower left")

    plt.show()


# running the program
def main():
    heuristic = getHeuristics()
    graph = createGraph()
    print(graph)
    city, citiesCode = getCity()

    for i, j in citiesCode.items():
        print(i, j)

    while True:
        inputCode = int(input("Please enter your desired city's number (0 for exit): "))
