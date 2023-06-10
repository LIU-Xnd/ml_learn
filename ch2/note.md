<<< note chapter 2 >>> [BACK](./../readme.md)

# Open data repositories

- Popular open data repositories
    - UC Irvine Machine Learning Repository
    - Kaggle datasets
    - Amazon’s AWS datasets
- Meta portals (they list open data repositories)
    - Data Portals
    - OpenDataMonitor
    - Quandl
- Other pages listing many popular open data repositories
    - Wikipedia’s list of Machine Learning datasets
    - Quora.com
    - The datasets subreddit

# ML project checklist

## Frame the problem and look at the big picture.

A prediction of a district's median housing price will be fed to another ML system (investment analysis), along with many other signals.

Supervised, (univariate multiple) regression, plain batch learning.

Performance measure: RMSE.

Measuring instances number: $m$.

$\bold{x}^{(i)}=\left(\begin{matrix}\text{longitude}\\\text{latitude}\\\text{inhabitants number}\\\text{median income}\end{matrix}\right)$.

$y^{(i)}=\text{median house value}$.

$\bold{X}=\left(\begin{matrix}(\bold{x}^{(1)})^\top\\\vdots\\(\bold{x}^{(2000)})^\top\end{matrix}\right)$.

Need just categories.

<< Signal; Data pipeline; Univariate/Multivariate; >>

## Get the data.

I used `urllib3` instead of `urllib`.

`pd.read_csv()`

`housing.head(); housing.info(); housing['ocean_proximity'].value_counts(); housing.describe()`

<< Percentile; Capped; >>

`housing.hist()`

Finally, many histograms are tail-heavy ... We will try transforming these attributes later on to have more bell-shaped distributions.

Wait! Before you look at the data any further, you need to create a test set, put it aside, and never look at it.

### Create a test set

<< Data snooping bias; Strata/Stratum >>

To have a stable train/test split even after updating the dataset, a common solution is to use each instance’s identifier to decide whether or not it should go in the test set (assuming instances have a unique and immutable identifier).

`~np.array([True, ...]) == np.array([False, ...])`

The simplest function (of `sklearn.model_selection`) is `train_test_split()` ... First, there is a random_state parameter that allows you to set the random generator seed. Second, you can pass it multiple datasets with an identical number of rows, and it will split them on the same indices (this is very useful, for example, if you have a separate DataFrame for labels).

Stratified sampling.

- Create an income category attribute.
- Should not have too many strata; each stratum should be large enough.

## Explore the data to gain insights.

`data.plot(kind="scatter",x,y,alpha)`.

`data.plot(kind="scatter",x,y,alpha,s,c,cmap="jet")`.

`.corr()`. Only measures linear correlations.

- `pandas.scatter_matrix()`.


## Prepare the data to better expose the underlying data patterns to Machine Learning algorithms.

`sklearn.impute.SimpleImputer`.

## Explore many different models and shortlist the best ones.

## Fine-tune your models and combine them into a great solution.

## Present your solution.

8. Launch, monitor, and maintain your system.

