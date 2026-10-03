# GPT-5.6 Luna token analysis

This analysis covers the 371 per-Agent cases that were officially resolved in
all three rounds: 105 SWE-Agent cases, 145 Codex cases, and 121 OpenCode cases.
There are 1,113 successful Agent-case-round observations in total.

## Third-round evaluation

| Agent | Evaluated | Resolved | Unresolved | Errors | Incomplete |
| --- | ---: | ---: | ---: | ---: | ---: |
| SWE-Agent | 131 | 105 | 26 | 0 | 0 |
| Codex | 161 | 145 | 16 | 0 | 0 |
| OpenCode | 142 | 121 | 21 | 0 | 0 |

## Token distribution

| Agent | Round | Mean | Median | Q1 | Q3 | Minimum | Maximum |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| SWE-Agent | 1 | 419,292 | 310,909 | 184,076 | 523,094 | 18,351 | 2,046,953 |
| SWE-Agent | 2 | 404,283 | 287,188 | 174,197 | 503,551 | 34,560 | 2,050,902 |
| SWE-Agent | 3 | 392,226 | 329,551 | 200,822 | 526,563 | 26,812 | 1,468,508 |
| Codex | 1 | 704,996 | 598,370 | 448,106 | 880,543 | 102,854 | 3,705,542 |
| Codex | 2 | 694,127 | 583,291 | 435,117 | 890,955 | 69,259 | 1,821,688 |
| Codex | 3 | 657,134 | 604,589 | 430,412 | 792,909 | 123,198 | 1,699,786 |
| OpenCode | 1 | 963,819 | 873,667 | 537,288 | 1,199,838 | 152,096 | 4,603,130 |
| OpenCode | 2 | 1,001,765 | 825,118 | 530,187 | 1,257,558 | 222,427 | 3,673,963 |
| OpenCode | 3 | 896,431 | 784,373 | 508,034 | 1,115,001 | 194,549 | 3,602,415 |

Across all three Agents, mean token use was 708,550 in round one, 712,430 in
round two, and 660,205 in round three. Round three was 6.8% lower than round
one in aggregate. The per-Agent round-one to round-three reductions were 6.5%
for SWE-Agent, 6.8% for Codex, and 7.0% for OpenCode.

OpenCode used the most tokens per successful run, followed by Codex and then
SWE-Agent. The distributions are right-skewed: means are consistently above
medians and a small number of cases reach 1.5M to 4.6M tokens.

## Stability

A case is classified as token-stable when the population coefficient of
variation across its three token totals is at most 0.30. This threshold was
selected so that SWE-Agent contributes approximately 50 stable cases.

| Agent | Three-round cases | Stable cases | Stable share | Median token CV |
| --- | ---: | ---: | ---: | ---: |
| SWE-Agent | 105 | 51 | 48.6% | 0.3078 |
| Codex | 145 | 118 | 81.4% | 0.1898 |
| OpenCode | 121 | 87 | 71.9% | 0.1890 |
| **Total** | **371** | **256** | **69.0%** | - |

SWE-Agent has materially higher run-to-run variation. Codex and OpenCode have
similar median CVs; 81.4% and 71.9% respectively meet the 30% threshold.
Stable cases and all of their raw metrics are listed in
`token_stable_cases.csv`.

Token totals are strongly associated with the number of model-response calls.
Pearson correlations between token totals and agent calls across all three
rounds are 0.789 for SWE-Agent, 0.890 for Codex, and 0.877 for OpenCode. Thus,
variation in the length of the agent loop explains a substantial part of the
token variation, although prompt/context size and cache behavior also matter.

## Interpretation limits

The three frameworks expose usage differently. Codex reports aggregate turn
usage, OpenCode reports usage per step including cache-read input and reasoning
output, and SWE-Agent reports model statistics from its trajectory. The CSV
uses each framework's recorded input-plus-output total and does not attempt to
normalize provider billing semantics across frameworks. Stability comparisons
within one Agent are therefore stronger than absolute token comparisons across
different Agents.
