<img type="image/svg" src="https://byob.yarr.is/gcattan/git-quality-check/score"/> 
 
# git-quality-check (WIP)
Simple tool to check quality of git commits, and build indicators on it.
Four estimation are performed:
- the percent of commits containg a list of prohibited words;
- the percent of commits related to testing;
- the percent of branches with last commit having more than 2 months old;
- the percent of coupled branches.
A branch is coupled to another branch if it is contained in this other branch history (`git branch --contains...`).
When there is more than 10 branches, the program randomly select 10 branches among all branches plus the branches passed through the `mainBranches` input.

The overall score returned as an output is a combination of these scores.
The closer to 100%, the higher the quality.

An example is available [here](.github/workflows/test-action.yml).

## Description of inputs

|Field|Descrition|
|-|-|
|badWords|A list of words that should be avoided in a commit message.|
|mainBranches|Coupling of other branches with these main branches will be always checked.|

## Description of output

|Field|Descrition|
|-|-|
|score|The overall score for your repository. It takes into account the percent of "bad" commits, commits related to testing, old branches and coupling.|
