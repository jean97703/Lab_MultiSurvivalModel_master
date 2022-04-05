import MultiSurvivalModelClasses as Cls
import SimPy.Plots.SamplePaths as Path
import SimPy.Plots.Histogram as Hist

MORTALITY_PROB = 0.1    # annual probability of death
TIME_STEPS = 100        # years
N_COHORTS = 500         # number of cohorts
COHORT_POP_SIZE = 100   # size of each cohort
ALPHA = 0.05            # significance level

# create multiple cohorts
multiCohort = Cls.MultiCohort(
    ids=range(N_COHORTS),   # [0, 1, 2 ..., N_COHORTS-1]
    pop_sizes=[COHORT_POP_SIZE]*N_COHORTS,  # [COHORT_POP_SIZE, COHORT_POP_SIZE, ..., COHORT_POP_SIZE]
    mortality_probs=[MORTALITY_PROB]*N_COHORTS  # [p, p, ....]
)

# simulate all cohorts
multiCohort.simulate(TIME_STEPS)

# plot the sample paths
Path.plot_sample_paths(
    sample_paths=multiCohort.multiCohortOutcomes.survivalCurves,
    title='Survival Curves',
    x_label='Time-Step (Year)',
    y_label='Number Survived',
    transparency=0.5)

# plot the histogram of average survival time
Hist.plot_histogram(
    data=multiCohort.multiCohortOutcomes.meanSurvivalTimes,
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count')

# print projected mean survival time (years)
print('Projected mean survival time (years)',
      multiCohort.multiCohortOutcomes.statMeanSurvivalTime.get_mean())

# print projection interval
print('95% projection (prediction, percentile, or uncertainty) interval of average survival time (years)',
      multiCohort.multiCohortOutcomes.statMeanSurvivalTime.get_PI(alpha=ALPHA))
