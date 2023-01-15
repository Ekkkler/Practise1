from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm

def main():

    funcs = (
        (factorial.factorial, int, 1),
        (exponentiation.exp2, float, 1),
        (exponentiation.exp3, float, 1),
        (root.root2, float, 1),
        (root.root3, float, 1),
        (logarithm.lg, float, 1),
        (logarithm.ln, float, 1),
        (logarithm.log, float, 2)
    )
    for idx, (func, _, _) in enumerate(funcs):
        print(str(idx) + ".", func.__name__)

    try:
        func_idx = int(input("Enter index: "))
    except Exception as e:
        print(e)
        return

    if func_idx < 0 or func_idx >= len(funcs):
        print("Out of bounds")

    try:
        func, args_type, args_count = funcs[func_idx]

        args = list(map(args_type, input(f"Enter {args_count} argument(s) separated by space: ").split(" ")))
        
        if len(args) != args_count:
            raise Exception(f"wrong argument count for function: {func.__name__}, expected {args_count}, got {len(args)}")


        print('result:', func(*args))

    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()