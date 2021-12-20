def apply_median_filter(i, j):
  submatrix = [[0 for _ in range(len(kernel[0]))] for _ in range(len(kernel))]
  x_lim = len(submatrix[0]) // 2
  y_lim = len(submatrix) // 2
  median_arr = []
  for m in range(-x_lim, x_lim+1):
    for n in range(-y_lim, y_lim+1):
      if -1<i+m<len(arr) and -1<j+n<len(arr[0]):
        median_arr.append(arr[i+m][j+n])
  median = int(np.median(median_arr))
  arr[i][j] = median

  #for i in range(len(arr)):
  #  for j in range(len(arr[0])):
  #    apply_median_filter(i, j)
