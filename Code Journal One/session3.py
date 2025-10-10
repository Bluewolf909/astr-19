def f(x):
    try:   
        y = (x**3 + 8)
        return y
    except:
        print("There was an error... returning 0.")
        return 0


def main():
    x = 9

    if(f(x) > 27):
        print("\"YAY!\"")

if __name__=="__main__":
	main()