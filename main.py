# python3
# 221RDB060 Artjoms Sidorkins

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    end = [0] * n
    for i in range(m):
        time = data[i]
        min_time = min(end)
        users_thread = end.index(min_time)
        output.append((users_thread, min_time))
        end[users_thread] += time    

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    # n = 0
    # m = 0
    n, m = map(int, input().split())
   
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for end, time in result:
        print(end,time)


if __name__ == "__main__":
    main()
