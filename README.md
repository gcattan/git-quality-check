<img type="image/svg" src="https://byob.yarr.is/gcattan/git-quality-check/score"/>

# git-quality-check
Simple tool to check quality of git commits, and build indicators on it.
Four estimation are performed:
- the percent of commits containg a list of prohibited words;
- the percent of commits related to testing;
- the percent of branches with last commit having more than 2 months old;
- the percent of coupled branches.
A branch is coupled to another branch if it is contained in this other branch history (`git branch --contains...`).
When there is more than 10 branches, the program randomly select 10 branches among all branches plus the branches passed through the `mainBranches` input.

The overall score returned as an output is a combination of these score.
The closer to 100%, the higher the quality.

## Examples

Place the folowing example in your `.github/workflows` repository (in a file called `test-action.yml`) for example:

```
name: Test Action

on: [push]

jobs:
  build-linux:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v3
      with:
        fetch-depth: 0
    - name: Git Quality Check
      id: git-quality-check
      uses: gcattan/git-quality-check@v0.1
      with:
        badWords: WIP, todo
        mainBranches: origin/master, origin/develop, origin/main
    - name: Check outputs
      run: |
        test "${{ steps.git-quality-check.outputs.score }}" != ""
```

The example above will checkout and run `git-quality-check` on your repo.

## Description of inputs

|Field|Descrition|
|-|-|
|badWords|A list of words that should be avoided in a commit message.|
|mainBranches|Coupling of other branches with these main branches will be always checked.|

## Description of output

|Field|Descrition|
|-|-|
|score|The overall score for your repository. It takes into account the percent of "bad" commits, commits related to testing, old branches and coupling.|

## Adding a badge to your README

You may find convenient to add a badge on your readme to display the score obtained with git quality check.
This is a two steps process:

1) Add https://github.com/RubbaBoy/BYOB action at the end of your `test-action.yml` file as follows:

```
- name: Create badge
      uses: RubbaBoy/BYOB@v1.3.0
      with:
        NAME: score
        LABEL: 'Git Quality Score'
        STATUS: ${{ steps.git-quality-check.outputs.score }}
        COLOR: 00EEFF
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

You can find the complete example of `test-action.yml` [here](.github/workflows/test-action.yml).

2) Add this line to your `README`:

```<img type="image/svg" src="https://byob.yarr.is/<your github account>/<your project>/score"/>```

Do not forget to replace <you github account> and <your project> in the above!!
