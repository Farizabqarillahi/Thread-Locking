import threading

def is_prime(m):
    if m <= 1:
        return False
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            return False
    return True

def count_primes(n, m, results):
    count = 0
    for i in range(n, m+1):
        if is_prime(i):
            count += 1
    results.append(count) # Menambahkan hasil dari setiap thread ke list

def main():
    # Membagi rentang menjadi 4 bagian yang sama
    n = 20000
    m = 9999
    num_threads = 4
    step = (n - m + 1) // num_threads
    threads = []
    results = []
    for i in range(num_threads):
        start = m + i * step
        end = start + step - 1
        if i == num_threads - 1:
            end = n
        thread = threading.Thread(target=count_primes, args=(start, end, results))
        thread.start()
        threads.append(thread)

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()
        # Menambahkan hasil dari setiap thread ke list

    # Menambahkan hasil dari setiap thread
    total_count = sum(results)
    print(f'Jumlah bilangan prima: {total_count}')

if __name__ == '__main__':
    main()
