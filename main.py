import random, time
import tabulate

def ssort(a):
    L = list(a)
    for i in range(len(L)):
        #print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L


def qsort(a, pivot_fn):
    ## TO DO
    pass
    
def time_sort(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the sort function
      mylist......the list to sort

    Returns:
      the number of milliseconds it takes to run this
      sort function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 400, 800]): #, 1600, 3200, 6400, 12800, 25600, 51200, 102400]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, sorting_alg1_time, sorting_alg2_time, sorting_alg3_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = #
    qsort_random_pivot = #
    # tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))

        # shuffles list if needed
        #random.shuffle(mylist)

        result.append([
            len(mylist),
            time_sort(ssort, mylist),
            time_sort(qsort_fixed_pivot, mylist),
            time_sort(qsort_random_pivot, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'ssort', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

random.seed()
# print_results(compare_sort()) # ensure this is commented out when you submit