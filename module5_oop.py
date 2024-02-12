class BasicClass:
    @staticmethod
    def basic_method():
        print("Please input an positive number N:")
        N = int(input())
        print(f"Your input N is: {N}")

        print("Please input N positive numbers:")
        inputs = []
        for _ in range(N):
            n = int(input())
            inputs.append(n)
        print(f"Your inputs are {inputs}.")

        print("Please input an integer X:")
        X = int(input())

        print("THe index of X is:")
        if X not in inputs:
            print("-1")
        else:
            print(inputs.index(X) + 1)