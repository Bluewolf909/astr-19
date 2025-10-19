import numpy as np

def sinX(x):    # returns sin(x)
    return np.sin(x)

def table(x):   # tables the data
    for i in range(len(x)):
        print(f"x: {x[i]:.20f}; sin(x): {sinX(x[i]):.20f}")

def main():
    
    s = 0           # start value
    e = 2 * np.pi   # end value
    a = 1000        # amonut of value

    x = np.linspace(s, e, a)

    table(x)

if __name__ == "__main__":
    main()