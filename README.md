# Exercise Sheet 5 Solution

Replace `YOUR_GITHUB_USERNAME` and `exercise-sheet-5` with your own GitHub username and repository name.

## Files

- `mergesort.py`: cleaned merge sort code and improved plotting.
- `single_element.py`: efficient solution for Exercise 2.
- `tests/test_single_element.py`: pytest tests for the algorithm.
- `tests/test_libraries.py`: test showing that numpy, pandas, matplotlib and seaborn are installed.
- `Dockerfile`: installs numpy, pandas, matplotlib, seaborn and pytest.
- `docker-compose.yml`: provides two services: running tests and running the method.
- `.gitignore`: ignores `to_be_ignored.txt` and common Python cache files.

## Exercise 1 commands

### a) Create local repository, add files and commit

```bash
mkdir exercise-sheet-5
cd exercise-sheet-5
git init
cp ../mergesort.py .
cp ../to_be_ignored.txt .
git add mergesort.py to_be_ignored.txt
git commit -m "Add initial exercise files"
```

### b) Create .gitignore and remove ignored file from Git history

```bash
echo "to_be_ignored.txt" > .gitignore
echo "__pycache__/" >> .gitignore
echo ".pytest_cache/" >> .gitignore
echo "*.pyc" >> .gitignore

git rm --cached to_be_ignored.txt
git add .gitignore
git commit -m "Ignore unnecessary text file"
```

### c) Create feature branch, clean mergesort.py and commit

```bash
git switch -c clean-mergesort
# Replace mergesort.py with the cleaned version from this solution folder.
git add mergesort.py
git commit -m "Clean and document merge sort implementation"
```

At least 7 improvements in `mergesort.py`:

1. Replaced unclear function name `mergeSort` with `merge_sort`.
2. Replaced uppercase helper `ASSIGNMENT` with direct assignments and a clearer `merge` function.
3. Removed redundant conditions such as `not len(...) < 1` and `len(...) != 0`.
4. Added docstrings.
5. Added a `main()` function.
6. Added `if __name__ == "__main__"` guard.
7. Used descriptive variable names instead of `l`, `r`, and `i`.
8. Split sorting, merging and plotting into separate functions.
9. Added type hints.

### d) Create public GitHub repository, set SSH, add remote

Create a public repository on GitHub first. Then run:

```bash
ssh-keygen -t ed25519 -C "YOUR_EMAIL@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Copy the printed public key to GitHub:
Settings → SSH and GPG keys → New SSH key.

Then add the remote:

```bash
git remote add origin git@github.com:YOUR_GITHUB_USERNAME/exercise-sheet-5.git
git remote -v
```

### e) Switch back to main and push

```bash
git switch main
git push -u origin main
```

### f) Modify plotting on main, commit and push

```bash
# Modify the plotting part of mergesort.py on main.
# A bar plot is better here because we compare discrete list elements by index.
git add mergesort.py
git commit -m "Improve merge sort visualization"
git push origin main
```

### g) Switch to feature branch, fork and create pull request

```bash
git switch clean-mergesort
```

Now another user, or your own account if the repo is inside an organization, must fork the repository on GitHub.

Add the fork as another remote:

```bash
git remote add fork git@github.com:OTHER_USERNAME/exercise-sheet-5.git
git push -u fork clean-mergesort
```

Then open GitHub and create a pull request from:

`OTHER_USERNAME:clean-mergesort` into `YOUR_GITHUB_USERNAME:main`.

### h) Resolve conflicts by merging main into feature branch

```bash
git switch clean-mergesort
git merge main
# Resolve conflicts in mergesort.py manually.
git add mergesort.py
git commit -m "Resolve merge conflict with main"
git push fork clean-mergesort
```

Then go back to GitHub and merge the pull request.

### i) Pull merged main and delete local feature branch

```bash
git switch main
git pull origin main
git branch -d clean-mergesort
```

View history:

```bash
git log --oneline --graph --all
```

## Exercise 2 commands

Run tests locally:

```bash
pytest -q
```

Run method locally:

```bash
python single_element.py 1 2 3 4 3 1 2
```

Expected output:

```text
4
```

Run with Docker Compose:

```bash
docker compose up --build run-tests
docker compose up --build run-method
```

## What to upload

The sheet asks for the complete Git repository folder including the hidden `.git` folder. After you have run all Git commands and added your GitHub link, zip the whole repository folder.

Example:

```bash
cd ..
zip -r yourname_12345678.zip exercise-sheet-5
```
