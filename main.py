from CPU import CPU
from Core import Core

def main():
    noOfCores = int(input("Enter number of cores: "))
    cacheSize = input("Enter L1 cache size for cores or press enter for default size: ")
    cpu = CPU(noOfCores, cacheSize)


    print(f"\n{noOfCores} cores successfully created.\n")

    cpu.createProcess()
    cpu.createProcess()
    cpu.createProcess()

    for core in cores:
        print(f"Core {core.id}: \n{core.status()}")
    
    print(f"Core {core.id}: \n{core.displayProcesses()}")


if __name__ == "__main__":
    # execute only if run as a script
    main()