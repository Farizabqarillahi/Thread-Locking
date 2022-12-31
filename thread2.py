import threading

def factorial(n):
  result = 1
  for i in range(1, n+1):
    result *= i
  print(f"{n}! = {result}\n")

def main():
  n = 15
  m = 20
  # Membuat thread untuk menghitung n!
  thread1 = threading.Thread(target=factorial, args=(n,))

  # Membuat thread untuk menghitung m!
  thread2 = threading.Thread(target=factorial, args=(m,))

  # Menjalankan thread
  thread1.start()
  thread2.start()

  # Menunggu thread selesai
  thread1.join()
  thread2.join()

  print("Selesai")

if __name__ == '__main__':
    main()
