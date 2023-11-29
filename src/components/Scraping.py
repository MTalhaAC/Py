import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
async def scrape_website(url):
    # browser = await launch()
    browser = await launch({'headless': True})
    page = await browser.newPage()
    # page.setDefaultNavigationTimeout(6000)
    urls:str = url
    try:
      await page.goto(url, waitUntil='networkidle0')
      
      html = await page.content()
      # You may need to wait for some time to ensure all content is loaded
      # await page.waitForSelector('your_selector')
      
      click_options = {
        'button': 'left',
        'clickCount': 2,
        'delay': 100
      }
      
      
      
      if html.__len__() > 0 :
        # closed the models
        # if(html.find('button', class_="modal__dismiss").getText().strip().count() > 0):
        if urls.__contains__("muhammadtalha028989"):
          await page.click(".modal__dismiss", click_options),
          await page.click(".cta-modal__dismiss-btn", click_options),
        
        soap = BeautifulSoup(html,"html.parser")
        
        # check if sign up model is available or not
        isSignedUpModel = soap.find("button", class_="sign-in-modal__outlet-btn").get_text(strip=True).__contains__("Sign in")
        
        if isSignedUpModel is True:
          await page.click(".sign-in-modal__outlet-btn", click_options)
                  # Wait for the sign-in modal to appear
          await page.waitForSelector("#public_profile_contextual-sign-in_sign-in-modal_session_key")

          # Set email value
          await page.type("#public_profile_contextual-sign-in_sign-in-modal_session_key", "miansonu776932@gmail.com")

          # Set password value
          await page.type("#public_profile_contextual-sign-in_sign-in-modal_session_password", "")
          
          await page.click(".sign-in-form__submit-btn--full-width", click_options)
        
        
        await asyncio.sleep(2)
        # Get the plaintext content of the page
        await page.screenshot({'path': 'src/assets/ss/test.png'})
        # Linkedin profile scrapping
        # title of profile
        title = soap.find("h1", class_="top-card-layout__title").get_text(strip=True)
        # skills
        subTitle = soap.find("h2", class_="top-card-layout__headline").get_text(strip=True)
        skills = subTitle.split("|")
        
        # Abount
        
        about = soap.find("div", class_="core-section-container__content").find("p").get_text(strip=True)
        aboutTitle = soap.find("h2", class_="core-section-container__title").get_text(strip=True)
        # Experience 
    

        experience = soap.find("section", class_="experience")
        experienceTitle = experience.find("h2", class_="core-section-container__title").get_text(strip=True)
        
        if experience.__len__() > 0:
          
          companyTitle = experience.find("h3", class_="profile-section-card__title").get_text(strip=True)
          
          companySubTitle = experience.find("h4", class_="profile-section-card__subtitle").getText().strip()
      
          experience_duration = experience.find("p", class_="experience-item__duration").get_text(strip=True).split("\n")  
          
          location = experience.find("p", class_="experience-item__location").get_text(strip=True)
        
          description = experience.find("p", class_="show-more-less-text__text--less").get_text(strip=True)
          
        # Education
        
        education = soap.find("section", class_="education")

        educationTitle = education.find("h2", class_="core-section-container__title").get_text(strip=True)
        
        educationContent = education.find("ul", class_="education__list").find("div", class_="profile-section-card__contents")
        
        universityName = educationContent.find("h3", class_="profile-section-card__title").get_text(strip=True)
        
        courses = educationContent.find("h4", class_="profile-section-card__subtitle").get_text(strip=True).split("\n")
        
        educationDuration = educationContent.find("p", class_="education__item education__item--duration").get_text(strip=True).split("\n")
              
        educationDescription = education.find("p", class_="show-more-less-text__text--less").get_text(strip=True)
        
        # Volunteer information
        volunteering = soap.find("section", class_="volunteering")

        volunteeringHeader = volunteering.find("h2", class_="core-section-container__title").get_text(strip=True)
        
        volunteeringContent = volunteering.find("div", class_="profile-section-card__contents")
        
        volunteeringTitle = volunteeringContent.find("h3", class_="profile-section-card__title").get_text(strip=True)
        
        volunteeringSubTitle = volunteeringContent.find("h4", class_="profile-section-card__subtitle").get_text(strip=True).split("\n")
        
        volunteeringDuration = volunteeringContent.find("p", class_="volunteering__item volunteering__item--duration").get_text(strip=True).split("\n")
              
        volunteeringDescription = volunteering.find("p", class_="show-more-less-text__text--less").get_text(strip=True)
        
        
        # Licenses and certification
        certifications = soap.find("section", class_="certifications")

        certificationsHeader = certifications.find("h2", class_="core-section-container__title").get_text(strip=True)
        
        certificationsContent = certifications.find("div", class_="profile-section-card__contents")
        
        certificationsTitle = certificationsContent.find("h3", class_="profile-section-card__title").get_text(strip=True)
        
        certificationsSubTitle = certificationsContent.find("h4", class_="profile-section-card__subtitle").get_text(strip=True).split("\n")
        
        
        # Project
        
        projects = soap.find("section", class_="projects")
        
        listOfProjects = projects.find("ul", class_="projects__list").find_all("li")

        projectListObject = list()
        
        for project in listOfProjects:
          title = project.find("h3").get_text(strip=True)
          subTitle = project.find("h4").get_text(strip=True)
          # description = project.find("p", class_="show-more-less-text__text--less").get_text(strip=True)
          projectListObject.append({
          "title": title,
        })
        
        profile = {
          "fullname": title,
          "skills": [skill.strip() for skill in skills],
          "about": {
            "title": aboutTitle,
            "paragraph": about
          },
          "experience": {
            "title": experienceTitle,
            "content": {
              "company_name": companyTitle,
              "sub_title": companySubTitle,
              "duration": experience_duration,
              "location": location,
              "description": description
            }
          },
          "education": {
            "title": educationTitle,
            "content":{
              "university_name": universityName,
              "course_name": courses,
              "education_duration": educationDuration,
              "education_description": educationDescription
            }
          },
          "volunteering":{
            "title": volunteeringHeader,
            "content":{
              "title": volunteeringTitle,
              "sub_title": volunteeringSubTitle,
              "duration": volunteeringDuration,
              "description": volunteeringDescription
            }
          },
          "certification":{
            "title": certificationsHeader,
            "content":{
              "title": certificationsTitle,
              "sub_title": certificationsSubTitle
            }
          }
        }
        print(projectListObject)
      else:
        print("HTML file not found")
    finally:
      # Close the browser
      await browser.close()


