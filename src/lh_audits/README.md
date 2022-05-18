# Automated Lighthouse Audits

We will use Lighthouse CLI to automate experiments on a bulk of popular webpages and then we will extract and visualize the frequency of failed audits.

After cloning the repository:


- First install Lighthouse CLI

```sh
npm install -g lighthouse
```



- Then run the bash script:

```sh
bash lh_500_run.sh
```
It will run Lighthouse experiments on Alexa 500 webpages while simulating a mobile device. It will store the reports of each experiments in a CSV file in the current directory.



- Lastly, run the python script "extract_opportunities.py" to grab the frequency of failed audits from all the CSV files generated for each website:

```sh
python3 extract_opportunities.py
```

The count for failed audits will be store in "failed_audits_freq.csv"

<br>

