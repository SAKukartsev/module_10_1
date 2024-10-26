from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):
            sleep(0.1)
            file.write(f'Какое-то слово № {i + 1}' + '\n')
        print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_and = datetime.now()
res_time = time_and - time_start
print(res_time)

time_start = datetime.now()

Thr_write_1 = Thread(target=write_words, args=(10, 'example5.txt'))
Thr_write_2 = Thread(target=write_words, args=(30, 'example6.txt'))
Thr_write_3 = Thread(target=write_words, args=(200, 'example7.txt'))
Thr_write_4 = Thread(target=write_words, args=(100, 'example8.txt'))

Thr_write_1.start()
Thr_write_2.start()
Thr_write_3.start()
Thr_write_4.start()

Thr_write_1.join()
Thr_write_2.join()
Thr_write_3.join()
Thr_write_4.join()

time_and = datetime.now()
res_time = time_and - time_start
print(res_time)
