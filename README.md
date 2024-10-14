# weather-forecast-app
A Python application that fetches weather data using the Open-Meteo API.

## Issues
Issue: The city input was case-sensitive.
Solution: Updated the input to handle both lowercase and uppercase city names.

Issue: User needed temperature in Fahrenheit.
Solution: Implemented a unit conversion feature.

## More Issues

### Untracked Files
Issue: After running `git status`, I noticed that my file (`weather-forecast-app.py`) was listed as "untracked."
Solution: I used the command `git add weather-forecast-app.py` to stage the file for committing.

### Error When Committing
Issue: Attempted to commit changes but received an error about no files being staged.
Solution: I verified that I had staged the file using `git add`. After staging the file, I successfully committed using `git commit -m "Initial commit: added weather forecast app script"`.

### Confusion About Branch Name
Issue: Initially, I thought I was on the "main" branch but realized I was on the "master" branch.
Solution: I checked my current branch with `git branch` and noted that my repository was still using "master." I ensured I used `git push -u origin master` when pushing.

### Issues with GitHub Connection
Issue: After running `git push`, I encountered an error saying that the repository did not exist or I did not have permission.
Solution: I checked the remote URL using `git remote -v` and found that I had entered the wrong repository URL. I corrected it using `git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git`.

### Need to Keep Sensitive Information Secure
Issue: I realized I should not include sensitive information (like API keys) in my GitHub repo.
Solution: I created a `.gitignore` file to exclude certain files from being tracked and added the relevant patterns (like `.env`) to it.

### Pushing Changes Not Reflecting on GitHub
Issue: After pushing, my changes did not appear on GitHub.
Solution: I verified that I was pushing to the correct branch and that there were no errors during the push process. I used `git log` to ensure my commits were recorded correctly.
