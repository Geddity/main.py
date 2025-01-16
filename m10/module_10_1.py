import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}"
            f.write(word + '\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

func_start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

func_end_time = time.time()
func_total_time = func_end_time - func_start_time

print(f"Работа потоков: {func_total_time:.2f} секунд")

threads = [threading.Thread(target=write_words, args=(10, 'example5.txt')),
            threading.Thread(target=write_words, args=(30, 'example6.txt')),
            threading.Thread(target=write_words, args=(200, 'example7.txt')),
            threading.Thread(target=write_words, args=(100, 'example8.txt'))]

thread_start_time = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

thread_end_time = time.time()
thread_total_time = thread_end_time - thread_start_time

print(f"Работа потоков: {thread_total_time:.2f} секунд")