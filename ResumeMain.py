from google import genai
import api_secrets


def get_job_description() -> str:
    # if this were a later sprint I would get this from something other than a pasted in job
    return """This is a remote position.\n
    ****Senior / Principal Backend Software Engineer** \n
     (5 year experience, remote)**\n 
     About us: Be part of our future! This job posting builds our talent pool for potential future openings. We'll 
     compare your skills and experience against both current and future needs. If there's a match, we'll contact you directly.
      No guarantee of immediate placement, and we only consider applications from US/Canada residents during the application process.
      Hiring Type: Full\\-Time\n   \n\n  \n\n Base Salary: $100K\\-$120K Per Annum
       Candidates must be authorized to work in the United States full\\-time. We are not able to sponsor applicants for
        work visas at this time.\n   \n\n  \n\n Benefits:\n   \n\n  \n\n* We offer health benefits and generous PTO 
        packages.\n* Our office is dog friendly, has unlimited snacks \\& drinks, flexible working hours (get out for 
        the pow day!), and lots of rock climbing \\& skateboarding.\n* We offer competitive healthcare benefits and a 
        401k program.\n* we are committed to being a fun, groundbreaking, and inclusive place to work. We strongly encourage
         engineers from all community and traditionally underrepresented backgrounds to apply\n\n\n**About The Role**\n 
         We\u2019re looking for people with a strong technical background and a passion for building products, not just features.
           \n\n  \n\n This is not a management but a full time hands\\-on position: you will spend the majority of your time coding.
              \n\n  \n\n As an engineer at Team Remotely , you will:\n   \n\n  \n\n Design, build and maintain Team Remotely 
              products, services and features\n   \n\n  \n\n Write technical design docs and customer\\-facing documentation
                \n\n  \n\n Carry out code reviews\n   \n\n  \n\n Address customer issues\n  
                Build tooling to monitor and analyze Team Remotely services, both in terms of performance and security
                  \n\n  \n\n Take part in the on\\-call rota\n   \n\n  \n\n Coordinate your work with our frontend engineers 
                  and designers\n   \n\n  \n\n Have broad exposure to our entire architecture\n   \n\n  \n\n
                   You will use: Go (Golang)\n   
                   GCP\n   \n\n 
                    \n\n Hardware Security Modules (HSM)\n   
                   n Postgres and MySQL\n   \n\n  \n\n Terraform\n  
                    Docker\n   
                    Redis\n   \
                     Please note:
         The exact level of the role (Senior or Principal) will depend on your experience and interview 
          performance\n   \n\n  \n\n Team Remotely is remote\\-first and we offer flexible working arrangements
           to help our team manage their daily lives in the way that works best for them\n
         if you are not located in the US, you will be hired either via a B2B contract or through an employer
         of record\n   \n\n  \n\n You are a good fit if you Have experience as a cloud or backend engineer 
          for a multi\\-tenant large scale mission critical system\n   \n\n  \n\n Have a strong understanding
           of reliability practices, distributed systems, and cloud native architectures
           Care about application security, scalability and performance\
           Understand and apply engineering best practices, including appropriate testing paradigms and effective 
           peer code reviews\n   \n\n  \n\n Have a good understanding of multi\\-threading, concurrency, 
            and parallel processing technologies\n   \n\n  \n\n Are comfortable working with a high degree 
             of independence and minimal process\n   \n\n  \n\n Thrive in a fast\\-paced, collaborative 
              and iterative environment\n   **Care Deeply About User Experience And Developer Experience**\n
             Enjoy working with a diverse group of people with different backgrounds and expertise"""


def get_contact_info() -> str:
    # again for a later sprint I would get this from a data source, but just hard coded for now
    return """
    John F. Santore, Ph.D
DMF Science and Math Center 333
Bridgewater State University
(508)-531-2226
jsantore@bridgew.edu
    """


def get_skills() -> str:
    # same caveat as get_contact_info above
    return """
    git
    github actions
    gitlab pipelines
    golang
    gin web framework
    python
    grpc
    C++
    lisp
    java
    SQL
    postgresql
    sqlite3
    """


def get_constraints() -> str:
    return """
    give me only the resume in markdown format without any additional notes or extra cruft
    Use only skills and projects listed in the prompt - don't add any
    omit skills and projects that don't support this job description.

    """


def get_education() -> str:
    # again hard coded for sprint1
    return """
    BA in Cognitive Science from University of Rochester
    MS in Computer Science from University at Buffalo
    Ph.D in Computer Science from University at Buffalo
    """


def get_experience() -> str:
    return """
    DownEast Technology (3 years)
    team delivered an app for sales people to enter, track and synch full spectrum sales data, saving it both locally
    in the sales persons device and synching it to the company so that nothing is lost and multiple sales people working
    the same lead don't waste time covering the same ground. App built in C++ with significant SQL component 
    
    Weston Books (2 years) 
    Built an inventory management and cash register program for a bookstore in golang. Program used a bar code reader 
    to read ISBN numbers from the bar codes and queried book API to auto fill most field when stocking books. Data stored 
    in SQL database. Application produced PDF reports for inventory, sales and more.
    
    WheresMyJob.com (3 years)
    Delivered an application that pulled data from jobs APIs and displayed them on a map, displaying full data when 
    a job was selected by the user. Users filter jobs to not be overwhelmed. App written using python, pandas, plotly, dash,
    geopy, requests and postgresql database. AI integration helps users auto generate resumes from a set of skills and a 
    selected job.
    
    """

def get_references() -> str:
    return """
    Dr. Seikyung Jung (Long Time colleague and team member at Wheresmyjob, She can speak to my ability to work with team 
    members who go from peer to supervisor. She succeeded me as team lead.)
    sjung@bridgew.edu


Dr. Enping Li (junior colleage at wheresmyjob for the last 3 years, she can speak on my ability to work with and mentor 
junior team members)
eli@bridgew.edu


Dr, Pallavi Mathew (former colleague at Weston Books and meetup cohost.)
Pallavi@WestonBooks.com
    """

def get_service()->str:
    # same caveat as above
    return """
    Meetup cohost:
    organized golang meetup for Providence RI. Arranged venue, organized speakers and worked with co-host and members
    to keep the meetup viable
    
    K-12 outreach:
    worked with local University on an initiative that brought middle school girls from a school that pulled 100% of its 
    students from inner city residents of disadvantaged backgrounds to campus for a series of hands on seminars in STEM. 
    The purpose was to both introduce these middle school students to the University, and get them to see themselves at 
    the University, expanding opportunities.
    """

def google_generate_resume(
    job_desc: str,
    contact_info: str,
    skills: str,
    education: str,
    constraints: str,
    experience: str,
        service: str,
        refs:str
):
    # this original code came from the google api docs before I marked it up.
    client = genai.Client(api_key=api_secrets.gemini_api_key)
    prompt = f"""build a markdown resume for a job with the following description: {job_desc}
    for an applicant with the following contact info: {contact_info} and skills: {skills}
    the following education {education}, and the following professional work experience{experience} 
    the following professional service {service}
    and these professional references {refs}
    and constraints {constraints}
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    print(response.text)  # for debugging purposes only
    with open("resume.md", "w") as file:
        file.write(response.text[9:-3])


def main():
    google_generate_resume(
        get_job_description(),
        get_contact_info(),
        get_skills(),
        get_education(),
        get_constraints(),
        get_experience(),
        get_service(),
        get_references()
    )


if __name__ == "__main__":
    main()
