# while True:
#     if input('##') == 'exit':
#         break
#     if input('##') == 'hi':
#         print("hello wolrd")
#     else:
#         continue

def console():
    if input('##') == 'exit':
        return None
    if input('##') == 'hi':
        print('hello world')
    console()


console()
