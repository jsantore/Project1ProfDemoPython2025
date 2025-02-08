# Prof Demo of Sprint 1
## Prof Santore

# To run

* install libraries in requirements.txt
* create api_secrets.py
  * add `gemini_api_key = <your api key here>`
* run ResumeMain.py


## AI syatem chosen
    I chose Google's Gemini because about 80% of you did

## getting to a good prompt
  I forst tried just putting in skills and education and the job description. This caused the AI to 
  "hallucinate" several skills including French that I don't have.
  I added additional items for the resume to use like references and service. However, the LLM continued
  to add junk. Finally, I added constraints, first one then more, till I had only an accurate resume.