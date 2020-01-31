import multiprocessing

def calc_quad(number):
    print('quad: ', number * number * number *number)

def count():
    i = 0
    while i < 250:
        i += 1
        print(i)

if __name__ == "__main__":
    number1 = 7777777777777777777777777777777
    number2 = 8888888888888888888888888888888

    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=calc_quad, args=(number2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()