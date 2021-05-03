
from Core import Core

def main():
    noOfCores = int(input("Enter number of cores: "))
    cacheSize = input("Enter cache size or press enter for default size: ")
    cores = []

    if cacheSize == '':
        for coreID in range(noOfCores):
            cores.append(Core(coreID))

    elif cacheSize.isdigit():
        cSize = int(cacheSize)
        for coreID in range(noOfCores, cSize):
            cores.append(Core(coreID, cSize))


    print(f"\n{noOfCores} cores successfully created.\n")

    cores[0].createProcess()
    cores[0].createProcess()
    cores[2].createProcess()

    for core in cores:
        print(f"Core {core.id}: \n{core.status()}")


if __name__ == "__main__":
    # execute only if run as a script
    main()