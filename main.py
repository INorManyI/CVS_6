'''необходимо разработать функцию, принимающую список строк и строку, и
выполняющую вставку строки в середину списка (если длина списка
нечетная, то вставлять строку перед серединным элементом);'''

'''необходимо разработать функцию, принимающую список строк, число и
строку, и выполняющую вставку строки в указанную позицию, если вставка
на указанную позицию невозможна, то вернуть сообщение «operation is not
possible».'''

############[f[f[f]

def string():
    string = list(input())
    case = input()
    log = int(len(string) / 2)
    string.insert(log, case)
    print("".join(string))
string()



def constring():
    string = list(input())
    stickLog = int(input())
    case = input()
    if(stickLog<=len(string) and stickLog >= 0):
        string.insert(stickLog, case)
        print("".join(string))
    else: print("operation is not possible")
constring()
