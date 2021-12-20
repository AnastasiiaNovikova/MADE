def apply_filter(i, j):
  submatrix = [[0 for _ in range(len(kernel[0]))] for _ in range(len(kernel))]
  x_lim = len(submatrix[0]) // 2
  y_lim = len(submatrix) // 2
  for m in range(-x_lim, x_lim+1):
    for n in range(-y_lim, y_lim+1):
      if -1<i+m<len(arr) and -1<j+n<len(arr[0]):
        submatrix[m+y_lim][n+x_lim] = arr[i+m][j+n]

  subm_filt = [[0 for _ in range(len(submatrix[0]))] for _ in range(len(submatrix))]
  s = 0
  for m in range(len(submatrix[0])):
    for n in range(len(submatrix)):
      subm_filt[m][n] = submatrix[m][n] * kernel[m][n]
      s += subm_filt[m][n]

  for m in range(len(submatrix[0])):
    for n in range(len(submatrix)):
      arr[i][j] += 1./s * subm_filt[m][n]
  return arr

  # for i in range(len(arr)):
  #   for j in range(len(arr[0])):
  #     apply_filter(i, j)
