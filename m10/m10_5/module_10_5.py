import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

def main():
    filenames = [f'./file {i}.txt' for i in range(1, 5)]

    lin_start_time = time.time()

    for filename in filenames:
        read_info(filename)

    lin_end_time = time.time() - lin_start_time
    print(f"Линейное выполнение: {lin_end_time:.4f} сек")
    time.sleep(1)

    multi_start_time = time.time()

    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)

    multi_end_time = time.time() - multi_start_time
    print(f"Многопроцессорное выполнение: {multi_end_time:.4f} сек")


if __name__ == '__main__':
    main()