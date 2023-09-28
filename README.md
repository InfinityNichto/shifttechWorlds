# shifttechWorlds
shifttech server world archive, updated every hour. Website coming soon!

.yml file:
```name: Download Shifttech Worlds
on:
  schedule:
    - cron: "0 * * * *"

jobs:
  download:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Download Shifttech Worlds
      run: |
        mkdir -p worlds
        wget -np -nH -nd -N -rv -P worlds http://shifttech.xyz:8081/shifttechterraria/hourly/
      working-directory: ${{ github.workspace }}

    - name: Commit and push changes
      run: |
        git config user.name "GitHub Actions"
        git config user.email "actions@github.com"
        git add worlds
        git commit -m "Auto-download"
        git push
```
