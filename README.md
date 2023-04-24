# LambdaPCA

## Quickstart

- Create or open an Excel spreadsheet
- Create a named range called `PCA_INTERNAL` and copy-paste the contents of the file `PCA_INTERNAL.min.lambda` into the `Refers to:` field
- Create a named ranged called `PCA` and copy-paste the contents of the file `PCA.min.lambda` into the `Refers to:` field
- Setup your centered data. That is, the mean of each column must be zero
- Call the function as `=PCA(A1:D30,,)`. Note the two extra commas required because `PCA` can take additional optional arguments. This returns the "weights" or "coeff" matrix
- Create the "factors" or "scores" matrix by multiplying the centered data on the right by the transpose of the weights matrix

See also demo.xlsx, which runs PCA on the classic Iris dataset.

## Notes

- PCA's second, optional, parameter is `tolerance` which controls how close to zero the off-diagonal elements of eigendecomposition needs to be. Defaults to 1e-7.
- PCA's third, optional, parameter is `centralityCheck`. PCA works just fine on uncentered data but if you need to recover the scores you have to multiple the weights by the centered data so this check is provided to catch a common error. If the mean of any column is greater than or equal to `centalityCheck` then PCA returns a `#VALUE!` error. Set to a negative number or any non-numeric value to suppress the check. Defaults to 1e-7.
- LambdaPCA works by computing the eigendecomposition of the covariance matrix using Jacobi iterations. See <https://web.stanford.edu/class/cme335/spr11/lecture7.pdf>.
- The choice to return the weights matrix in the form it is in (requiring transpose) is to be consistent with MATLAB/Octave's PCA function

## Troubleshooting

| Issue               | Possible remediation                                                                            |
| ------------------- | ----------------------------------------------------------------------------------------------- |
| Returning `#NAME?`  | Ensure that `PCA_INTERNAL` is correctly named                                                   |
| Returning `#NUM!`   | Increase the `tolerance` parameter. Try 0.01 as a starting point                                |
| Returning `#VALUE!` | Either subtract the mean from each column or suppress error by passing -1 as the final argument |
