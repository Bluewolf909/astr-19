import numpy as np      ## import numpy for many operations

def main():
    i = 0               ## int
    n = 10              ## int
    x = 19.0            ## double

    ## use numpy to to declare arrays quickly

    y = np.zeros(n,dtype=float)      ## declares 10 zeros as floats using np

    ## we can use loops to iterate with a variable

    for i in range(n):  ## i in range [0,n-1]
        y[i] = 2.0 * float(i) + 1.  ## set y = 2i+1 as float
    
    ## we can also simply iterate through a variable
    for y_element in y:
        print(y_element)

if __name__ == "__main__":
    main()