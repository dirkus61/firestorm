# Firestorm

## Intent

The Firestorm project was put together to facilitate speaker topic selection
for the Python Utah North usergroup in Logan, Utah.  This project begun
development on 10/29/2015 as part of a Python Hack Night.

## Overall Application Behavioral Design

The thought is that we will allow all users of the application to
simultaneously log in during our Meetup event and concurrently add/edit topics
for discussion as well as collaboratively vote on upcoming speaker topics.  We
would also like to have some sort of kiosk-type display that can continuously
update the current state of our topic discussion on the projector.  That way,
as users add topics and express their desire/skillset for presentation, we can
negotiate topics that interest everybody.

## Current State

We have a basic project infrastructure put together through this repository.
We believe we have a good start at the definition of the database
models/schema.  Additionally, we have a simple authentication system that will
create users on-the-fly with only an email address required as a credential.
As this is an internal-only type application, this lack of security should
suffice.

## Best Practices

Several items have been agreed upon by the developers:

1. We will make every effort to adhere strictly to PEP8.

2. All code will be developed against a branch of an individual's fork of the
application.  When the code is ready for merge (or feedback), a GitHub "pull-
request" will be created to represent the desired merge.  The code will be
visually inspected against obvious syntactical problems or design quality.
Also, the code will be evaluated for consistency and PEP8 compliance.  Feedback
will be provided against that pull request or agreement for merge.

3. Every effort should be made to keep our PyLint score at or above an 8.

## Next Steps

Currently, we need work done on the following items:

1. Presentation/Layout.  Somebody with some design skills needs to make it
look professional.

2. Kiosk display.  We want to dynamically display the topics, ordered by
user interest in some fashion that promotes positive discussion as to our next
topic selection.

3. Mechanisms to create/edit/list topics.

4. Mechanisms to vote on topics with 2 facets: A) User interest,
B) current skillset/desire to present on the topic.

5. Some scheduling mechanism for documenting a speaker/topic/date.

6. Some feedback recording mechanism for providing feedback after a
presentation.  This also should provide some way of indicating that the user
did not attend the meeting.  Additionally, topics should be closed for feedback
after a certain time has lapsed (45 days?).  A user should be able to decline
providing feedback and not be bothered again for the particular event.  A
user should also be able to edit feedback they have historically provided.

7. A mechanism for the user to be able to receive/view the feedback they have
received.

8. A user needs to be able to update their profile (first/last name) as well
as disable their account.  Disabled accounts should not have their topic
votes considered, however their feedback on prior meetings should be retained.
