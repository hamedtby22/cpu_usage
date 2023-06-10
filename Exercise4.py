import psutil
from multiprocessing import Pool, cpu_count



def cpu_usage():
    #cpu درصد استفاده از هر هسته 
    print("Usage percentage of each CPU core:")
    for count, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        print(f"Core {count}: {percentage}%")
    print(f"Total percentage of CPU usage: {psutil.cpu_percent()}%")


def increase_usage(value):
    #cpu تابعی برای افزایش استفاده از 
    if value <= 1:
        return value
    else:
        return increase_usage(value-1) + increase_usage(value-2)


if __name__ == "__main__":
    try:
        while True:
            cpu_usage()

            # یک عدد برای افزایش کارایی پردازنده 
            input_number = input("Enter a number (Enter Exit to going out): ")
            if input_number.lower() == 'exit':
                break

            number = int(input_number)
            print(f"Calculating Fibonacci numbers up to...{number}")

            with Pool(cpu_count()) as count:
                count.map(increase_usage, [number for _ in range(cpu_count())])

            print("Done.")

    except Exception as error:
        print(error)