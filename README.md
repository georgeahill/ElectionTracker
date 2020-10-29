# ElectionTracker

## Requirements

Return election number data from AP
 - Presidential Race (electoral college/states)
 - Senate Race (seats/states)
 - House Race (seats/states)

Put election data into Google Sheet (why not csv?)

Edit JSON format on-the-fly
 - file location
 - file format

Deploy on the web? Stretch goal
 - If this doesn't work, run locally

## Work Elements
 - Back End
   - JSON File Parsing
     - Including Mutability - this is vvv. important
     - This involves format design as well as parsing
     - Transform data from AP into nice format for front end
   - File Scraping
     - Get file from AP - must be easily changeable
     - Update every `n` seconds
   - API
     - Required if hosting
 - Front End
   - Google Sheets/CSV
   - Nice Front End shit
     - Required if hosting
     - Doesn't have to be fancy - just functional
 - Integration between front/backend
 - Local run
 - Deployment
     - Required if hosting
   - CI/CD
   - Hosting etc.
 - And all before Tuesday! That's 5 days which is plenty of time.