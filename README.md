
# Job Matching System

The Job Matching System is designed to assist recruiters in effectively matching candidate profiles to job descriptions (JDs). By leveraging text processing and similarity algorithms, the system identifies suitable job roles for candidates based on extracted information from resumes and JDs.






## Run Locally

Clone the project

```bash
  git clone https://github.com/vaghani04/Job_Matching_System.git
```

Add job decriptions in `.\inputs\job_decriptions.txt` and put resume.pdf in `.\inputs` directory

Install all the dependencies

```bash
  pip install -r requirements.txt

```

run the app.py from resume_parser to extract data from resume

```bash
  python .\resume_parser\app.py
```

run the app.py from jd_parser to extract data from resume

```bash
  python .\jd_parser\app.py
```

run the `mathcing_analysis.py` from `match_engine` to find similarities between skills, education, experience, and technologies.

```bash
  python .\match_engine\mathcing_analysis.py
```

run the `match_profiles.py` from `match_engine` to find similarities between all JDs and resume

```bash
  python .\match_engine\match_profiles.py
```

Now you can see all parsed resumes `.json` file in the `.\outputs` directory and all the similarities in `.json` in the `.\outputs\jd_similarity\` directory.
