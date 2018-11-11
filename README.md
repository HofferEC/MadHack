## Inspiration

One of our team members is deeply enveloped in the music game. When brainstorming ideas, we soon realized that making custom Alexa skill that would automatically generate lyrics would be entertaining for both us the developers and for the end users. 

## What it does

It receives user input word from an Alexa command. Based on that word, it generates a short "freestyle rap" of rhymed couplets, that Alexa reads back to the user. The rap generated is both randomized and context-driven.

## How we built it

We developed a custom Alexa skill through the Alexa developer page. We send the Alexa Skill Event to AWS lambda, where the user input is parsed and set to an external web server for processing. On the web server, we execute a couple PHP files and a main Python script that generates the rap through usage of a dictionary API and a web scraper. 

## Challenges we ran into

After successfully developing and running our web scraper, we were promptly IP-banned from the first lyrics site we used for sending too many requests in a short period of time. We spent a lot of time on developing solutions to this issue and eventually created a scraper that not only works but is more time efficient than its previous iteration.

## Accomplishments that we're proud of

Many team members were able to effectively complete tasks we had no previous experience in, including new languages, API's, SDK's, hardware, and libraries. We also finished on time, were able to sleep and include all the applicable error-handling that is required for smooth execution.

## What we learned

### Technical learning objectives
* Alexa Skill integration
* AWS Lambda functions
* Beautiful Soup 4
* Requests library for API requests
* Python

### Interpersonal learning objectives
* Communication skills
* Time management
* Task assignment
* Efficient Allocation of resources

## What's next for DJ Lil Lex

Future improves would include counting syllables so that couplets and stanzas have uniform length. We would include options for language filtering. We would include more variance in the rhyming schemes. We would also try to standardize the rate at which Alexa reads the output so that she would read lines "on beat". 

## Authors

Caleb Floyd    |  ctfloyd@wisc.edu
Tim Schabel    |  tschabel@wisc.edu
Nicholas Hoff  |  nbhoff@wisc.edu

#Developed in 24 hours for Madhacks Fall 2018 Hackathon
